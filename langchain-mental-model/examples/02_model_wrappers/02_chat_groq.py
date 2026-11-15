"""Shows ChatGroq.invoke (Layer 1); prints content from a LangChain message."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_name, require_package


def main() -> None:
    require_package("langchain_groq", "langchain-groq")
    key = api_key("groq")
    model = model_name("groq")
    from langchain_groq import ChatGroq

    response = ChatGroq(model=model, api_key=key).invoke(
        "Explain a chat model in one sentence."
    )
    print(response.content)


if __name__ == "__main__":
    main()
