from typer.testing import CliRunner
from run import app
import typer


runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output
    assert "Show this message and exit." in result.output
