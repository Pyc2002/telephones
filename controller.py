from user_interface import get_menu_item
# from remove_contact import delete_contact
from add_contact import add_contact
# from edit_contact import edit_contact
from search import search_by
from show_db import show
import output


def procedure():
    while True:
        choice = get_menu_item()
        if choice == 1:
            add_contact()
        # elif choice == 2:
        #     delete_contact()
        # elif choice == 3:
        #     edit_contact()
        elif choice == 4:
            search_by()
        elif choice == 5:
            show()
        elif choice == 6:
            output.output_menu()
        elif choice == 7:
            exit()
