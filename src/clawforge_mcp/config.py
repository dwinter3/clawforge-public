"""Configuration for ClawForge MCP Server."""

import json
import os
from pathlib import Path

API_URL = os.environ.get("CLAWFORGE_API_URL", "https://api.clawforge.dev")

# API key can come from env var or persisted config
API_KEY = os.environ.get("CLAWFORGE_API_KEY", "")

# Config file for persisting API key across sessions
CONFIG_DIR = Path(os.environ.get("CLAWFORGE_CONFIG_DIR", os.path.expanduser("~/.clawforge")))
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config() -> dict:
    """Load persisted config from ~/.clawforge/config.json."""
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_config(config: dict) -> None:
    """Save config to ~/.clawforge/config.json."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(config, indent=2))


def get_api_key() -> str:
    """Get API key from env var or persisted config."""
    if API_KEY:
        return API_KEY
    config = load_config()
    return config.get("api_key", "")


def get_agent_id() -> str:
    """Get agent ID from persisted config."""
    config = load_config()
    return config.get("agent_id", "")
