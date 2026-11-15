"""Uses the raw SDK (Layer 0); prints an answer based on provided sample weather."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from examples.common.config import api_key, model_name, require_package
from task import WEATHER_CONTEXT, WEATHER_QUESTION


def main() -> None:
    require_package("openai", "openai")
    key = api_key("openai")
    model = model_name("openai")
    from openai import OpenAI

    response = OpenAI(api_key=key).chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": WEATHER_CONTEXT},
            {"role": "user", "content": WEATHER_QUESTION},
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
