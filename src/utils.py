import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations_data(transaction: Any) -> list:
    """Функция которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""
    empty_data: list = []
    try:
        with open(transaction, encoding="UTF-8") as file:
            try:
                logger.info("Получение данных из файла.")
                operation_data = json.load(file)
            except json.JSONDecodeError:
                logger.error("Ошибка декорирования JSON-файла.")
                print("Ошибка декорирования JSON-файла")
                return empty_data
    except FileNotFoundError:
        logger.error("Ошибка! Файл не найден.")
        print("Ошибка! Файл не найден")
        return empty_data
    return operation_data


if __name__ == "__main__":
    list_of_dict = get_operations_data(os.path.abspath("../data/operations.json"))
    print(list_of_dict)
