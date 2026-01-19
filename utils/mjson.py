import json, os
from utils import ui



def create(name):   
    """
    Create .json file, return false if file already exists
    """
    try:
        with open(f"./data/{name}", 'x', encoding='utf-8') as f:
            json.dump([], f, indent=4)
        return True
    
    except FileExistsError:
        return False 


def load_json(filepath):
    """
    Return load .json in python object
    """
    if not os.path.exists(filepath):
        ui.show_error(filepath)
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        ui.show_error(filepath)
        return []