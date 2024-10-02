import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 899092211366522956", None),
        ("8777578868898578", "8777 57** **** 8578"),
        ("64686473678894779589", "**9589"),
        ("Счет 736541084301358", None),
        ("Visa Platinum 89do922113r65229", "Visa Platinum None"),
        ("Счет 7365410843d58e74e305", "Счет None"),
        ("Maestro 15963786870519", None),
        ("Счет 86473678894779589", None),
    ],
)
def test_mask_account_card(number: str, expected_result: str) -> None:
    assert mask_account_card(number) == expected_result


@pytest.mark.parametrize(
    "format_data, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2015-05-30T12:26:15.251587", "30.05.2015"),
        ("1945-04-12T33:26:15.251587", "12.04.1945"),
    ],
)
def test_get_data(format_data: str, expected_result: str) -> None:
    assert get_data(format_data) == expected_result
