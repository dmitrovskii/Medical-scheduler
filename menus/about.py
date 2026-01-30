from utils import mjson, ui
from config import MAIN

def run():
   file = mjson.load(MAIN['about'])

   for name in file:
      ui.great_print(f"{name['name']}")
   input()
