import os
import re


def create_name_filter(file_names: str) -> tuple[list[str], list[str]]:
    """Принимает файл с именами на разном языке, возвращает два файла с именами на русском
    и английском языке"""

    eng_names = []
    rus_names = []

    if os.path.exists("src/data"):
        try:
            with open(file_names, "r", encoding="utf-8") as file:
                for name in file:
                    name = name.strip()
                    if re.fullmatch(r"[A-Za-z]+", name):
                        eng_names.append(name)
                    if re.fullmatch(r"[А-Яа-яЁё]+", name):
                        rus_names.append(name)
            eng_names.sort()
            rus_names.sort()
            return eng_names, rus_names
        except FileNotFoundError:
            print("Файл отсутствует!")
    else:
        os.makedirs("src/data")


path_name_filter = r"src/data/result_filter.txt"

if __name__ == "__main__":
    english_name, russian_name = create_name_filter(path_name_filter)
    print()
    print("Английские имена:")
    print("-----------------")
    for name in english_name:
        print(name, sep=", ")
    print()
    print("Русские имена:")
    print("--------------")
    for name in russian_name:
        print(name, sep=", ")
