from menus import menu, info
from utils import actions, ui
import time, os

def ls(dirpath):
    show = os.listdir(dirpath)
    ui.index_list(show)

