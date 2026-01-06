import json
from utils import actions
from utils import ui


data = {
    "name": "Василій",
    "age": 12,
    "salary": 25000.5,
    "human": True,
    "skilss": ["фудбол", "сантехнік", "ПОТУЖНО"]
}


# with open('data1.json', 'r', encoding="utf-8") as f:
#     templates = json.load(f)

# for key, value in templates.items():
#     print(f"{key}: {value}")

info = actions.load_json('main_menu.json')

ui.index_list(info)