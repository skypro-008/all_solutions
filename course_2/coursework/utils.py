import requests
import json
from random import randint

from classes.basic_word import BasicWord

def load_random_word():
    raw_json = requests.get("https://jsonkeeper.com/b/HD8I")
    random_number = randint(0, 2)
    well_json = json.loads(raw_json.text)
    word = well_json[random_number]["word"]
    subwords = well_json[random_number]["subwords"]
    return BasicWord(word, subwords)
