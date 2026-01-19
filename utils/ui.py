"""
Output information to console with mamipulation 
"""

import os
import time

# Функція для очистки консолі
def clear(parametr):
    time.sleep(parametr)
    os.system('cls')

# Виводить помилку
def show_error(item, prompt='is not correct!'):
    print(f"'{item}' {prompt}")
    time.sleep(1)

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

def great_print(text):
    """
    Print text with drucar machine effect
    """
    for i in text:
        time.sleep(0.01)
        print(i, end="", flush=True)