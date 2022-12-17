from user_interface import choice
from remove_contact import delete_contact
from add_contact import add_contacts

def procedure(choice):
    if choice == 1:
        add_contacts()
    elif choice == 2:
        delete_contact()
    elif choice
