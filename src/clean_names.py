def get_only_names(file_names: str) -> list[str]:
    """Принимает файл с именами и возвращает имена без знаков препинания и цифр"""

    cool_names = []
    try:
        with open(file_names, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                only_name = "".join(c for c in line if c.isalpha())
                if only_name:
                    cool_names.append(only_name)
        return cool_names
    except FileNotFoundError:
        print("Файл не найден! Проверьте путь к файлу!")
        return []


file_path = r"C:\Users\User\PycharmProjects\Homework\src\data\result_filter.txt"


def writing_file(cool_names: list[str], file_path: str) -> None:
    """Записывает отчищенные от пробелов и цифр имена в файл"""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(cool_names))
            print("Список имен успешно сохранен")
    except FileNotFoundError:
        print("Файл отсутствует!")


if __name__ == "__main__":
    result = get_only_names("src/data/names.txt")
    # print(*result, sep=", ")
    writing_file(result, file_path)
