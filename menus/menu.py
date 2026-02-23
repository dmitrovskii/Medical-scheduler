import os
import time
import config
from utils import mjson, ui

class MenuHandler:
    def __init__(self, filepath):
        self._filepath = filepath
        self._menu_items = None

    @property
    def menu_items(self): # Lazy load
        if self._menu_items is None:
            if not os.path.exists(self._filepath):
                raise FileNotFoundError(f"File '{self._filepath}' not found!")
            self._menu_items = mjson.load(self._filepath)
        return self._menu_items

    def process_input(self, raw_input: str) -> list:
        splitted = raw_input.split()
        valid_indices = []
        menu_length = len(self.menu_items)

        for item in splitted:
            try:
                user_num = int(item)
                if 1 <= user_num <= menu_length:
                    valid_indices.append(user_num - 1)
                else: print(f"The number '{user_num}' is out of menu range!")
            except ValueError: print(f"'{item}' is not a number!")
        return valid_indices

    def get_action_by_index(self, index: int) -> str:
        if 0 <= index <= len(self.menu_items):
            return self._menu_items[index]['action']
        return None

    def route_data(self, action_name, action_dict) -> function:
        func = action_dict.get(action_name)
        if func: func()

    def run(self, title: str, action_dict: dict) -> None:
        while True:
            ui.clear()
            print(f" --- {title} --- \n")
            ui.index_dict_name(self.menu_items)   

            raw_input = input('\nEnter: ')
            valid_indices = self.process_input(raw_input)

            if valid_indices:
                index = valid_indices[0]
                action_name = self.get_action_by_index(index)
                ui.clear()

                if action_name == "return":
                    return
                self.route_data(action_name, action_dict)
                
            ui.clear(3)