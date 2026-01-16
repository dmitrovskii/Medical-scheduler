from menus import menu
from utils import actions
import router

def main():

    while True:
        main_menu = menu.loop_menu()   
        res = actions.take_action(main_menu, './config/menu_m.json')
        route = router.run(res)
        if route == "exit":
            break

if __name__ == '__main__': 
    main()