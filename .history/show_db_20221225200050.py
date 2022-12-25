from functions import get_lines
from constants import DAT


def show():
    """
    Показывает базу данных.

    :return:
    """
    reader = get_lines()
    for row in reader:
        print(*row.values())
