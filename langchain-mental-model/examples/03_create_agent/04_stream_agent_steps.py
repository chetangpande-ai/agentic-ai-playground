"""Streams model/tool steps (Layer 2); prints progress and sample weather output."""

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

    agent = create_agent(model=model_spec(), tools=[get_weather])
    for update in agent.stream(
        {"messages": [{"role": "user", "content": "What's the weather in Pune?"}]},
        stream_mode="updates",
    ):
        for node, state in update.items():
            print(f"\nStep: {node}")
            for message in state.get("messages", []):
                if getattr(message, "tool_calls", None):
                    print("Requested tools:", message.tool_calls)
                elif message.type == "tool":
                    print("Tool result:", message.content)
                elif message.type == "ai":
                    print("Final answer:", message.content)


if __name__ == "__main__":
    main()
