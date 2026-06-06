---
title: Picture to Story Generator
emoji: 📖
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 3.46.0
app_file: app.py
pinned: false
license: mit
---

# The Storyteller
***A Local LLM-Based App to Generate Stories from Pictures***

> This application runs entirely locally using [Ollama](https://ollama.com). It uses a vision-capable model (`llava`) to generate a vivid description of an uploaded image, then passes that description to a text model (`llama3`) to craft an engaging story in your chosen genre and writing style — no API keys or internet connection required after setup.

## App Flow

1. **Image → Caption** — The image is encoded and sent to `llava` (via Ollama) which generates a detailed description covering subjects, setting, mood, and colors.
2. **Caption → Story** — The caption is used to construct a prompt that is passed to `llama3`, which produces a story matching your selected genre, writing style, length, and creativity level.

## Prerequisites

- [Ollama](https://ollama.com) installed and running locally (`http://localhost:11434`)
- The required models pulled:
  ```bash
  ollama pull llava
  ollama pull llama3
  ```

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## App Details

- The app runs locally — performance depends on your hardware.
- Dark mode is enabled by default. Use the **Dark Mode** toggle to switch to light mode.
- Story length is capped at **200 words per request**.
- If Ollama is not running, the app will return a connection error with a link to the Ollama setup page.

## Controls

| Control | Description |
|--------|-------------|
| **Dark Mode Toggle** | Switches between dark and light mode. Dark mode is on by default. |
| **Image Selector** | Upload an image from your computer or drag and drop. Click `X` to clear and reset. |
| **Story Genre** | Choose from 14 genres: Adventure, Children Literature, Comedy, Drama, Fantasy, Fiction, Horror, Mystery, Non-fiction, Poetry, Romance, Satire, Surrealism, Urban Fantasy. |
| **Story Writing Style** | Choose from 17 styles including Cinematic, Narrative, Symbolic, Experimental, Stream of Consciousness, and more. |
| **Story Length Slider** | Set word count between 30 and 200 words (step: 10). |
| **Creativity Index Slider** | Controls generation temperature (0.3–1.0). Range 0.5–0.7 recommended; 1.0 gives highly creative and sometimes surprising output. |
| **Generate Story Button** | Starts the captioning + story generation pipeline. |
| **Clear Button** | Resets image, sliders, and story output to defaults. |
| **Story Text Area** | Displays the generated story. |
| **Examples Section** | Click "Expand for examples" to load a pre-configured example. Selecting one auto-fills all inputs — no image upload needed. |

## Built-in Examples

Five themed examples are included under `assets/examples/`:

| File | Theme | Genre | Style | Words | Creativity |
|------|-------|-------|-------|-------|------------|
| `nature-wolf.jpg` | Nature & Wildlife | Poetry | Symbolic | 80 | 0.8 |
| `emotions-portrait.jpg` | People & Emotions | Fiction | Cinematic | 100 | 0.7 |
| `fantasy-forest.jpg` | Fantasy & Mystical | Surrealism | Non-linear | 120 | 1.0 |
| `city-night.jpg` | Urban & City Life | Horror | Narrative | 90 | 0.6 |
| `adventure-mountain.jpg` | Adventure & Travel | Children Literature | Experimental | 70 | 0.9 |

## Project Structure

```
The Storyteller Webapp/
├── app.py            # Gradio UI and event wiring
├── model.py          # Ollama vision + text pipeline
├── config.py         # App settings, genre/style lists, theme
├── mongo_utils.py    # In-memory access counter (MongoDB removed)
├── style.css         # Button styles and footer visibility
├── requirements.txt  # Python dependencies
└── assets/
    └── examples/     # Example images for the Examples section
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | [Gradio](https://gradio.app) 3.45 with Dracula Revamped theme |
| Vision (Image → Caption) | `llava` via Ollama |
| Text (Caption → Story) | `llama3` via Ollama |
| Image processing | Pillow |
| HTTP client | requests |

## Project Source
[👉 Visit GitHub Repo](https://github.com/AADHYA-A/Picture-to-Story-Generator)
