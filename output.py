from constants import DATA_BASE, CONTACT_TEMPLATE
import csv


def get_lines():  # надо перенести в functions эту функцию
    """
    Считывает строки из базы данных и возвращает список,
    каждый элемент которого соответствует контакту

    :return:
    """
    with open(DATA_BASE, "r", newline='', encoding='windows-1251') as csvfile:
        result = csv.DictReader(csvfile, dialect='excel', delimiter=";")
        data = []
        for row in result:
            data.append(list(row.values()))
    return data


def write_lines(file_name: str, data):
    """
    Записывает данные в csv файл, разбивая список по колонкам
    :param file_name: имя выходного файла
    :param data: входящий список данных
    :return:
    """
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=';')
        for i in data:
            writer.writerow(i)


def export_to_rows():
    """
    Экспортирует контактные данные в файл формата csv
    в строку
    :return:
    """
    reader = get_lines()
    write_lines("rows.csv", reader)


def export_to_columns():
    """
    Экспортирует контактные данные в файл формата csv
    в столбик
    :return:
    """
    reader = get_lines()
    data = []
    for i in range(len(CONTACT_TEMPLATE)):
        data.append(list(j[i] for j in reader))
    write_lines("columns.csv", data)
