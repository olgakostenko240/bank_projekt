from typing import Any, Generator


def filter_by_currency(transactions: Any, currency: Any) -> filter | str:
    """Функция принимает на фход список своварей и возвращает id операции"""
    if len(transactions) > 0:
        filtered_transactions = filter(
            lambda transactions: transactions.get("operationAmount").get("code") == currency, transactions
        )
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions: Any) -> Generator[Any, Any, str]:
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    try:
        for transaction in transactions:
            yield transaction.get("description")
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
