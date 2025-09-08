import datetime
import os
from pathlib import Path
from typing import Union

from pydantic import BaseModel, Field, computed_field
from pydantic.dataclasses import dataclass
from pydantic_settings import BaseSettings, SettingsConfigDict


@dataclass
class BaseTree:
    """
    Basic directory structure can be specified here.

    The defined path are relative to the project root defined below.
    This tree structure is supposed to not move too much.
    """

    # Describes where data files are stored
    data: Path = Path("data")

    # Path can then be built combining different paths sub sections
    raw: Path = data / "raw"
    interim: Path = data / "interim"
    processed: Path = data / "processed"

    # Describes where model files are stored
    model: Path = Path("models")


class ArtifactMgr(BaseModel):
    """
    Handles data and model storage locations

    The goal is to reference here the location and naming of all
    files that are required by the packaged code.
    """

    root: Path
    creation_date: str = datetime.datetime.now().strftime("%Y%m%d")

    @computed_field  # type: ignore[misc]
    @property
    def raw_data(self) -> Path:
        return self.root / BaseTree.data / "input_data.csv"

    @computed_field  # type: ignore[misc]
    @property
    def model(self) -> Path:
        """
        For example, one can timestamp created filenames with the drawback
        that if you need to rerun the process on an other day could lead to issues.

        This means that creation_date might need to be overwritten.
        """
        return self.root / BaseTree.model / f"{self.creation_date}_model.h5"


class CatBoostHP(BaseSettings):
    """
    Handles some CatBoost model hyperparameters (as an example)
    """

    verbose: bool = False
    depth: int = 5
    iterations: int = 1000
    early_stopping_rounds: int = 50
    grow_policy: str = "Depthwise"


class Base(BaseSettings):
    """
    Base class to store all the project configs.

    This class will be overloaded by a specific class per environment.
    We define here environment independant config variables
    """

    secret_key: str = Field(
        "random_string", json_schema_extra={"env": "ANOTHER_SECRET_KEY"}
    )
    port: int = 5050
    username: str = "basic_username"

    artifacts: ArtifactMgr = ArtifactMgr(
        root=(
            Path(__file__).parent.resolve() if ("__file__" in locals()) else Path.cwd()
        )
    )
    model: CatBoostHP = CatBoostHP()

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


class Dev(Base):
    """
    Development environment settings.
    """

    username: str = "dev_username"

    model_config = SettingsConfigDict(env_file=".dev.env", env_file_encoding="utf-8")


class Prod(Base):
    """
    Production environment settings.
    """

    username: str = "prod_username"

    model_config = SettingsConfigDict(env_file=".prod.env", env_file_encoding="utf-8")


config = dict(dev=Dev, prod=Prod)
# Here the default values can be overloaded by local environment files.
# By default, it is considered that we are in `dev` environment,
# so dev configuration is loaded in settings.
# To select the environment explicitly you could:
# ENV=dev poetry run python -m project_slug.main --help ...
settings: Union[Dev, Prod] = config[os.environ.get("ENV", "dev").lower()]()


if __name__ == "__main__":
    print("# Only for demo purposes")
    print("Instanciate a basic conf: cfg = Base()")
    cfg = Base()
    print("This is this config's username:")
    print(cfg.username)
    print("\n")
    print("# All path elements are accessible from the artifacts object")
    print("Typing: cfg.artifacts.raw_data")
    print(cfg.artifacts.raw_data)
    print("\n")
    print("Typing: cfg.artifacts.model")
    print(cfg.artifacts.model)
    print("\n")
    print("# Your model hyperparameters are all accessible in a")
    print("# properly defined dict, typing: cfg.model.model_dump()")
    print(cfg.model.model_dump())
    print("\n")
    print("# They can be used to instanciate a model directly:")
    print("# model = CatBoostClassifier(**cfg.model.model_dump())")
    print("\n")
    cfg_prd = Prod()
    print("# Instanciate a basic conf: cfg = Prod()")
    print("# The only difference here is that we changed the username")
    print("# Typing cfg_prd.username: ")
    print(cfg_prd.username)
    print("\n")
    print("# This shows default behaviour")
    print("# Strength come frome the fact that having a configuration")
    print("# file called .env, .dev.env or .prod.env will overwrite")
    print("# the different config class attributes")
    print("\n")
    print("# Everybody knows what is expected but can tune it to its own")
    print("# local situation")
    print("\n")
    print(
        "# This is then called in the typer callback and accessible in the whole package."
    )
