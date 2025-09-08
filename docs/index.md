# project_name

!!! note "What is project_name?"
    Template to build industrialized data science projets.

## Example

The recommended way to run the code of this project is via CLI:

```bash
project-name --help
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

## Project tree

The project follows the tree structure described below :

```text
.
├── app                  # Entrypoints (FastAPI)
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

## Acknowledgments

This project is based on the Python CookieCutter template created by Capgemini Invent.
