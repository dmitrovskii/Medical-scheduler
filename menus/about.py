from utils import mjson, ui

FILEPATH =  './config/about.json'

def run():
    file = mjson.load_json(FILEPATH)

    for name in file:
       ui.great_print(f"{name['name']} \n")
    input()
