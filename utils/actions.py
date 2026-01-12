# Бібліотека для роботи з тим, чого нема в консолі

import pyperclip
import json
import os
from utils import ui, actions

# Копіювання в буфер
def copy_buf(info):
    pyperclip.copy("\n".join(info))

# Нарізання введеної інформації
def input_split(ask):
    info = input(str(ask)).split()
    return info

# Перетворення даних ліста на інт та прохід фільтрів. Для праці з індексами
def filtr_list(splitted, info):
    time_list = []
    for item in splitted:
        try: 
            index = int(item)
            if 1 <= index <= len(info):
                time_list.append(index - 1)
            else: 
                ui.show_error(item)
        except ValueError: 
            ui.show_error(item)
        ui.clear(0.5)
    return time_list


def take_action(index, filepath):
    load_list = actions.load_json(filepath)
    return load_list[index]['action']

# Для завантаження джоснчіків
def load_json(filepath):
    if not os.path.exists(filepath):
        ui.show_error(filepath)
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        ui.show_error(filepath)
        return []

# Для запису джсончіків
def write_json(filepath, data):

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
