"""Shows create_agent calling a sample tool (Layer 2); prints a non-live weather answer."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_spec, provider_name, require_package
from examples.common.tools import get_weather


def main() -> None:
    provider = provider_name()
    require_package("langchain", "langchain")
    require_package(
        "langchain_openai" if provider == "openai" else "langchain_groq",
        "langchain-openai" if provider == "openai" else "langchain-groq",
    )
    api_key(provider)
    from langchain.agents import create_agent

    agent = create_agent(
        model=model_spec(),
        tools=[get_weather],
        system_prompt="Use the weather tool for weather questions. Say the result is sample data.",
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in Pune?"}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
