
from src.colors import bcolors
from src.data import Point
from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple


class PipeType(Enum):
    snake = 1
    ladder = 2


class ITunnel(ABC):
    id: str
    name: str | None
    tail_name: str | None
    color: str

    @abstractmethod
    def goto() -> Point:
        pass

    @abstractmethod
    def getEntryCoords() -> Point:
        pass


class Snake(ITunnel):
    head: Point
    tail: Point

    def __init__(self, head: Point, tail: Point, name=None, tail_name=None, color=bcolors.FAIL):
        self.head = head
        self.tail = tail
        self.name = name
        self.tail_name = tail_name
        self.color = color

    def goto(self):
        return self.tail

    def getEntryCoords(self):
        return self.head


class Ladder(ITunnel):
    high: Point
    low: Point

    def __init__(self, high: Point, low: Point, name=None, tail_name=None, color=bcolors.WARNING):
        self.high = high
        self.low = low
        self.name = name
        self.tail_name = tail_name
        self.color = color

    def goto(self):
        return self.high

    def getEntryCoords(self):
        return self.low


class PipeFactory:

    @staticmethod
    def createPipe(type: PipeType, coords_pair: Tuple[Point, Point]) -> ITunnel:
        coords1, coords2 = coords_pair
        match type:
            case PipeType.ladder:
                return Ladder(coords1, coords2, name=f"ladder{coords2.row}_{coords2.col}", tail_name=f"#{coords1.row}_{coords1.col}")
            case PipeType.snake:
                return Snake(coords1, coords2, name=f"Snake{coords1.row}_{coords1.col}", tail_name=f"S{coords2.row}_{coords2.col}")
