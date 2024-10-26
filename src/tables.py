import pandas as pd


def read_cvs(file_name: str) -> list[dict]:
    transactions_csv = pd.read_csv(file_name, encoding='UTF-8')
    df_dict = transactions_csv.to_dict(orient='records')
    return df_dict


def read_excel(file_path: str) -> list[dict]:
    excel_data = pd.read_excel(file_path)
    excel_data_dict = excel_data.to_dict(orient='records')
    return excel_data_dict


if __name__ == "__main__":
    print(read_cvs("../data/transactions.csv"))

if __name__ == "__main__":
    print(read_excel("../data/transactions_excel.xlsx"))
