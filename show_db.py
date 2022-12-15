from constants import DATA_BASE
import csv


def show():
    with open(DATA_BASE, "r", newline='', encoding='windows-1251') as csvfile:
        reader = csv.DictReader(csvfile, delimiter="|")
        for row in reader:
            print(row)
