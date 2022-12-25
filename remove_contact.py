from functions import get_lines, write_lines
from constants import DATA_BASE, CONTACT_TEMPLATE
from search import search_by


def delete_contact():
    reader = get_lines()
    choice = search_by()
    try:
        reader.remove(choice[0])
    except IndexError:
        return print("Couldn't find data")
    reader.insert(0, CONTACT_TEMPLATE.keys())
    write_lines(DATA_BASE, reader)
    return print("Removing comlete")
