from utils import actions, ui

def loop_menu(menu_json='./data/main_menu.json', prompt='\nEnter: ', header='Головне меню'):

    infomenu = actions.load_json(menu_json)

    while True:
        ui.clear(0)
        print(f'--- {header} ---\n')
        ui.index_list(infomenu)
        user = actions.input_split(prompt)
        res = actions.filtr_list(user, infomenu)

        if res: return res[0]