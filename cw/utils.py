import random

import requests

# https://jsonkeeper.com/b/99JK
from cw.classes.BasicWord import BasicWord


def load_words_from_jsonkeeper(path):
    result = requests.get(path)
    data = result.json()
    return data


def get_random_word(path):
    data = load_words_from_jsonkeeper(path)
    word_data = random.choice(data)
    word = BasicWord(word_data["word"], word_data["subwords"])
    return word
