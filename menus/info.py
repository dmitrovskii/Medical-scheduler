from menus import menu
from utils import ui, actions

FILEPATH = "./config/info_m.json"

def run():
    while True:
        choose = menu.loop_menu(FILEPATH, header="Інформація")
        action_name = actions.take_action(choose, FILEPATH)
        back = actions.route(action_name, INFO_MAP)

        if back == "return": 
            break


    
def add():
    print("Coming soon")
    return True

def delete():
    print("Coming soon")
    return False
    
def show(path="./data"): 
    ui.list_dir(path)


INFO_MAP = {
    "info_show": show,
    "add": add,
    "delete": delete
}