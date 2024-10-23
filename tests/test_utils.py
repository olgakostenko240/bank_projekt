from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_operations_data


@patch("builtins.open", new_callable=mock_open, read_data='{"transaction_id": 1}')
def test_get_operations_data(mock_file: Any) -> None:
    transactions = get_operations_data("test.json")
    assert transactions == {"transaction_id": 1}


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: Any) -> None:
    transactions = get_operations_data("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file: Any) -> None:
    transactions = get_operations_data("data/operations.json")
    assert transactions == []

