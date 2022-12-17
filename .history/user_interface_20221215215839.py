from functions import give_int
from constants import ABILITIES


choose_option = 'Выберите действие из списка:\n'

def get_menu_item() -> int:
    """
    Функция выводит все возможные действия с БД
    Returns:
       choice: Выбор пользователя -> int
    """
    for i, item in list(enumerate(ABILITIES, start=1)):
        print(i, item, end='\n')
    choice = give_int(choose_option, 1, 6)
    return choice


if 
choice = get_menu_item()