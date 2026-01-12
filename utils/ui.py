# Бібліотека створена для написання чота в консолі

import os
import time

# Функція для очистки консолі
def clear(parametr):
    time.sleep(parametr)
    os.system('cls')

# Виводить помилку
def show_error(item):
    print(f"'{item}' is not correct!")

# Вивід списку з нумерацією
def index_list(out_info):
    for index, name in enumerate(out_info, start=1):
        print(f"{index}. {name['name']}")
