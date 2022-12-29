from os import path
from log import show_all


def print_hogwarts():  # печать в консоль из файла Hogwarts.csv
    file = 'Hogwarts.csv'
    if path.exists(file):
        show_all()
        with open(file, 'r', encoding='utf-8') as text:
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                print(v.strip())
