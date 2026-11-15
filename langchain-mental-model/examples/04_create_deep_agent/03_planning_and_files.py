"""Shows planning and virtual files (Layer 3); prints tool names and the final reply."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_spec, provider_name, require_package


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

    agent = create_deep_agent(model=model_spec())
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": (
                "Make a two-step plan, then use your virtual filesystem to write "
                "a one-sentence note to /learning-note.txt. Tell me when it is done."
            ),
        }]
    })
    for message in result["messages"]:
        for call in getattr(message, "tool_calls", []):
            print("Built-in tool:", call["name"])
    print("Final response:", result["messages"][-1].content)


if __name__ == "__main__":
    main()
