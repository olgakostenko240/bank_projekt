import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "cart_number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1659354003746607", "1659 35** **** 6607"),
        ("64756488g6dd5342", None),
        ("85767686868888", None),
        ("436827408342675175", None),
        ("", None),
    ],
)
def test_get_mask_card_number(cart_number: str, expected_result: str) -> None:
    assert get_mask_card_number(cart_number) == expected_result


@pytest.mark.parametrize(
    "acc_number, expected_result",
    [
        ("73654108430135674305", "**4305"),
        ("45657476535645753544", "**3544"),
        ("37564678foe07457ft84", None),
        ("64565920165756565", None),
        ("104555537489903542758", None),
    ],
)
def test_get_mask_account(acc_number: str, expected_result: str) -> None:
    assert get_mask_account(acc_number) == expected_result
