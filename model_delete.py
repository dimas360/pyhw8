import csv
from log import error_enter


def read():
    with open('Hogwarts.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for rec in reader:
            print(rec)


def delete_data():
    with open('Hogwarts.csv', 'r', newline='\n', encoding='utf-8') as f:
        try:
            n_id = input('Enter id of employee that you want to delete :')
        except ValueError:
            error_enter()
        found = 0
        r = csv.reader(f, delimiter=";")
        nrec = []
        for rec in r:
            if rec[0] == n_id:
                print('deleted record:', rec)
                found = 1
            else:
                nrec.append(rec)

        if found == 0:
            print('Error, please try again :(')
            f.close()
        else:
            with open('Hogwarts.csv', 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f, delimiter=';')
                w.writerows(nrec)
# read()
# delete_data()
