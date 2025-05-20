# Running unit tests

## Pytest

Install the dev dependencies:

```bash
source .venv/bin/activate
uv sync --extra dev
```

Run unit tests:

```bash
pytest
```

## Coverage

Coverage is automatically assessed. By default coverage is computed both on the `app` and `project_name` folders. Unit tests are configured in the `pyproject.toml` file.
