from constants import DATA_BASE
import csv
import os.path
from functions import write_lines

def fieldnames():
    """Create file.csv if it not exists, to avoid duplicate headers
    
    args -> None
    returns -> None
    """
    if not os.path.exists(
            DATA_BASE):  # проверка существует ли файл (если да, то последующий код  функции не запускается)
        with open(DATA_BASE, 'a', newline='') as file:
            writer = csv.writer(file, dialect='excel', delimiter=';')
            writer.writerow(['Имя', 'Фамилия', 'Телефон', 'Группа', 'Комментарий'])
            file.close()


def check_name(
        text):  # не вводил проверку на количество символов, т.к. фамилии могут быть разной длины (двойные фамилии)
    """ Testing input data of first_name and last_name 

    args -> str (input text)
    retuns -> str
    """
    while not text.isalpha() or text == '':
        text = input('Ошибка! Обязательное поле, принимаются только буквы, повторите ввод: \n')
    return text.title()


def check_phone(num):
    """Testing input data of phone_number

    args -> str (input text)
    retuns -> str
    """
    while num == '' or not num[1:].isdigit() or num[
        0] != '+':  # не вводил проверку на количество символов, т.к. может быть иностранный номер
        num = input('Ошибка! Обязательное поле, принимаются только "+" и цифры, повторите ввод: \n ')

    with open(DATA_BASE, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for item in reader:
            while num in item['Телефон']:
                num = input(f'Этот номер телефона уже записан в справочнике, введите другой номер: \n ')
    return num


def add_contact():
    """ Adding data of new contact in csv-file. User inputs data (str), def create dict and add it in file.

    args -> None
    returns -> None
    """
    fieldnames()
    name = check_name(input('Введите имя контакта: \n '))
    last_name = check_name(input('Введите фамилию контакта: \n '))
    phone = check_phone(input('Введите телефон контакта(+ код страны телефон (без пробелов)):\n '))
    group = input('Введите группу контакта: \n ')
    comment = input('Введите комментарий контакта:\n ')
    new_contact = {'Имя': name, 'Фамилия': last_name, 'Телефон': phone, 'Группа': group, 'Комментарий': comment}

    with open(DATA_BASE, mode='a', newline='') as csv_file:
        field_names = ['Имя', 'Фамилия', 'Телефон', 'Группа', 'Комментарий']

        writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel', restval='', delimiter=';')
        writer.writerow(new_contact)
        csv_file.close()
