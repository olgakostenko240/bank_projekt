from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str | None:
    """Функция, маскирует счет/карту"""
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
        return result
    else:
        return None


def get_data(format_data: str) -> str:
    """Функция принимает на вход один формат даты, а выводит в формате dd.mm.gggg"""
    new_format_data = format_data[0:10].split("-")
    return ".".join(new_format_data[::-1])
