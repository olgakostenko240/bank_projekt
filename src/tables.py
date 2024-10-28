from typing import Any

import pandas as pd


def read_cvs(file_name: str) -> list[dict[Any, Any]]:
    """Функция для считавыния финансовых операций из CSV"""
    transactions_csv = pd.read_csv(file_name, encoding="UTF-8")
    df_dict: list[dict[Any, Any]] = transactions_csv.to_dict(orient="records")
    return df_dict


def read_excel(file_path: str) -> list[dict[Any, Any]]:
    """Функция для считавыния финансовых операций из Excel"""
    excel_data = pd.read_excel(file_path)
    excel_data_dict: list[dict[Any, Any]] = excel_data.to_dict(orient="records")
    return excel_data_dict


if __name__ == "__main__":
    print(read_cvs("../data/transactions.csv"))

if __name__ == "__main__":
    print(read_excel("../data/transactions_excel.xlsx"))
