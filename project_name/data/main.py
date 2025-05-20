import logging

import typer

app = typer.Typer()
logger = logging.getLogger(__name__)


@app.command()
def download(ctx: typer.Context):
    """
    Download data from somewhere in the cloud.
    """
    _settings = ctx.parent.parent.settings
    logger.info("Downloading data from somwhere with user: %s.", _settings.username)


@app.command()
def build(ctx: typer.Context):
    """
    Build a dataset based on downloaded data that is useful for the model.
    """
    _settings = ctx.parent.parent.settings
    logger.info(
        "Building a marvelous dataset from raw data: %s.", _settings.artifacts.raw_data
    )


@app.command()
def delete(ctx: typer.Context):
    """
    Delete a dataset.
    """
    logger.warning("This dataset will be deleted")
