"""Inspects AIMessage fields (Layer 1); prints content, usage metadata, and tool calls."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_name, provider_name, require_package
from examples.common.tools import add_numbers


def main() -> None:
    provider = provider_name()
    package, distribution = (
        ("langchain_openai", "langchain-openai")
        if provider == "openai"
        else ("langchain_groq", "langchain-groq")
    )
    require_package(package, distribution)
    key = api_key(provider)
    model = model_name(provider)

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        chat = ChatOpenAI(model=model, api_key=key)
    else:
        from langchain_groq import ChatGroq

        chat = ChatGroq(model=model, api_key=key)
    message = chat.bind_tools([add_numbers]).invoke(
        "Use add_numbers to calculate 19 plus 23."
    )
    print("content:", message.content)
    print("usage_metadata:", message.usage_metadata)
    print("tool_calls:", message.tool_calls)


if __name__ == "__main__":
    main()
