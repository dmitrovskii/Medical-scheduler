"""
Виводить інформацію в консоль в залежності від заданих параметрів 
"""
import os
import time
import sys

# def clear():
#     if os.name == "nt":
#         os.system('cls')
#     else: 
#         os.system('clear')

def clear(value=0):
    if value == 0:
        sys.stdout.write('\x1b[2J\x1b[H')
    else:
        for _ in range(1, value):
            sys.stdout.write('\x1b[1A\x1b[2K')
    sys.stdout.write('\x1b[1A')
    sys.stdout.flush()


def show_files(path):
    """
    Виводить в стовбчик файли в заданій директорії
    """
    list_of_files = os.listdir(path)
    for item in list_of_files:
        print(item)

# Виводить помилку
def show_error(item, prompt='не є правильним!'):
    print(f"'{item}' {prompt}")
    time.sleep(1)

# Вивід списку з нумерацією
def index_dict_name(out_info, waittime=0):
    for index, name in enumerate(out_info, start=1):
        time.sleep(waittime)
        print(f"{index}. {name['name']}")

# def index_list(info, waittime=0):
#     for index, name in enumerate(info, start=1):
#         time.sleep(waittime)
#         print(f"{index}. {name}")

def great_print(text):
    """
    Вивиодить текст з ефектом друкарської машини
    """
    for i in text:
        time.sleep(0.01)
        print(i, end="", flush=True)
    print('')
