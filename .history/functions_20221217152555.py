from typing import Optional
from typing import List
import constants

def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    Takes: string
    Returns: int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')



def get_list_data(filename: str) -> List[str]:
    '''
    Возвращает список из строк файла
    Args:
    filename - имя файла
    Returns:
    List[str]
    '''
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')

def get_lines():    # надо перенести в functions эту функцию
    with open(DATA_BASE, "r", newline='', encoding='windows-1251') as csvfile:
        reader = csv.DictReader(csvfile, delimiter="|")
        data = []
        for row in reader:
            if search_data in row[atr]:
                data.append(row)
        for i in data:
            print(*i.values())
        result = csv.DictReader(csvfile, delimiter="|")
    return result