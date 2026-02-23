import os
import time

import config
from menus import info, settings, about
from menus.menu import MenuHandler

ROUTES = {
    "info": info.run,
    "settings": settings.run,
    "about": about.run
}

def main():
    menu = MenuHandler(config.MAIN['menu']) 
    try:
        menu.run("MAIN MENU", ROUTES)
    except KeyboardInterrupt: 
        print("\nClose program...")


if __name__ == '__main__': 
    main()