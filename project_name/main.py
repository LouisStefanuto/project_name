import typer
from loguru import logger

from project_name.config import settings
from project_name.data import main as data
from project_name.model import main as model

app = typer.Typer(no_args_is_help=True)


@app.callback()
def cli(ctx: typer.Context, verbose: bool = False):
    """
    Run all datascience commands.
    """
    # This will make available to all downstream commands the loaded configuration
    ctx.settings = settings

    if verbose:
        logger.setLevel("DEBUG")


@app.command()
def run(ctx: typer.Context):
    """
    Run cmd line entry point, e.g. useful to start pipelines.
    """
    logger.info("Current configuration: %s", dict(ctx.parent.settings))
    # This should print something like:
    # 2023-03-17 15:23:08,056 __main__ - INFO: Current configuration: {
    #     "SECRET_KEY": "random_string",
    #     "PORT": 5050,
    #     "USERNAME": "username",
    #     "ROOT_DATA_PATH": "data",
    #     "MODEL": "models\\dev_model.h5"
    # }


app.add_typer(data.app, name="data", help="Manages data flow.")
app.add_typer(model.app, name="model", help="Manages model training and predictions.")


if __name__ == "__main__":
    app()
