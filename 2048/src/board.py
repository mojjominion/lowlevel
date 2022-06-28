from math import log
from random import choices
from typing import List
from src.point import Point
from utils.promt import get_promt_num
from src.printer import IBoardPrinter


class Board:
    over: bool
    max_num: int
    # 4 - left,   6 - right
    # 2 - bottom, 8 - top

    def __init__(self, printer: IBoardPrinter):
        self.size = 4
        self.state = [[0] * self.size for _ in range(self.size)]
        self.over = False
        self.max_num = 2
        self.printer = printer
        self._populateNumbers()

    def getState(self):
        return self.state

    def _populateNumbers(self, limit: int = 2):
        for _ in range(limit):
            p = self._generateCoords()
            self.state[p.row][p.col] = self._generateRandomPowerOfTwo()

        self.over = True
        for row in self.state:
            filled = all(row)
            if not filled:
                self.over = False

    def _generateRandomPowerOfTwo(self) -> int:
        return 2 ** choices(range(1, self.max_num))[-1]

    def _generateCoords(self) -> Point:
        coord = self._generateRandomCoord()
        while self._isCoordsInvalid(coord):
            coord = self._generateRandomCoord()

        return Point(*coord)

    def _generateRandomCoord(self) -> List[int]:
        return choices(range(self.size), k=2)

    def _isCoordsInvalid(self, c1: List[int]):
        i, j = c1
        if self.state[i][j]:
            return True

        return False

    def startGame(self):
        state = self.getState()
        self.printer.printState(state)
        while not self.over:
            self.present()
        self.printer.gameOver()

    def present(self):
        num = get_promt_num(
            "Enter Top[8] Right[6] Bottom[2] Left[4] : ", default_val=2)
        self.shift(num)
        self._populateNumbers(1)
        self.printer.printState(self.getState())

    def shift(self, num: int):
        match num:
            case 8: self.top()
            case 6: self.moveRight()
            case 2: self.bottom()
            case 4: self.moveLeft()

    def _slideLeft(self, row: int) -> List[int]:
        non_zero = [val for val in self.state[row] if val]
        updated_row = []
        for val in non_zero:
            if updated_row and updated_row[-1] == val:
                updated_row[-1] *= -2
                # capping for generating future numbers
                power = int(log(abs(updated_row[-1]), 2))
                self.max_num = max(self.max_num, power)

            else:
                updated_row.append(val)

        # get remaining cells number
        # append remaining cells with '0'
        remaining_cells = self.size - len(updated_row)
        updated_row += [0] * remaining_cells
        updated_row = [abs(x) for x in updated_row]

        # update row
        self.state[row] = updated_row

    def _transpose(self):
        """
        Transpose matrix
        ```
        input:
                [1, 2]   
                [3, 4]   
        output:
                [1, 3]
                [2, 4]
        ```
        """
        self.state = list([list(x) for x in zip(*self.state)])

    def _reverse_rows(self):
        """
        Reverses matrix rows
        ```
        [1, 2]   [2, 1]
        [3, 4]   [4, 3]
        ```
        """
        for i, row in enumerate(self.state):
            self.state[i] = row[::-1]

    def moveLeft(self):
        for i in range(self.size):
            self._slideLeft(i)

    def moveRight(self):
        self._reverse_rows()
        self.moveLeft()
        self._reverse_rows()

    def top(self):
        self._transpose()
        self.moveLeft()
        self._transpose()

    def bottom(self):
        self._transpose()
        self.moveRight()
        self._transpose()
