# Тут буде відбуватися перенаправлення юзера на функцію в залежності від його вибору 

from menus import info, settings, about
from utils import ui

ROUTES = {
    "info": info.run,
    "settings": settings.run,
    "about": about.run
}

def run(action_name):
    func = ROUTES.get(action_name)
    
    if func: 
        func()
    else: 
        return action_name
