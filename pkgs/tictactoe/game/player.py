from enum import Enum


class Symbol(Enum):
    X = 0
    O = 1  # noqa: E741

    def __str__(self) -> str:
        return self.name


class Player:
    def __init__(self, symbol: Symbol) -> None:
        self.symbol = symbol

    def get_symbol(self):
        return str(self.symbol)

    def flip(self):
        if self.symbol == Symbol.X:
            return Player(Symbol.O)
        return Player(Symbol.X)
