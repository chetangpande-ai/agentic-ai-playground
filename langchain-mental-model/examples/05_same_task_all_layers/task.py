"""Shares the Layer 0–3 weather task; prints the same prompt used by each layer."""

WEATHER_QUESTION = "What's the weather in Pune?"
WEATHER_CONTEXT = "Sample data only: Pune is sunny and 28 C."


def main() -> None:
    """Print the shared question for quick inspection."""
    print(WEATHER_QUESTION)


if __name__ == "__main__":
    main()
