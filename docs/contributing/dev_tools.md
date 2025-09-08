# Dev tools

!!! note
    To contribute and develop on the project, we recommend using some useful dev tools, like Pre-commit.

## Pre-commit Hooks

The repo integrates [**Pre-commit**](https://pre-commit.com) to automate code quality checks every time you commit. Some of the hooks (checks) included:

>✅ [**Ruff**](https://docs.astral.sh/ruff/): Ultra-fast linter and formatter — replaces flake8, black, and isort.
>
>🔍 [**Mypy**](https://www.mypy-lang.org): Static type checker to validate type hints.
>
>🔒 **Detect secrets**: Prevents committing sensitive data like API keys.
>
>📄 **YAML and JSON checkers**: Ensure config files are valid and properly formatted.

To enable pre-commit hooks in your local repo:

```bash
git init             # need a git repo
uv sync --extra dev  # install dev dependencies
pre-commit install   # install the git hooks
```

Now, every time you git commit locally, the configured checks will run. To manually trigger them across all files:

```bash
pre-commit run --all-files
```
