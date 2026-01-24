from menus import menu
from utils import actions, ui
from config import MAIN
import router

def main():

    while True:
        main_menu = menu.loop_menu(MAIN['menu'])   
        res = actions.take_action(main_menu, MAIN['menu'])
        ui.clear()
        if res == "exit":
            break
        
        
        router.run(res)

if __name__ == '__main__': 
    main()