import pathlib

ROOT = pathlib.Path(__file__).resolve().parent

FILES = {
    "about": ROOT / 'config' / 'about.json',
    "info": ROOT / 'config' / 'info_m.json', 
    "menu": ROOT / 'config' / 'menu_m.json'
}
