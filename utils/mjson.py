"""
Work with .json
"""


import json, os
from utils import ui



def create(name, path):   
    """
    Create .json file, return false if file already exists
    """
    try:
        with open(f"{path}/{name}", 'x', encoding='utf-8') as f:
            json.dump([], f, indent=4)
        return True
    
    except FileExistsError:
        return False 


def load(filepath):
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