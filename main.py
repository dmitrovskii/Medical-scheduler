from menus import menu, info
from utils import actions, ui
import time

def main():

    while True:
        a = menu.loop_menu('./data/menu_m.json')   
        
        if a == 1:
            info.run()
        elif a == 2:
            print('no work')
            time.sleep(1)
            continue
        elif a == 3: 
            print('no work')
            time.sleep(1)
            continue
        else: break



if __name__ == '__main__': 
    main()