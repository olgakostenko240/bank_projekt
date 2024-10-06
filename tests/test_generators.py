from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction: list[dict[str, str | dict[str, Any] | int]]) -> None:
    result = filter_by_currency(transaction, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"


def test_transaction_descriptions(transaction: list[dict[str, str | dict[str, Any] | int]]) -> None:
    result = (transaction_descriptions(transaction))
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"
    assert next(result) == "Перевод организации"


@pytest.mark.parametrize("start, stop, expected", [(1, 1, "0000 0000 0000 0001")])
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    assert next(card_number_generator(start, stop)) == expected
