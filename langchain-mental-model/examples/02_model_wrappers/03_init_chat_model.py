"""Shows init_chat_model factory selection (Layer 1); prints model-generated text."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_spec, provider_name, require_package


def main() -> None:
    provider = provider_name()
    require_package("langchain", "langchain")
    require_package(
        "langchain_openai" if provider == "openai" else "langchain_groq",
        "langchain-openai" if provider == "openai" else "langchain-groq",
    )
    api_key(provider)
    from langchain.chat_models import init_chat_model

    response = init_chat_model(model_spec()).invoke(
        "Explain a chat model in one sentence."
    )
    print(response.content)


if __name__ == "__main__":
    main()
