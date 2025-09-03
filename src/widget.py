import re

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


def get_date(date: str) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ' ('11.03.2024')."""

    formatted_date = date[0:10]
    correct_date = re.sub(r"\-", "\.", formatted_date)
    return ".".join(correct_date.split(".")[::-1])


def get_masks():
    try:
        while True:
            print("Выберете, что хотите ввести:")
            print()
            print("1 - Тип и номер карты")
            print("---------------------")
            print("2 - Номер счета")
            print("---------------")

            user_input = input("Ваш выбор: ").strip()
            if user_input == "1":
                number_account_card = input("Введите тип и номер карты через пробел: ").strip()
                print(mask_account_card(number_account_card))
                break

            elif user_input == "2":
                number_account_card = input("Введите номер счета: ").strip()
                print(mask_account_card(number_account_card))
                break
            else:
                print("Некорректный вввод! Введите 1 - тип и номер карты, 2 - номер счета")
                print()
    except ValueError:
        print("Вы ввели некорректные данные!")


if __name__ == "__main__":
    get_masks()
