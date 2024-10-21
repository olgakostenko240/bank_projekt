import json
from typing import Any


def get_operations_data(file_path: Any) -> list:
    """Функция которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""
    empty_data: list = []
    try:
        with open(file_path, encoding="UTF-8") as file:
            try:
                operation_data: Any = json.load(file)
            except json.JSONDecodeError:
                print("Ошибка декорирования JSON-файла")
                return empty_data
    except FileNotFoundError:
        print("Ошибка! Файл не найден")
        return empty_data
    return operation_data


if __name__ == "__main__":
    data_operations = get_operations_data("../data/operations.json")
