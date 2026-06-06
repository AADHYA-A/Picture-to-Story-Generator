import base64
import requests
from PIL import Image
import io

# Ollama API base URL (default local endpoint)
OLLAMA_BASE_URL = "http://localhost:11434"

# Model names — update these to match what you have pulled in Ollama
VISION_MODEL = "llava"       # For image captioning (vision-capable)
TEXT_MODEL = "llama3"        # For story generation


def encode_image_to_base64(image_path: str) -> str:
    """Convert an image file to a base64-encoded string for Ollama."""
    with Image.open(image_path) as img:
        # Convert to RGB to ensure compatibility
        img = img.convert("RGB")
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")


def get_image_caption(image_path: str) -> str:
    """
    Use Ollama's vision model (e.g. llava) to generate a description of the image.
    """
    image_b64 = encode_image_to_base64(image_path)

    payload = {
        "model": VISION_MODEL,
        "prompt": (
            "Describe this image in detail. "
            "Focus on the subjects, setting, mood, colors, and any notable details. "
            "Be descriptive and vivid."
        ),
        "images": [image_b64],
        "stream": False,
    }

    response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
    response.raise_for_status()
    return response.json().get("response", "").strip()


def generate_story_text(
    caption: str,
    genre: str,
    style: str,
    word_count: int,
    creativity: float,
) -> str:
    """
    Use Ollama's text model to generate a story based on the image caption.
    creativity maps to the `temperature` parameter (0.3 – 1.0).
    """
    prompt = (
        f"You are a creative writer. Based on the following image description, "
        f"write a {genre} story in a {style} writing style. "
        f"The story must be approximately {word_count} words long. "
        f"Do not reference the image description directly — immerse the reader in the story.\n\n"
        f"Image description:\n{caption}\n\n"
        f"Story:"
    )

    payload = {
        "model": TEXT_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": creativity,
            "num_predict": word_count * 6,  # rough token estimate (1 word ≈ 1.3 tokens)
        },
    }

    response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
    response.raise_for_status()
    return response.json().get("response", "").strip()


def generate_story(
    image_path: str,
    genre: str,
    style: str,
    word_count: int,
    creativity: float,
) -> str:
    """
    Main entry point called by the Gradio interface.
    1. Captions the image using a vision model.
    2. Generates a story from the caption using a text model.
    Returns the generated story string.
    """
    if image_path is None:
        return "Please upload an image to generate a story."

    try:
        # Step 1: Caption the image
        caption = get_image_caption(image_path)
    except requests.exceptions.ConnectionError:
        return (
            "Could not connect to Ollama. "
            "Make sure Ollama is running locally: https://ollama.com"
        )
    except Exception as e:
        return f"Error captioning image: {e}"

    try:
        # Step 2: Generate the story
        story = generate_story_text(caption, genre, style, word_count, creativity)
    except Exception as e:
        return f"Error generating story: {e}"

    return story
