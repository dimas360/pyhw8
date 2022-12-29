# добавление строки в базу

def adding():
    to_add = []
    print("\nYou are adding info to base. If you don't know what to put, put: None\n")
    to_add.append(input('Name: '))
    to_add.append(input('Position: '))
    to_add.append(input('Subject: '))
    to_add.append(input('What is his pets name: '))
    to_add.append(input('Extra: '))
    with open('last_key.txt', "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    with open('Hogwarts.csv', "a", encoding='utf-8') as base:
        base.write('{};{};{};{};{};{}\n'.format(new_key + 1, to_add[0], to_add[1], to_add[2], to_add[3], to_add[4]))
    with open('last_key.txt', "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
