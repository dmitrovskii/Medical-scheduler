# Бібліотека створена для написання чота в консолі

import os
import time

# Функція для очистки консолі
def clear(ytime):
    time.sleep(ytime)
    os.system('cls')

# Виводить помилку
def show_error(item):
    print(f"'{item}' is not correct!")

# Вивід списку з нумерацією
def index_list(out_info):
    for index, name in enumerate(out_info.values(), start=1):
        print(f"{index}. {name}")
