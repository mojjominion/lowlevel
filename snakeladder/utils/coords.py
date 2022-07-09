from random import choices
from typing import List, Tuple

from src.data import Point


class CoordsUtil:
    def __init__(self, limit: int):
        self.size = limit
        self.occupied = set()

    def generateCoords(self) -> Tuple[Point, Point]:
        coords1, coords2 = self._generateRandomPair()
        while self._isCoordsInvalid(coords1, coords2):
            coords1, coords2 = self._generateRandomPair()

        return self._sortPair(coords1, coords2)

    def calculateCoords(self, pos: Point, num: int):
        next_num = self._coordsToNumber(pos) + num
        if next_num >= self.size * self.size:
            return pos

        row = next_num // self.size
        col = next_num % self.size

        return Point(row=row, col=col)

    def _coordsToNumber(self, pos: Point):
        return self.size * pos.row + pos.col

    def _sortPair(self, c1: List[int], c2: List[int]):
        sorted_coords = sorted([c1, c2])[::-1]
        return (Point(*sorted_coords[0]), Point(*sorted_coords[1]))

    def _generateRandomPair(self):
        coords1 = choices(range(self.size), k=2)
        coords2 = choices(range(self.size), k=2)
        return coords1, coords2

    def _isCoordsInvalid(self, c1: List[int], c2: List[int]):
        start, end = (0, 0), (self.size-1, self.size-1)
        tc1, tc2 = tuple(c1), tuple(c2)

        if tc1 == tc2:
            return True
        if tc1 in self.occupied or tc2 in self.occupied:
            return True
        if tc1 == start or tc2 == start:
            return True
        if tc1 == end or tc2 == end:
            return True

        self.occupied.add(tc1)
        self.occupied.add(tc2)
        return False
