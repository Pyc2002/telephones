from constants import DATA_BASE
from datetime import datetime as dt
import csv

"add, edit, remove"

LOGGER_TEMPLATE = {
    "Имя": "",
    "Фамилия": "",
    "Телефон": "",
    "Группа": "",
    "Комментарий": "",
    "Дата": "",
    "Операция": ""
}


def add_logger(data, init):
    datetime = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.log', newline='') as file:
        reader = log.reader(file)
        for row in reader:
            print(row['Имя'], row['Фамилия'], row['Телефон'], row['Группа'], row['Комментарий'], row[datetime], row['Add contact'],)


