import argparse
from dataclasses import dataclass, asdict
from typing import List


parser = argparse.ArgumentParser(description='Program that teaches us args')
parser.add_argument('--mode', help='Program mode', type=str, default='list_view')


def list_view() -> None:
    """ Main function that shows records from file """
    print('Hello from list_view()')


def create_view() -> None:
    """ Takes input from user and adds record to the file """
    print('Hello from create_view()')


@dataclass
class HistoricalPeriod:
    name: str
    events: List[str]


def save_data(name: str, events: List[str]) -> None:
    """ Stores single Historical Period with at least one event """
    pass


def read_data() -> List[HistoricalPeriod]:
    """ Reads file reciords """
    pass


"""
[
{"name": "Three Kingdoms", "events": ["First event"]},
]
"""


if __name__ == '__main__':
    args = parser.parse_args()
    if args.mode == 'list_view':
        list_view()
    else:
        create_view()

