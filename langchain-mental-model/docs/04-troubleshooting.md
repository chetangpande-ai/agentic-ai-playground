# Troubleshooting

## Missing API key

The script names the missing environment variable. Set it in `.env` or in your shell. Do not paste a real key into a Python file or commit `.env`.

## Missing model name or invalid model

Fill in the provider's model variable in `.env`. Model identifiers change; choose one currently available to your account and supported for the operation (for example, tool calling for agent examples).

## Missing Python package

Install the base dependencies from the workspace root:

```console
python -m pip install -r requirements.txt
```

For Layer 3, install `deepagents` separately in Python 3.11+:

```console
python -m pip install deepagents
```

## Provider-specific errors

- Confirm the key belongs to the provider selected by `MODEL_PROVIDER`.
- Check that the selected model is enabled for your account and supports the requested API.
- For agent examples, choose a model with tool-calling support.
- Check the provider's status page and current SDK documentation for API or rate-limit changes.

## Imports work in one command but not another

Activate the virtual environment before installing and running examples. Run scripts from this workspace root using the documented `python path/to/file.py` form.

## Weather output is not live

The shared `get_weather` tool intentionally returns sample data. It does not call a weather service.

## Raw API history seems to disappear

Chat Completions requests are stateless. Include all relevant prior messages in each request; the provider does not remember earlier calls automatically.
