import constants
from constants import ABILITIES
activity = 'Выберите действие из списка:\n'

def main_menu():
    print(list(enumerate(ABILITIES, start = 1)), sep='\n')

main_menu()