from menus import menu
from utils import actions
from config import FILES
import router

def main():

    while True:
        main_menu = menu.loop_menu(FILES['menu'])   
        res = actions.take_action(main_menu, FILES['menu'])
        
        if res == "exit":
            break
        
        router.run(res)

if __name__ == '__main__': 
    main()