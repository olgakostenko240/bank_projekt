import os

import requests
from dotenv import load_dotenv

from src.utils import get_operations_data

load_dotenv()


def get_transaction_amount(transactions: dict) -> float:
    """Функция которая принимает на вход транзакцию и возвращает сумму транзакций"""
    amount = float(transactions["amount"])
    currency = transactions["currency"]

    if currency == "RUB":
        return amount

    elif currency != "RUB":

        apikey = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        headers = {"apikey": apikey}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return float(data["result"])

    else:
        raise ValueError(f"Неизвестная валюта {currency}.")


if __name__ == "__main__":
    data_transactions = get_operations_data(get_operations_data(file_path="../data/operations.json"))