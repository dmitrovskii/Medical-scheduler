# Тут буде відбуватися перенаправлення юзера на функцію в залежності від його вибору 

from menus import info, settings, about

ROUTES = {
    "info": info.run,
    "settings": settings.run,
    "about": about.run
}

def run(action_name):
    func = ROUTES.get(action_name)
    ROUTES[func]()
