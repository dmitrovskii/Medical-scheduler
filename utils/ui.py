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
def index_dict_name(out_info):
    for index, name in enumerate(out_info, start=1):
        time.sleep(0.05)
        print(f"{index}. {name['name']}")

def index_list(info):
    for index, name in enumerate(info, start=1):
        time.sleep(0.05)
        print(f"{index}. {name}")

def list_dir(dirpath):
    show = os.listdir(dirpath)
    index_list(show)

def great_print(info):
    for i in info:
        print(i, end="", flush=True)