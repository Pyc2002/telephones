from functions import get_lines
from 


def show():
    """
    Показывает базу данных.

    :return:
    """
    reader = get_lines()
    for row in reader:
        print(*row.values())
