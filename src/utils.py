import json
from typing import Any


def get_operations_data(transaction: Any) -> list:
    """Функция которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""
    empty_data: list = []
    try:
        with open(transaction, encoding="UTF-8") as file:
            try:
                operation_data = json.load(file)
            except json.JSONDecodeError:
                print("Ошибка декорирования JSON-файла")
                return empty_data
    except FileNotFoundError:
        print("Ошибка! Файл не найден")
        return empty_data
    return operation_data


list_of_dict = get_operations_data("../data/operations.json")
