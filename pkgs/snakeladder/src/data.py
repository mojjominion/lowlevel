from dataclasses import dataclass


@dataclass()
class Point:
    row: int
    col: int

    def __eq__(self, other: object):
        if not isinstance(other, Point):
            return NotImplemented

        return self.row == other.row and self.col == other.col


@dataclass()
class Move:
    start: Point
    end: Point
