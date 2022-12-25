from functions import get_lines
акщ


def show():
    """
    Показывает базу данных.

    :return:
    """
    reader = get_lines()
    for row in reader:
        print(*row.values())
