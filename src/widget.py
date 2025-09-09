import re


def mask_account_card(number_account_card: str) -> str:
    """Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Последний элемент строки должен быть номером (карты или счета).

    Возвращает строку с замаскированным номером:
    - Для карты 16 цифр: оставляем первые 6 и последние 4 видимыми, остальное маскируем.
    - Для счета 20 цифр: оставляем только последние 4 цифры видимыми.

    Примеры:
    "Visa Platinum 7000792289606361" -> "Visa Platinum\n7000 79** **** 6361"
    "Счет 12345678901234567890" -> "Счет\n**7890"""

    parts = number_account_card.strip().split()
    if len(parts) >= 2:
        type_card = " ".join(parts[:-1])
        number_card = parts[-1]

        if type_card[0].lower() in ("счет", "счёт") and len(number_card) == 20 and number_card.isdigit():
            mask_number = "**" + number_card[-4:]
            return f"{' '.join(type_card)}\n{mask_number}"

        elif type_card[0].lower() not in ("счет", "счёт") and len(number_card) == 16 and number_card.isdigit():
            block_number = " ".join([number_card[i:i + 4] for i in range(0, len(number_card), 4)])
            mask_number = block_number[0:7] + "** **** " + block_number[-4:]
            return f"{' '.join(type_card)}\n{mask_number}"
        else:
            raise ValueError("Некорректный номер карты или счета!")
    raise ValueError("Неверный ввод! Введите тип и номер карты/счета.")

date = "2024-03-11T02:26:18.671407"


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ' ('11.03.2024')."""

    formatted_date = date[0:10]
    correct_date = re.sub(r"\-", ".", formatted_date)
    return ".".join(correct_date.split(".")[::-1])


def get_masks() -> None:
    """Запрашивает у пользователя ввод, обрабатывает ошибки и печатает результат маски"""
    while True:

        try:

            print("Выберите, что хотите ввести:")
            print()
            print("1 - Тип и номер карты")
            print("---------------------")
            print("2 - Номер счета")
            print("---------------")

            user_input = input("Ваш выбор: ").strip()
            if user_input in ("1", "2"):
                if user_input == "1":
                    number_account_card = input("Введите тип и номер карты через пробел: ").strip()
                    list_account_card = number_account_card.split()
                    if len(list_account_card) < 2:
                        raise ValueError("Введите тип карты!")
                    if (
                        list_account_card[0].lower() not in ("счет", "счёт")
                        and len(list_account_card[-1]) == 16
                        and list_account_card[-1].isdigit()
                    ):
                        print(mask_account_card(number_account_card))
                        break
                    raise ValueError("Вы выбрали карту, а ввели счет!")

                elif user_input == "2":
                    number_account_card = input("Введите тип и номер счета через пробел: ").strip()
                    list_account_card = number_account_card.split()
                    if len(list_account_card) < 2:
                        raise ValueError("Введите тип счета!")
                    if len(list_account_card[-1]) == 20 and list_account_card[-1].isdigit():
                        print(mask_account_card(number_account_card))
                        break
                    raise ValueError("Вы выбрали счет, а ввели карту!")

            raise ValueError("Некорректный ввод! Введите 1 - тип и номер карты, 2 - номер счета")
        except ValueError as err:
            print("Ошибка!", err)


if __name__ == "__main__":
    get_masks()
    get_date(date)
