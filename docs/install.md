# Installation

## Quick install

The easiest way to install project_name is to use the Makefile commands. It will install the package with all its optional dependencies:

```bash
make create-environment
source .venv/bin/activate
make install-requirements
```

The project is now installed as a package and as a command line tool.

## Manual install

Create a virtual environment:

```bash
uv venv .venv --python 3.12  # or any version of python >=3.10
source .venv/bin/activate
uv sync
```

The project is now installed as a package and as a command line tool. If you also want the optional dev and docs dependencies:

```bash
uv sync --extra dev --extra docs
```

## Install on machines without internet connection

On a machine WITH internet connection:

```bash
uv build
uv export --format requirements-txt --output-file dist/requirements.txt
sed -i -e '/^-e ./d' dist/requirements.txt` (remove artifact
uv run pip download -r dist/requirements.txt -d dist/wheels
```

This will download all wheels in the `dist/wheels` directory.

Next, transfer the wheel files to the machine without connection (network, hard drive, ...). Make sure the target machine already has Python installed. Then install the wheels:

```bash
pip install uv -f dist/wheels --no-index
pip install * -f dist/wheels --no-index
```

## Create a jupyter kernel with the virtual environment

Activate the virtual environment and add [**ipykernel**](https://pypi.org/project/ipykernel/) as a dev dependency:

```bash
source .venv/bin/activate
uv add ipykernel --optional dev
```

!!! warning
    **The kernel might not be available immediately in VScode interface.** Try restarting VScode if you have trouble finding the right kernel.
