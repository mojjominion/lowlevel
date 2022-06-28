from collections import deque
from random import choices
from typing import List, Tuple
from src.point import Point
from utils.promt import get_promt_num


class Board:
    occupied: set[Tuple[int, int]]
    over: bool
    # 4 - left, 6 - right
    # 2 - bottom, 8 - top

    def __init__(self):
        self.size = 4
        self.state = [[None] * self.size for _ in range(self.size)]
        self.occupied = set()
        self.over = False
        self._initGame()

    def _initGame(self):
        c1, c2 = self._generateCoords()
        c3, c4 = self._generateCoords()
        c5, c6 = self._generateCoords()
        for p in [c1, c2, c3, c4, c5, c6]:
            self.state[p.row][p.col] = self._generateRandom(2)

    def _generateRandom(self, limit: int):
        if limit > 20:
            return 2048

        return 2 ** choices(range(1, limit))[-1]

    def _generateCoords(self) -> Tuple[Point, Point]:
        coords1, coords2 = self._generateRandomPair()
        while self._isCoordsInvalid(coords1, coords2):
            coords1, coords2 = self._generateRandomPair()

        return (Point(*coords1), Point(*coords2))

    def _generateRandomPair(self):
        coords1 = choices(range(self.size), k=2)
        coords2 = choices(range(self.size), k=2)
        return coords1, coords2

    def _isCoordsInvalid(self, c1: List[int], c2: List[int]):
        tc1, tc2 = tuple(c1), tuple(c2)

        if tc1 == tc2:
            return True
        if tc1 in self.occupied or tc2 in self.occupied:
            return True

        self.occupied.add(tc1)
        self.occupied.add(tc2)
        return False

    def printBoard(self):
        print(f"Board State")
        for row in self.state:
            for val in row:
                print(val if val else "-", end="  ")
            print("\n")

    def startGame(self):
        self.printBoard()
        while not self.over:
            self.present()

    def present(self):
        num = get_promt_num(
            "Enter Top[8] Right[6] Bottom[2] Left[4] : ", default_val=2)
        self.shift(num)
        self.printBoard()

    def shift(self, num: int):
        match num:
            case 8: self.top()
            case 6: self.right()
            case 2: self.bottom()
            case 4: self.left()

    def mergeColumn(self, col: int) -> List[int]:
        new_column = []
        for i in range(self.size):
            val = self.state[i][col]
            if not val:
                continue

            if new_column and new_column[-1] == val:
                new_column[-1] += val
            else:
                new_column.append(val)

        return new_column

    def mergeRow(self, row: int) -> List[int]:
        new_row = []
        for j in range(self.size):
            val = self.state[row][j]
            if not val:
                continue

            if new_row and new_row[-1] == val:
                new_row[-1] += val
            else:
                new_row.append(val)

        return new_row

    def top(self):
        for col in range(self.size):
            new_column = self.mergeColumn(col)
            for row in range(self.size):
                if row < len(new_column):
                    self.state[row][col] = new_column[row]
                    continue

                self.state[row][col] = None

    def bottom(self):
        for col in range(self.size):
            new_column = self.mergeColumn(col)
            for row in range(self.size):
                if row < len(new_column):
                    self.state[self.size - row - 1][col] = new_column[row]
                    continue

                self.state[self.size - row - 1][col] = None

    def right(self):
        for row in range(self.size):
            new_row = self.mergeRow(row)
            for col in range(self.size):
                if col < len(new_row):
                    self.state[row][self.size - col - 1] = new_row[col]
                    continue

                self.state[row][self.size - col - 1] = None

    def left(self):
        for row in range(self.size):
            new_row = self.mergeRow(row)
            for col in range(self.size):
                if col < len(new_row):
                    self.state[row][col] = new_row[col]
                    continue

                self.state[row][col] = None
