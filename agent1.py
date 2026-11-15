#deepseek/deepseek-v4.1-flash-1017

from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openrouter:deepseek/deepseek-v4.1-flash-1017",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)


result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?, multipy 22*4"}]}
)
print(result["messages"][-1].content_blocks)


