import os
from typing import Any

from config import PATH_HOME
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.regular_exspressions import search_list_of_dict
from src.tables import read_cvs, read_excel
from src.utils import get_operations_data
from src.widget import get_data, mask_account_card

# Путь до JSON-файла
path_to_file = os.path.join(PATH_HOME, "data", "operations.json")

# Путь до CSV-файла
path_to_file_1 = os.path.join(PATH_HOME, "data", "transactions.csv")

# Путь до XLSX-файла
path_to_file_2 = os.path.join(PATH_HOME, "data", "transactions_excel.xlsx")


def filter_transaction(transaction_list: Any, cur: Any) -> list:
    """Функция принимает на фход словарь из CSV и XLSX файлов возвращает заданные транзакции"""
    new_list = []
    for transact_list in transaction_list:
        if transact_list["currency_code"] == cur:
            new_list.append(transact_list)
    return new_list


def main() -> str:
    """Функция отвечающая за основную логику проекта"""

    user_input_1 = input(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Пользователь: """
    )
    if user_input_1 == "1":
        print("Для обработки выбран JSON-файл.")
        transaction = get_operations_data(path_to_file)
    elif user_input_1 == "2":
        print("Для обработки выбран CSV-файл.")
        transaction = read_cvs(path_to_file_1)
    elif user_input_1 == "3":
        print("Для обработки выбран XLSX-файл.")
        transaction = read_excel(path_to_file_2)

    status_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING """
        ).upper()
        if status not in status_list:
            print(f'Статус операции "{status}" не доступен.')
        else:
            break
    filtered_transaction = filter_by_state(transaction, status)

    sort = input("Отсортировать операции по дате? Да/Нет ").lower()
    if sort == "да":
        if input("Отсортировать по возрастанию или по убыванию? ").lower() == "по возрастанию":
            date_flag = False
        else:
            date_flag = True
        filtered_transaction = sort_by_date(filtered_transaction, date_flag)

    print_rub = input("Выводить только рублевые транзакции? Да/Нет ").lower()
    if print_rub == "да":
        if user_input_1 == "1":
            rub_transaction = filter_by_currency(filtered_transaction, "RUB")
            filtered_transaction = list(rub_transaction)
            print(filtered_transaction)
        elif user_input_1 == "2" or user_input_1 == "3":
            filtered_transaction = filter_transaction(filtered_transaction, "RUB")

    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").lower()
    if filter_by_word == "да":
        word = input("Введите слово: ")
        filtered_transaction = search_list_of_dict(filtered_transaction, word)

    print("Распечатываю итоговый список транзакций...")
    if len(filtered_transaction) == 0:
        return "Не найденно ни одной транзакции, подходящей под ваши условия фильтрации."
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transaction)}")
        for i in filtered_transaction:
            if user_input_1 == "1":
                currency = i["operationAmount"]["currency"]["name"]
                i_date = get_data(i["date"])
                if i["description"] == "Открытие вклада":
                    from_to = mask_account_card(i["to"])
                else:
                    from_to = mask_account_card(i["from"]) + " -> " + mask_account_card(i["to"])
                amount = i["operationAmount"]["amount"]
                print(f"{i_date} {i["description"]}\n{from_to}\nСумма: {round(float(amount))} {currency}")
            elif user_input_1 == "2" or user_input_1 == "3":
                currency = i["currency_code"]
                i_date = get_data(i["date"])
                if i["description"] == "Открытие вклада":
                    from_to = mask_account_card(i["to"])
                else:
                    from_to = mask_account_card(i["from"]) + " -> " + mask_account_card(i["to"])
                amount = i["amount"]
                print(f"{i_date} {i["description"]}\n{from_to}\nСумма: {round(float(amount))} {currency}")


if __name__ == "__main__":
    print(main())
