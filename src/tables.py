from typing import Any

import pandas as pd

import os


current_csv = os.path.dirname(os.path.abspath(__file__))
rel_csv_file_path = os.path.join(current_csv, "../data/transactions.csv")
csv_file_path = os.path.abspath(rel_csv_file_path)

current_xlsx = os.path.dirname(os.path.abspath(__file__))
rel_xlsx_file_path = os.path.join(current_xlsx, "../data/transactions_excel.xlsx")
xlsx_file_path = os.path.abspath(rel_xlsx_file_path)


def read_cvs(file_name: str) -> list[dict[Any, Any]]:
    """Функция для считавыния финансовых операций из CSV"""
    transactions_csv = pd.read_csv(file_name)
    df_dict: list[dict[Any, Any]] = transactions_csv.to_dict(orient="records")
    return df_dict


def read_excel(file_path: str) -> list[dict[Any, Any]]:
    """Функция для считавыния финансовых операций из Excel"""
    excel_data = pd.read_excel(file_path)
    excel_data_dict: list[dict[Any, Any]] = excel_data.to_dict(orient="records")
    return excel_data_dict


if __name__ == "__main__":
    print(read_cvs(csv_file_path))

if __name__ == "__main__":
    print(read_excel(xlsx_file_path))
