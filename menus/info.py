from menus import menu
from utils import core, ui, actions, mjson
from config import FILES

# INFO = FILES['info']

def run():
    while True:
        choose = menu.loop_menu(FILES['info'], header="Файли та рядки")
        action_name = actions.take_action(choose, FILES['info'])
        back = core.route(action_name, INFO_MAP)

        if back == False: 
            break


def create(prompt='Назва файлу: '):
    ui.great_print("Створюйте .json файли. Програма працює лише з ними.\n")
    ui.great_print("Пропишіть 'exit', щоб вийти.\n")

    while True:
        name_file = input(prompt)
        if name_file == "exit":
            break

        elif name_file.endswith('.json'):
            complete = mjson.create(name_file)

            if complete:
                ui.great_print(f"Файл '{name_file}' створено!")
            else: 
                ui.show_error(name_file, "Файл вже існує!")
        else:
            ui.show_error(name_file)

def add():
    ui.great_print("Coming soon")
    input()
    return True

def delete():
    ui.great_print("Coming soon")
    input()
    return True

    
def show(path="./data"): 
    ui.list_dir(path)
    input()

INFO_MAP = {
    "info_show": show,
    "add": add,
    "delete": delete,
    "create": create
}