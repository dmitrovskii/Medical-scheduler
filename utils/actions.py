"""
Background for app
"""


import pyperclip, json
from utils import ui, mjson


# Копіювання в буфер
def copy_buf(info):
    pyperclip.copy("\n".join(info))

# Нарізання введеної інформації
def input_split(prompt=""):
    """Split string to list with string data"""
    split_list = input(str(prompt)).split()
    return split_list

# Перетворення даних ліста на інт та прохід фільтрів. Для праці з індексами
def filtr_list(splitted, list_of_dict):
    """Перетворює масив зі str на масив з int.
    Видає помилку, якщо елемент масиву не є числом,
    або є більшим за довжину масиву."""
    time_list = []
    for item in splitted:
        try: 
            index = int(item)
            if 1 <= index <= len(list_of_dict):
                time_list.append(index - 1)
            else: 
                ui.show_error(item)
        except ValueError: 
            ui.show_error(item)
    return time_list


def take_action(index, filepath):
    if isinstance(index, list):
        if len(index) > 0:
            index = index[0]
        else: 
            return None

    load_list = mjson.load(filepath)
    return load_list[index]['action']

