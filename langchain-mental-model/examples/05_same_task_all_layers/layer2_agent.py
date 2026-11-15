"""Uses create_agent and a tool (Layer 2); prints a sample-weather answer."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_spec, provider_name, require_package
from examples.common.tools import get_weather
from task import WEATHER_QUESTION


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
        system_prompt="Use the weather tool and identify its result as sample data.",
    )
    result = agent.invoke({"messages": [{"role": "user", "content": WEATHER_QUESTION}]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
