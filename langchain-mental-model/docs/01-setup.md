# Setup

## Requirements

- Python 3.10 or newer for Layers 0–2.
- Python 3.11 or newer for the current `deepagents` package and Layer 3 examples.
- An API key and a model name supported by that provider.

The base `requirements.txt` pins LangChain, its OpenAI and Groq integrations, their provider SDKs, and `python-dotenv`. `deepagents` is separate and optional; current Deep Agents releases require Python 3.11+, so install it only in a compatible environment:

```console
python -m pip install deepagents
```

## Create an environment

Run these commands from `langchain-mental-model/`:

```console
python -m venv .venv
```

Activate it, then install the pinned base packages:

```console
python -m pip install -r requirements.txt
```

Windows PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS or Linux activation:

```console
source .venv/bin/activate
```

## Configure credentials

Copy `.env.example` to `.env`. Set the key and model variable for your provider. `MODEL_PROVIDER` selects `openai` or `groq` for examples that choose a provider dynamically. Model names are deliberately left blank: use a currently available model that supports the feature the example needs.

`ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL` are included as configuration placeholders, but this workspace does not install or demonstrate the Anthropic integration.

## Run a script

From the folder root, for example:

```console
python examples/01_raw_api/01_openai_chat_completions.py
python examples/02_model_wrappers/03_init_chat_model.py
python examples/03_create_agent/02_agent_with_tools.py
```

Each script loads `.env` from the workspace root. Existing shell environment variables take precedence. Layer 3 scripts use the same command form once `deepagents` is installed in a Python 3.11+ environment.
