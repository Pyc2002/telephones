from user_interface import choice
from remove_contact import delete_contact
from add_contact import add_contacts
from edit_contact import edit_contact
from search import search_by
from show_db import show

def procedure(choice):
    while True:
        #добавить выбор пункта меню экспорт 
        if choice == 1:
            add_contacts()
        elif choice == 2:
            delete_contact()
        elif choice == 3:
            edit_contact()
        elif choice == 4:
            search_by()
        elif choice == 5:
            show()
        elif choice == 6:
            exit()


