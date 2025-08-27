from src.masks import get_mask_card_number

user_input = input("Введите номер карты: ").strip()
print(get_mask_card_number(user_input))
