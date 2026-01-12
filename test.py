from menus import menu, info
from utils import actions, ui



# with open('data1.json', 'r', encoding="utf-8") as f:
#     templates = json.load(f)

# for key, value in templates.items():
#     print(f"{key}: {value}")

# attemp = actions.load_json('./data/menu_m.json')
# print(attemp,"\n")

# for s in attemp.items():
#     print(s, "\n")

def take_action(index, filepath):
    load_list = actions.load_json(filepath)
    return load_list[index]['action']

