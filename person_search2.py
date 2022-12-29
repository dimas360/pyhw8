from log import search, error_enter


def person_search():
    name = input('Enter name: ')
    search(name)
    with open('Hogwarts.csv', 'r', encoding='utf_8') as data:
        data_list = data.readlines()
        for i in range(1, len(data_list)):
            if name in data_list[i]:
                print(data_list[i])
                break
        else:
            error_enter()
            print('data not found')
