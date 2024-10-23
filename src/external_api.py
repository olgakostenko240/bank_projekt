import os

import requests
from dotenv import load_dotenv


load_dotenv()


def get_transaction_amount(transactions: dict) -> list[str] | float:
    """Функция которая принимает на вход транзакцию и возвращает сумму транзакций"""
    amount = transactions["operationAmount"]["amount"]
    currency = transactions["operationAmount"]["currency"]["code"]

    if ["operationAmount"] == currency:
        return ["operationAmount"]

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

    result = get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
    # print(result)
