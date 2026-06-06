from config import app_config


def fetch_curr_access_count():
    """Use in-memory counter instead of MongoDB"""
    if app_config.openai_curr_access_count is None:
        app_config.openai_curr_access_count = 0


def increment_curr_access_count():
    """Increment in-memory counter"""
    if app_config.openai_curr_access_count is None:
        app_config.openai_curr_access_count = 0
    app_config.openai_curr_access_count += 1