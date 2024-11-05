import logging
import os

current_logs = os.path.dirname(os.path.abspath(__file__))
rel_logs_file_path = os.path.join(current_logs, "../logs/masks.log")
logs_file_path = os.path.abspath(rel_logs_file_path)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(logs_file_path, encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция, которая маскирует номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Маскирует карту клиента.")
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    else:
        logger.error("Ошибка. Неправильный ввод карты.")
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Функция, которая маскирует номер счета"""
    if acc_number.isdigit() and len(acc_number) == 20:
        logger.info("Маскирует счет клиента.")
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        logger.error("Ошибка. Неправильный ввод счета.")
        return None


if __name__ == "__main__":
    print(get_mask_card_number(str(1234667765434972)))
    print(get_mask_account(str(12346677654349084693)))
