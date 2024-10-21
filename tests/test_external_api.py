from unittest.mock import patch

from src.external_api import get_transaction_amount


@patch('requests.get')
def test_get_transaction_sum(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_transaction_amount(transaction) == 100

@patch('requests.get')
def test_get_transaction_sum_1(mock_get):
    transaction = {"amount": 50, "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 3800}
    assert get_transaction_amount(transaction) == 3800
