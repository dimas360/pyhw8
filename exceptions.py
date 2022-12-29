from log import error_enter, search


def user_choice():
    choice1 = input('Please enter you choice: ')
    try:
        choice1 = int(choice1)
        if (choice1 > 5) and (choice1 < 0):
            print('Error')
            return user_choice()
        else:
            return choice1
    except ValueError:
        print('Error')
        error_enter()
        return user_choice()


def data_search():
    try:
        my_search = input('Enter a position to search for employees: ')
        search(my_search)

    except ValueError:
        print('Error')
        error_enter()
    return my_search
