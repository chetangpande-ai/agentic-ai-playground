"""Shows one raw Groq Chat Completions request (Layer 0); prints model text."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_name, require_package


def main() -> None:
    require_package("groq", "groq")
    key = api_key("groq")
    model = model_name("groq")
    from groq import Groq

    client = Groq(api_key=key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Explain a chat model in one sentence."}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
