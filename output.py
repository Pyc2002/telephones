from functions import write_lines, get_lines
from constants import DATA_BASE
import json
import csv


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


def export_to_json():
    """
    Экспортирует данные из БД в файл формата *.json
    :return:
    """
    with open(DATA_BASE, "r", newline='', encoding='windows-1251') as csvfile:
        reader = list(csv.DictReader(csvfile, dialect='excel', delimiter=";"))
    with open("lines.json", "w", newline='', encoding='UTF-8') as file:
        file.write(json.dumps(reader, ensure_ascii=False, separators=(",", ":"), indent=4))
