import pyperclip
import json
import os
from utils import ui

# Копіювання в буфер
def copy_buf(info):
    pyperclip.copy(info)

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

