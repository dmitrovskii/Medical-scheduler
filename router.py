# Тут буде відбуватися перенаправлення юзера на функцію в залежності від його вибору 

from menus import info, settings, about
from utils import core

ROUTES = {
    "info": info.run,
    "settings": settings.run,
    "about": about.run
}

def run(action_name):
    core.route(action_name, ROUTES)
