from utils import mjson, ui
from config import FILES

def run():
   file = mjson.load_json(FILES['about'])

   for name in file:
      ui.great_print(f"{name['name']} \n")
   input()
