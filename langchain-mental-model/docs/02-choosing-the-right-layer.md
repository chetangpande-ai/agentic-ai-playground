# Choosing the right layer

Choose the lowest layer that provides the behavior you need. Lower layers expose more provider detail; upper layers manage more of the workflow.

| Need | Choose | Reason |
|---|---|---|
| See or control the provider request and response | Layer 0: provider SDK | You handle message serialization, history, and response fields directly |
| Make one model call using a LangChain interface | Layer 1: model wrapper | `.invoke()`, `.stream()`, and `.bind_tools()` use a common interface |
| Switch model/provider via configuration | Layer 1: `init_chat_model` | The factory resolves a `provider:model` string |
| Let a model decide when to call your tools | Layer 2: `create_agent` | It runs the model/tool loop |
| Add planning, filesystem context, and subagents for a longer task | Layer 3: `create_deep_agent` | The separate package supplies a fuller agent harness |

## Raw API or wrapper?

| Situation | Better starting point |
|---|---|
| No LangChain in the project | Raw provider SDK |
| Need direct access to provider-specific response details | Raw SDK, or provider-specific wrapper features |
| Want consistent message objects and invocation methods | A model wrapper |
| Want a model selected from environment/configuration | `init_chat_model` |
| Building a `create_agent` workflow | Either a wrapper object or a provider/model string |

## `create_agent` or `create_deep_agent`?

| Question | If yes |
|---|---|
| Is a model/tool loop enough? | Use `create_agent` |
| Does the task benefit from built-in planning, virtual files, or subagents? | Consider `create_deep_agent` |
| Is the task a single prompt and answer? | Stay at Layer 1 |
| Must the code run on Python 3.10? | Use Layers 0–2; current `deepagents` releases require Python 3.11+ |

Use the shared task examples in [05_same_task_all_layers](../examples/05_same_task_all_layers/README.md) to compare the same weather question across all four layers.
