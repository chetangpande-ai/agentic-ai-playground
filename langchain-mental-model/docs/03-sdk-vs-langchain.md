# Provider SDK vs. LangChain

Provider SDKs and LangChain model wrappers both send model requests. The wrapper gives application code a shared interface; it does not remove the provider SDK or make every provider feature identical.

| LangChain integration | Package | Provider SDK |
|---|---|---|
| `ChatOpenAI` | `langchain-openai` | `openai` |
| `ChatGroq` | `langchain-groq` | `groq` |

When calling `model.invoke(...)`, a provider integration typically:

1. Converts LangChain messages and options to the provider's request format.
2. Calls the provider SDK.
3. Converts the response to a LangChain message object, exposing content and supported metadata such as token usage or tool calls.

## What the wrapper adds

- A common model API such as `.invoke()`, `.stream()`, and `.bind_tools()`.
- LangChain message types, which work with agents and other LangChain components.
- Integration with LangChain's tool-calling and streaming patterns.

## What it does not promise

- Identical provider features, request parameters, or response metadata.
- Support for a provider's new feature before its integration exposes it.
- That the integration always uses a specific endpoint. Check current provider docs; an integration can use another endpoint when appropriate.

For direct wire-level control, use the provider SDK. For a common model interface and LangChain composition, use its provider integration. `init_chat_model` is a factory over those integrations, not a separate model API.

Official references: [ChatOpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai), [ChatGroq](https://docs.langchain.com/oss/python/integrations/chat/groq), and [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model).
