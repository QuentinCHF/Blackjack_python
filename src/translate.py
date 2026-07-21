## Importing libraries
import configparser
import importlib

config = configparser.ConfigParser()
config.read("config.ini")

LANG = config["General"]["language"]

if LANG != "en":
    language = importlib.import_module(f"src.lang.{LANG}")
    
def translate(key):
    if LANG == "en":
        return key

    if key not in language.translation:
        print(f"[WARNING] Missing translation: '{key}'")
        return key

    return language.translation[key]
