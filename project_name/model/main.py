import logging

import typer


app = typer.Typer()
logger = logging.getLogger(__name__)


@app.command()
def train(ctx: typer.Context):
    """
    Perform model training.
    """
    logger.info("Training a new model.")


@app.command()
def predict(ctx: typer.Context):
    """
    Perform predictions.
    """
    _settings = ctx.parent.parent.settings
    logger.info("Predict results with %s.", _settings.artifacts.model)
