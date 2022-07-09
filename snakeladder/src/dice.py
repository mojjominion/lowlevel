
from random import choices


class Dice:
    limit: int

    def __init__(self, limit: int) -> None:
        self.limit = limit

    def roll(self) -> int:
        return choices(range(self.limit))[-1]
