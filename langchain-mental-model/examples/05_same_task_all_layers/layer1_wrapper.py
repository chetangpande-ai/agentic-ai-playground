"""Uses a model wrapper (Layer 1); prints an answer based on provided sample weather."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_spec, provider_name, require_package
from task import WEATHER_CONTEXT, WEATHER_QUESTION


def main() -> None:
    provider = provider_name()
    require_package("langchain", "langchain")
    require_package(
        "langchain_openai" if provider == "openai" else "langchain_groq",
        "langchain-openai" if provider == "openai" else "langchain-groq",
    )
    api_key(provider)
    from langchain.chat_models import init_chat_model

    response = init_chat_model(model_spec()).invoke([
        ("system", WEATHER_CONTEXT),
        ("human", WEATHER_QUESTION),
    ])
    print(response.content)


if __name__ == "__main__":
    main()
