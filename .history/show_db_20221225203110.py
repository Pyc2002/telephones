from functions import get_lines
from constants


def show():
    """
    Показывает базу данных.

    :return:
    """
    reader = get_lines()
    for row in reader:
        print(*row.values())
