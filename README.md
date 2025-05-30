# project_name

Template to build industrialized data science projets.

## Install

Create a virtual environment:

```bash
uv venv .venv --python 3.12  # or any version of python >=3.10
source .venv/bin/activate
uv sync
```

`project_name` is now installed as a package and as a command line tool. If you also want the optional dev and docs dependencies:

```bash
uv sync --extra dev --extra docs
```

## Run the project

The recommended way to run the code of this project is via CLI.:

```console
uv run project-name --help
```

which should return the list of the available commands:

```text
 Usage: project-name [OPTIONS] COMMAND [ARGS]...

 Run all datascience commands.

╭─ Commands ──────────────────────────────────────────────────╮
│ data     Manages data flow.                                 │
│ model    Manages model training and predictions.            │
╰─────────────────────────────────────────────────────────────╯
```

## Documentation

To preview your documentation in real-time while editing, run:

```console
uv sync --extra docs
mkdocs serve
```

Learn about serving the documentation, adding pages and deploying [here](./docs/contributing/documentation.md).

## Project tree

The project follows the tree structure described bellow :

```text
.
├── app                  # Entrypoints (fastapi)
├── data                 # Datasets
├── docs                 # Mkdocs
├── models               # Model checkpoints
├── notebooks            # Experiment notebooks or code examples
├── project_name         # Your package
│   ├── data                 # Data loading logic
│   ├── model                # Model logic
│   ├── config.py            # Pydantic config loading
│   ├── main.py
│   └── ...
├── scripts              # Utility shell scripts (build img docker ...)
├── tests                # Unit tests. Should follow the structure of the package.
├── Dockerfile           # Container definition
├── Makefile             # Useful commands
├── mkdocs.yml           # Config for mkdocs
├── pyproject.toml       # UV package and dev tools config
└── README.md
```

## Configuration Management

To change configuration sources between dev and prod modes, set the environment variable `ENV=dev` or `ENV=prod`.

## Acknowledgments

This project is based on the Python CookieCutter template created by Capgemini Invent.
