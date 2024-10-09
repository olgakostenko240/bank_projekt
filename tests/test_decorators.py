from typing import Any
import pytest
from _pytest.capture import CaptureFixture
from src.decorators import log


def test_log_1() -> None:
    @log(filename="")
    def my_function(x: int, y: int) -> Any:
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_2(capsys: CaptureFixture[str]) -> None:
    @log(filename="")
    def my_function(x: int, y: int) -> Any:
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
    assert result == 3


@log(filename="mylog.txt")
def test_function_error() -> None:
    raise ValueError("Test error")
