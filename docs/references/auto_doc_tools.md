
# Auto documentation

!!! note
    There are many tools available for **automatically generating documentation** from your Python code. This guide focuses on a few tools to document **the package, the CLI or single functions/classes**.

## Auto document a full package

By default, the documentation for your Python code is generated using MkDocs along with related plugins (ex. `mkdocstrings[python]`). The **API Reference** section presents the code structure, mirroring your project's directory tree.

## Auto document a full cli

If your CLI is properly documented, you can use Typer's auto-documentation tool to generate a Markdown file that summarizes all available commands:

```bash
typer project_name/main.py utils docs --output docs/references/cli_api_reference.md
```

We recommend adding this command to your CLI to update the CLI Reference section automatically.

## Auto document a single function or class

You can document specific classes and functions automatically if your docstrings are square and clean. For instance,
if you want to describe your production configuration in your documentation, typing something like:

```text
::: project_name.config.Prod
```

would yield the following result:

___

::: project_name.config.Prod
