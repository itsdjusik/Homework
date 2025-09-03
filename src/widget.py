def mask_account_card(number_account_card: str) -> str:
    """Принимает на вход тип и номер карты и возвращает ее маску в формате
    XXXX XX** **** XXXX, где X — это цифра."""

    if not all(c.isdigit() for c in number_account_card):
        number_account_card = number_account_card.strip().split()

        if len(number_account_card) == 2:
            type_card = number_account_card[0]
            number_card = number_account_card[1]

            if len(number_card) == 16:
                block_number = " ".join([number_card[i:i + 4] for i in range(0, len(number_card), 4)])
                mask_number = block_number[0:7] + "******" + block_number[-4:]
                return f"Тип карты: - {type_card}\nНомер карты: - {mask_number}"
            raise ValueError("Номер карты некорректен!")

    if all(c.isdigit() for c in number_account_card):
        if len(number_account_card) == 20:
            mask_number = "**" + number_account_card[-4:]
            return f"Номер счета: - {mask_number}"
        raise ValueError("Номер счета некорректен!")
