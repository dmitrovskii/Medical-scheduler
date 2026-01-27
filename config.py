import pathlib

ROOT = pathlib.Path(__file__).resolve().parent

DATA = ROOT / 'data'

PATH_MAIN = ROOT / 'config' / 'main'
PATH_INFO = ROOT / 'config' / 'info'

MAIN = {
    'about': PATH_MAIN / 'about_main.json',
    'info': PATH_MAIN / 'info_main.json', 
    'menu': PATH_MAIN / 'menu_main.json'
}

INFO = {
    'files': PATH_INFO / 'files_info.json',
    'strings': PATH_INFO / 'strings_info.json'
}