from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple


class Locator(NamedTuple):
    strategy: str
    selector: str


class Currency(Enum):
    USD = "$"
    EUR = "€"
    GBP = "£"


@dataclass
class Person:
    firstname: str
    lastname: str
    email: str
    telephone: str
    password: str
    password_confirm: str
