from functions import get_lines, write_lines
from constants import DATA_BASE, CONTACT_TEMPLATE
from search import search_by
from constants import ABILITIES
import log
from add_contact import fieldnames, check_name, check_phone
import csv
import os.path


def edit_contact():
    reader = get_lines()
    choice = search_by()
    try:
        reader.remove(choice[0])
    except IndexError:
        return print("Couldn't find data"), log.add_logger(f"{ABILITIES[2]};{choice}; Couldn't find data")
    modify_key = input("""
Enter key number to modify field
Имя        : [0]
Фамилия    : [1]
Телефон    : [2]
Группа     : [3]
Комментарий: [4]
""")
    edit_contact = choice[0]
    name = edit_contact[0]
    last_name = edit_contact[1]
    phone = edit_contact[2]
    group = edit_contact[3]
    comment = edit_contact[4]
    
    if modify_key == '0':
        name = check_name(input('Введите новое имя контакта: \n '))
    elif modify_key == '1':
        last_name = check_name(input('Введите новую фамилию контакта: \n '))
    elif modify_key == '2':
        phone = check_phone(input('Введите новый телефон контакта(+ код страны телефон (без пробелов)):\n '))
    elif modify_key == '3':
        group = input('Введите новую группу контакта: \n ')
    elif modify_key == '4':
        comment = input('Введите новый комментарий контакта:\n ')
    else: print("Couldn't find data")

    edit_contact = {'Имя': name, 'Фамилия': last_name, 'Телефон': phone, 'Группа': group, 'Комментарий': comment}

    reader.insert(0, CONTACT_TEMPLATE.keys())
    write_lines(DATA_BASE, reader)

    fieldnames()

    with open(DATA_BASE, mode='a', newline='') as csv_file:
        field_names = ['Имя', 'Фамилия', 'Телефон', 'Группа', 'Комментарий']

        writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel', restval='', delimiter=';')
        writer.writerow(edit_contact)
        csv_file.close()

    return print("Edit complete"), log.add_logger(f"{ABILITIES[1]}; До редактирования:{choice}"), log.add_logger(f"{ABILITIES[2]}; Новая редакция: {edit_contact}")
