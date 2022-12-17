from functions import give_int
from constants import ABILITIES
from

choose_option = 'Выберите действие из списка:\n'

def get_menu_item():
    """
    Функция выводит все возможные действия с БД
    Returns:
       choice: Выбор пользователя -> int
    """
    for i, item in list(enumerate(ABILITIES, start=1)):
        print(i, item, end='\n')
    choice = give_int(choose_option, 1)
    return choice

def 



get_menu_item()