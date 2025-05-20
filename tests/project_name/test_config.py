from pathlib import Path, PurePath

from project_name import config


def test_data_path_default():
    base_tree = config.BaseTree()

    assert base_tree.data == PurePath("data")
    assert base_tree.raw == PurePath("data/raw")
    assert base_tree.interim == PurePath("data/interim")
    assert base_tree.processed == PurePath("data/processed")


def test_base_config():
    _settings = config.Base()

    assert _settings.secret_key == "random_string"
    assert _settings.port == 5050
    assert _settings.username == "basic_username"

    assert isinstance(_settings.artifacts, config.ArtifactMgr)
    assert isinstance(_settings.artifacts.creation_date, str)

    path_project = Path("../project_name").resolve()
    assert _settings.artifacts.root == path_project

    assert _settings.model == config.CatBoostHP(
        verbose=False,
        depth=5,
        iterations=1000,
        early_stopping_rounds=50,
        grow_policy="Depthwise",
    )

    artifacts = Path(*_settings.artifacts.raw_data.parts[-2:])
    assert artifacts == PurePath("data/input_data.csv")
