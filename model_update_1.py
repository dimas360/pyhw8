import csv
from log import error_enter


def read():
    with open('Hogwarts.csv', 'r', newline='\n', encoding='utf-8') as f:
        r = csv.reader(f, delimiter=";")
        for rec in r:
            print(rec)


def update():
    with open('Hogwarts.csv', 'r', newline='\n', encoding='utf-8') as f:
        n_id = input('Enter id of employee that you want to change :')
        print('1. Change Name')
        print('2. Change Position')
        print('3. Change Subject ')
        print('4. Change Owl')
        print('5. Change Comments')
        try:
            n = int(input('Enter the section that you want to change (1,2->5):'))
        except ValueError:
            error_enter()
        found = 0
        r = csv.reader(f, delimiter=";")
        nrec = []
        for rec in r:
            if rec[0] == n_id:
                if n == 1:
                    print('Current record:', rec)
                    rec[1] = input("Enter new name:")
                    print('Updated record:', rec)
                    found = 1
                elif n == 2:
                    print('Current record:', rec)
                    rec[2] = input("Enter new Position:")
                    print('Updated record:', rec)
                    found = 1
                elif n == 3:
                    print('Current record:', rec)
                    rec[3] = input("Enter new subject:")
                    print('Updated record:', rec)
                    found = 1
                elif n == 4:
                    print('Current record:', rec)
                    rec[4] = input("Enter new Owl:")
                    print('Updated record:', rec)
                    found = 1
                elif n == 5:
                    print('Current record:', rec)
                    rec[5] = input("Enter new Comments:")
                    print('Updated record:', rec)
                    found = 1
            nrec.append(rec)

        if found == 0:
            print('Error, please try again :(')
            error_enter()
            f.close()
        else:
            with open('Hogwarts.csv', 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f, delimiter=';')
                w.writerows(nrec)

# read()
# update()
