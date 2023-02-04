from collections import namedtuple
from enum import Enum

Locator = namedtuple("Locator", "strategy selector")


class Currency(Enum):
    USD = "$"
    EUR = "€"
    GBP = "£"
