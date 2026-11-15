"""Small deterministic tools shared by agent examples; weather is sample data."""


def get_weather(city: str) -> str:
    """Return sample weather data for a city, not a live forecast."""
    if city.strip().lower() == "pune":
        return "Sample data: Pune is sunny and 28 C."
    return f"Sample data: weather for {city} is unavailable."


def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
