from menus import menu
from utils import core, ui, actions, mjson
import config as cf

import os


def create(prompt='Назва файлу: '):

    ui.great_print("Створюйте .json файли. Програма працює лише з ними.\n")
    ui.great_print("Пропишіть 'exit', щоб вийти.\n")

    while True:
        name_file = input(prompt)

        if name_file == "exit": break

        elif name_file.endswith('.json'):
            complete = mjson.create(name_file)
            if complete:
                ui.great_print(f"Файл '{name_file}' створено!")
            else: 
                ui.show_error(name_file, "Файл вже існує!")
        else:
            ui.show_error(name_file)

def strings():
    ui.great_print('Coming soon')
    input()



def add():
    ui.great_print("Coming soon")
    input()
    return True

def delete():
    ui.show_files('./data')
    ui.great_print("Щоб відмінити - 'exit'")
    while True:
        filename = input("Enter: ")
        if filename == "exit": 
            break
        elif not os.path.exists(f'./data/{filename}'):
            ui.show_error(filename, "не існує!")
        else: 
            os.unlink(filename)
            ui.great_print("Файл видалено!")


def files():
    # ui.show_files('./data')
    # input()
    # return
    while True:
        user_choise = menu.loop_menu(cf.INFO['files'], header='Файли. Маніпуляція')
        action_name = actions.take_action(user_choise, cf.INFO['files'])
        ui.clear()
        
        back = core.route(action_name, INFO_MAP)
        if not back: break
    
    
def rename():
    ui.great_print('Coming soon')
    input()

INFO_MAP = {
    "files": files,
    "strings": strings,

    "rename": rename,

    "add": add,
    "delete": delete,
    "create": create
}

def run():
    while True:
        choose = menu.loop_menu(cf.MAIN['info'], header="Файли та рядки")
        action_name = actions.take_action(choose, cf.MAIN['info'])
        ui.clear()
        
        back = core.route(action_name, INFO_MAP)
        if not back: break