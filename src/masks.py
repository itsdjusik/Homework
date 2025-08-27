def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате
    XXXX XX** **** XXXX, где X — это цифра."""

    if len(card_number) == 16:
        mask_middle = "*" * 6
        stroke_mask = card_number[:6] + mask_middle + card_number[-4:]
        block_mask = " ".join([stroke_mask[i : i + 4] for i in range(0, len(stroke_mask), 4)])
        return block_mask
    raise ValueError("Введите корректный номер карты!")


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску '**XXXX',
    где X — цифра номера."""

    if len(account_number) != 6 or not account_number.isdigit():
        raise ValueError("введите 6-х значный номер счета цифрами!")

    mask_number = "**" + account_number[2:]
    return mask_number


if __name__ == "__main__":
    number_card = input("Введите номер карты: ").strip()
    print(get_mask_card_number(number_card))
