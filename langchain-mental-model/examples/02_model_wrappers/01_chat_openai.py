"""Shows ChatOpenAI.invoke (Layer 1); prints content from a LangChain message."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_name, require_package


def main() -> None:
    require_package("langchain_openai", "langchain-openai")
    key = api_key("openai")
    model = model_name("openai")
    from langchain_openai import ChatOpenAI

    response = ChatOpenAI(model=model, api_key=key).invoke(
        "Explain a chat model in one sentence."
    )
    print(response.content)


if __name__ == "__main__":
    main()
