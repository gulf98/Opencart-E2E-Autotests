from enum import Enum
from typing import NamedTuple


class Locator(NamedTuple):
    strategy: str
    selector: str


class Currency(Enum):
    USD = "$"
    EUR = "€"
    GBP = "£"
