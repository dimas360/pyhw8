from datetime import datetime


def start_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write(f'"Start work with app" Time {time_calc}\n')


def error_enter():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'{"Enter error"} Time {time_calc}\n')


def show_all():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'{"Showed all items"} Time {time_calc}\n')


def end_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'{"End work with app"} Time {time_calc}\n')


def search(search_object):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'Search: {search_object} Time {time_calc}\n')


def add():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'Added: {"Data successfully added"} Time {time_calc}\n')


def change():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'Changed: Time {time_calc}\n')


def del_item():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'Deleted: Time {time_calc}\n')
