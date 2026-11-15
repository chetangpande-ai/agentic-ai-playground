"""Uses create_deep_agent (Layer 3); prints an answer from the sample weather tool."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_spec, provider_name, require_package
from examples.common.tools import get_weather
from task import WEATHER_QUESTION


def main() -> None:
    if sys.version_info < (3, 11):
        raise RuntimeError("The current deepagents package requires Python 3.11 or newer.")
    require_package("deepagents", "deepagents", optional=True)
    provider = provider_name()
    require_package(
        "langchain_openai" if provider == "openai" else "langchain_groq",
        "langchain-openai" if provider == "openai" else "langchain-groq",
    )
    api_key(provider)
    from deepagents import create_deep_agent

    agent = create_deep_agent(
        model=model_spec(),
        tools=[get_weather],
        system_prompt="Use the weather tool and identify its result as sample data.",
    )
    result = agent.invoke({"messages": [{"role": "user", "content": WEATHER_QUESTION}]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
