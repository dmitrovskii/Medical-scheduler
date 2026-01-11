from menus import menu

def run():
    some = menu.loop_menu("./data/info_m.json", header="Інформація")

    if some == 4:
        return
    
    
    