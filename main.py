import log
from person_search2 import person_search
from print_info import print_hogwarts
from find_of_atribute import print_position
from adding_info import adding
from model_update_1 import read, update
from model_delete import delete_data
from exceptions import user_choice


def input_menu_choice():
    log.start_app()
    while True:
        print()
        print('-----------------------')
        print('What do you want to do?')
        print('-----------------------')
        print()
        print('1. Show all')
        print('2. Find info')
        print('3. Add new info')
        print('4. Change info')
        print('5. Delete info')

        print('0. Exit')
        choice_menu = user_choice()
        if choice_menu == 1:
            print_hogwarts()
        elif choice_menu == 2:
            print('1. Find by name')
            print('2. Find by position')
            print('0. Exit')
            choice1 = user_choice()
            if choice1 == 1:
                person_search()
            elif choice1 == 2:
                print_position()
            elif choice1 == 0:
                log.end_app()
                input_menu_choice()
            else:
                print('Error')
                log.error_enter()
                input_menu_choice()
        elif choice_menu == 3:
            adding()
            log.add()
            print('Data successfully added')
        elif choice_menu == 4:
            read()
            update()
            log.change()
        elif choice_menu == 5:
            read()
            delete_data()
            log.del_item()
        elif choice_menu == 0:
            log.end_app()
            return exit()
        else:
            print('Error')
            log.error_enter()
            return input_menu_choice()


input_menu_choice()
