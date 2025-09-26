from typing import Any


def filter_by_state(data_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает список словарей, фильтрует по ключу state и возвращает новый список словарей"""

    new_data = list(i for i in data_list if i["state"] == state)
    return new_data


data_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


print(*filter_by_state(data_list), sep="\n")


def sort_by_date(data_rev: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей и необязательный
    параметр, задающий порядок сортировки (по умолчанию — убывание)"""

    new_data_rev = list(sorted(data_rev, key=lambda x: x["date"], reverse=reverse))
    return new_data_rev


print(*sort_by_date(data_list), sep="\n")
