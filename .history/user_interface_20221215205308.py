import constants
from constants import ABILITIES
activity = 'Выберите действие из списка:\n'

def main_menu():
    print(enumerate(ABILITIES, start = 1))