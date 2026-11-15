"""Shows one raw OpenAI Chat Completions request (Layer 0); prints model text."""

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
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Explain a chat model in one sentence."}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
