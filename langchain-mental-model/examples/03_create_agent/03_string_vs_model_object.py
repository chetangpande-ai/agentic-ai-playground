"""Compares model input forms (Layer 2); prints a response from each agent."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import (
    api_key,
    model_name,
    model_spec,
    provider_name,
    require_package,
)


def main() -> None:
    provider = provider_name()
    require_package("langchain", "langchain")
    require_package(
        "langchain_openai" if provider == "openai" else "langchain_groq",
        "langchain-openai" if provider == "openai" else "langchain-groq",
    )
    key = api_key(provider)
    from langchain.agents import create_agent

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        model_object = ChatOpenAI(model=model_name(provider), api_key=key)
    else:
        from langchain_groq import ChatGroq

        model_object = ChatGroq(model=model_name(provider), api_key=key)

    prompt = {"messages": [{"role": "user", "content": "Say hello briefly."}]}
    string_agent = create_agent(model=model_spec(), tools=[])
    object_agent = create_agent(model=model_object, tools=[])
    print("String model:", string_agent.invoke(prompt)["messages"][-1].content)
    print("Model object:", object_agent.invoke(prompt)["messages"][-1].content)


if __name__ == "__main__":
    main()
