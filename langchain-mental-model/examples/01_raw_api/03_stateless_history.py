"""Shows stateless Chat Completions history (Layer 0); prints the recalled word."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_name, require_package


def main() -> None:
    require_package("openai", "openai")
    key = api_key("openai")
    model = model_name("openai")
    from openai import OpenAI

    client = OpenAI(api_key=key)
    history: list[dict[str, str]] = [
        {"role": "user", "content": "Remember this demo word: cedar."}
    ]
    first = client.chat.completions.create(model=model, messages=history)
    first_answer = first.choices[0].message.content or ""
    history.append({"role": "assistant", "content": first_answer})
    history.append({"role": "user", "content": "What demo word did I give you?"})
    second = client.chat.completions.create(model=model, messages=history)
    print(second.choices[0].message.content)


if __name__ == "__main__":
    main()
