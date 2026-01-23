from utils import actions, ui, mjson

def loop_menu(config_path, prompt='\nEnter: ', header='Головне меню'):

    infomenu = mjson.load(config_path)

    while True:
        ui.clear()
        print(f'--- {header} ---\n')
        ui.index_dict_name(infomenu)
        split_data = actions.input_split(prompt)
        res = actions.filtr_list(split_data, infomenu)

        # Повертає нульовий елемент в массиві, потрібно тільки тут адже це меню
        if res: return res[0]