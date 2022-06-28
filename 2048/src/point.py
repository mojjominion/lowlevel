
from dataclasses import dataclass


@dataclass()
class Point:
    row: int
    col: int

    def __eq__(self, other: 'Point') -> bool:
        return self.row == other.row and self.col == other.col
