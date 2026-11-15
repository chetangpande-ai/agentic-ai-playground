"""Shared environment and provider configuration for the runnable examples."""

import importlib.util
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROVIDER_VARIABLES = {
    "openai": ("OPENAI_API_KEY", "OPENAI_MODEL"),
    "groq": ("GROQ_API_KEY", "GROQ_MODEL"),
}


def require_package(module: str, distribution: str, optional: bool = False) -> None:
    """Raise an install hint before importing a required or optional package."""
    if importlib.util.find_spec(module) is None:
        hint = f"python -m pip install {distribution}"
        if optional:
            hint += " (Python 3.11+ required)"
        raise RuntimeError(f"Missing package '{distribution}'. Install it with: {hint}")


def load_environment() -> None:
    """Load this workspace's .env while preserving existing shell variables."""
    require_package("dotenv", "python-dotenv")
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env", override=False)


def provider_name() -> str:
    """Return the configured supported model provider."""
    load_environment()
    provider = os.getenv("MODEL_PROVIDER", "openai").strip().lower()
    if provider not in PROVIDER_VARIABLES:
        choices = ", ".join(PROVIDER_VARIABLES)
        raise ValueError(f"MODEL_PROVIDER must be one of: {choices}")
    return provider


def api_key(provider: str | None = None) -> str:
    """Return a configured provider API key or explain which variable is missing."""
    load_environment()
    selected = provider or provider_name()
    if selected not in PROVIDER_VARIABLES:
        raise ValueError(f"Unsupported provider '{selected}'")
    key_variable, _ = PROVIDER_VARIABLES[selected]
    value = os.getenv(key_variable, "").strip()
    if not value:
        raise ValueError(f"Set {key_variable} in .env or your shell environment.")
    return value


def model_name(provider: str | None = None) -> str:
    """Return the configured model name for a provider."""
    load_environment()
    selected = provider or provider_name()
    if selected not in PROVIDER_VARIABLES:
        raise ValueError(f"Unsupported provider '{selected}'")
    _, model_variable = PROVIDER_VARIABLES[selected]
    value = os.getenv(model_variable, "").strip()
    if not value:
        raise ValueError(f"Set {model_variable} in .env or your shell environment.")
    return value


def model_spec(provider: str | None = None) -> str:
    """Return the LangChain provider:model identifier for the selected provider."""
    selected = provider or provider_name()
    return f"{selected}:{model_name(selected)}"
