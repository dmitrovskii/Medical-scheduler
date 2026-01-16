from menus import menu
from utils import ui

def run():
    choose = menu.loop_menu("./config/info_m.json", header="Інформація")

    if choose == 4:
        return
    
    
def show(path="./data"): 
    ui.list_dir(path)