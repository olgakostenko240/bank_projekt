from typing import Any, Generator

from tests.conftest import transaction


def filter_by_currency(transactions: Any, currency: Any) -> Any:
    """Функция принимает на фход список своварей и возвращает id операции"""
    if not transactions:
        yield "Отсутствуют заданные параметры"
    for transact in transactions:
        if transact["operationAmount"]["currency"]["code"] == currency:
            yield transact


def transaction_descriptions(transactions: Any) -> Generator[Any, Any, str]:
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    try:
        for trans in transactions:
            yield trans.get("description")
    except StopIteration:
        if not transactions:
            return "Нет транзакций"


def card_number_generator(start: Any, stop: Any) -> Generator[str, Any, None]:
    """Генератор номеров карт в заданом параметре"""
    for number in range(start, stop + 1):
        empty_str = "000000000000000"
        str_sum = empty_str + str(number)
        formatted_numbers = f"{str_sum[:4]} {str_sum[4:8]} {str_sum[8:12]} {str_sum[12:]}"
        yield formatted_numbers


    for numbers in card_number_generator(1, 5):
        print(numbers)


data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }]

if __name__ == "__main__":
    result = filter_by_currency(data, 'USD')
    print(result)