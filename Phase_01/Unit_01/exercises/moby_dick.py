import re
from pprint import pprint
from typing import Dict, List


def with_comprehension(words: List[str]) -> List[str]:
    return [word.lower() for word in words]


def no_comprehension(words: List[str]) -> List[str]:
    lowered_words = []
    for word in words:
        lowered_words.append(word.lower())
    return lowered_words


def load_words_from_text(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)
    return [word.lower() for word in words]


def make_bag_of_words(words: List[str]) -> Dict[str, int]:
    bag_of_words = {}
    for word in words:
        if word not in bag_of_words:
            bag_of_words[word] = 0

        bag_of_words[word] += 1
    return bag_of_words


moby_dick_words = load_words_from_text('Data_MobyDick.txt')
bag_of_words = make_bag_of_words(moby_dick_words)

pprint(bag_of_words)