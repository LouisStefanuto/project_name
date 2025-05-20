import pytest
from typer.testing import CliRunner

from project_name.main import app

runner = CliRunner()


@pytest.mark.parametrize(
    "cmd,sub_cmd,expected_output",
    [
        ["data", "download", 0],
        ["data", "build", 0],
        ["data", "delete", 0],
        ["model", "train", 0],
        ["model", "predict", 0],
    ],
)
def test_app(cmd, sub_cmd, expected_output):
    result = runner.invoke(app, [cmd, sub_cmd])
    assert result.exit_code == expected_output
