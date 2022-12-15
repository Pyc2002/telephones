from constants import DATA_BASE, CONTACT_TEMPLATE
import csv


def get_lines():  # надо перенести в functions эту функцию
    with open(DATA_BASE, "r", newline='', encoding='windows-1251') as csvfile:
        result = csv.DictReader(csvfile, delimiter="|")
        data = []
        for row in result:
            data.append(list(row.values()))
    return data


def export_to_rows():
    reader = get_lines()
    with open("data_row.txt", "w", encoding="windows-1251") as file:
        for i in reader:
            file.writelines(" ".join(i) + "\n")


def export_to_columns():
    reader = get_lines()
    data = []
    for i in range(len(CONTACT_TEMPLATE)):
        data.append(list(j[i] for j in reader))
    with open("data_col.txt", "w", encoding="windows-1251") as file:
        for i in data:
            file.writelines(" ".join(i) + "\n")
