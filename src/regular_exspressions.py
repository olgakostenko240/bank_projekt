import re
from collections import Counter
from typing import Any


def search_list_of_dict(list_filter: Any, search_string: Any) -> list:
    """Функция принимает список словарей и страку для поиска, возвращает список словарей с данной строкой"""
    new_list_filter = []
    pattern = f"{search_string}"
    for operations in list_filter:
        if re.findall(pattern, operations["description"], flags=re.IGNORECASE):
            new_list_filter.append(operations)
    return new_list_filter


def count_categories(operations: Any) -> Counter:
    """Функция принимает список словарей и категории операций, возвращает количество операций"""
    category_transaction = []
    for operation in operations:
        category = operation["description"]
        category_transaction.append(category)
    counted = Counter(category_transaction)
    return counted


data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
]


if __name__ == "__main__":
    result = search_list_of_dict(data, "Перевод организации")
    print(result)

if __name__ == "__main__":
    resul = count_categories(data)
    print(resul)
