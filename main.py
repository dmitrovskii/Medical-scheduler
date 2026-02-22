import os
import time

import config
from utils import mjson, ui
from menus import info, settings, about
from menus.menu import MenuHandler

ROUTES = {
    "info": info.run,
    "settings": settings.run,
    "about": about.run
}

def main():
    path_to_file = config.MAIN['menu']

    mdict = mjson.load(path_to_file)
    menu = MenuHandler(path_to_file)

    try: 
        while True:
            print(" --- MAIN INFO --- \n")
            ui.index_dict_name(mdict)   

            raw_input = input('\nEnter: ')
            valid_indices = menu.process_input(raw_input)

            if valid_indices:
                index = valid_indices[0]
                action_name = menu.get_action_by_index(index)
                ui.clear()

                if action_name == "exit":
                    break
                menu.route_data(action_name, ROUTES)

            time.sleep(1) 
            ui.clear(3)

    except KeyboardInterrupt: 
        print("\nClose program...")


if __name__ == '__main__': 
    main()