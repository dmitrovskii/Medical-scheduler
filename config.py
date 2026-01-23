import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
CONF = ROOT / 'config'

FILES = {
    "about": CONF / 'about_main.json',
    "info": CONF / 'info_main.json', 
    "menu": CONF / 'menu_main.json',
}

INFO = {
    'files': CONF / 'files_info.json',
    'strings': CONF / 'strings_info.json'
}