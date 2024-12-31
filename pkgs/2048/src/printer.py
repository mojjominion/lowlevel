from abc import ABC, abstractmethod
from typing import List
from utils.colors import bcolors
from utils.promt import get_promt_num


class IBoardPrinter(ABC):
    @abstractmethod
    def printState(self, boardState: List[List[int]]):
        pass

    @abstractmethod
    def gameOver(self):
        pass

    @abstractmethod
    def render(self):
        pass


class BoardPrinter(IBoardPrinter):
    def __init__(self) -> None:
        pass

    def printState(self, boardState: List[List[int]]):
        print(f"{bcolors.HEADER}Board State{bcolors.ENDC}")
        for row in boardState:
            for val in row:
                if val:
                    print(
                        f"{self.getColor(val)}{self.padString(str(val))}", end=" ")
                else:
                    print(f"{bcolors.FAIL}{self.padString('')}", end=" ")
            print(f"{bcolors.ENDC}\n")

    def gameOver(self):
        print(f"{bcolors.HEADER}{bcolors.BOLD}Game Over!!{bcolors.ENDC}")

    def render(self):
        num = get_promt_num(
            "Enter Top[8] Right[6] Bottom[2] Left[4] : ", default_val=8)
        return num

    def getColor(self, num: int):
        if num >= 1024:
            return bcolors.BOLD
        if num >= 512:
            return bcolors.WARNING
        if num >= 256:
            return bcolors.FAIL
        if num >= 128:
            return bcolors.OKBLUE
        if num >= 64:
            return bcolors.FAIL
        if num >= 32:
            return bcolors.OKCYAN
        if num >= 8:
            return bcolors.WARNING
        if num >= 4:
            return bcolors.FAIL

        return bcolors.OKCYAN

    def padString(self, s: str):
        diff = (8 - len(s))//2
        return "-" * diff + s + "-" * diff
