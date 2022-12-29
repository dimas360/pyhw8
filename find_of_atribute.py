# from os import path
# # def print_csv(): # печать в консоль из файла Phonebook.csv
# #     file = 'Hogwarts.csv'
# #     if path.exists(file):
# #         with open(file, 'r', encoding='utf-8') as text:
# #             text_csv = text.readlines()
# #             for i, v in enumerate(text_csv):
# #                 print(v)
# print_csv()
import csv
from itertools import groupby
from log import search
from exceptions import data_search


def print_position():
    with open('Hogwarts.csv', encoding='utf-8') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter=";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        buff_position_list = []
    # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print('Position in Hogwarts:')
            # Вывод строк
            buff_position_list.append(row['Position'])
            count += 1
    # если я не использую метод sort(), то один из повторяющихся должностей повторится.
        buff_position_list.sort()
        position_list = [k for k, g in groupby(buff_position_list)]
        print(position_list)
        print(f'Total employees at Hogwarts {count + 1}.')
        find_personal = data_search()
        find_personal = find_personal.lower()
        print(find_personal)
    with open("Hogwarts.csv", encoding='utf-8') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter=";")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                print(f'{", ".join(row)}')
            count += 1
            if row['Position'] == find_personal:
                print(f'{count}, {row["Name"]}, {row["Position"]}, {row["Subject"]}, {row["Owl"]}, {row["Comments"]}')
            




# def search_person(find_personal = str(input('Введите должность для поиска сотдрудников: '))):
    # find_personal.lower()
    # with open("Hogwarts.csv", encoding='utf-8') as r_file:
    #     # Создаем объект DictReader, указываем символ-разделитель ","
    #     file_reader = csv.DictReader(r_file, delimiter=";")
    #     # Счетчик для подсчета количества строк и вывода заголовков столбцов
    #     count = 0
    #     # Считывание данных из CSV файла
    #     for row in file_reader:
    #         if count == 0:
    #             print(f'{", ".join(row)}')
    #         count += 1
    #         if row['Position'] == find_personal:
    #             print(f'{count}, {row["Name"]}, {row["Position"]}, {row["Subject"]}, {row["Owl"]}, {row["Comments"]}')

# print_position()
