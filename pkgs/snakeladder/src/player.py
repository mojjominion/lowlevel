
from src.data import Point, Move
from abc import ABC, abstractmethod
from typing import List


class IPlayer(ABC):
    id: str
    name: str
    coords: Point
    moves: List[Move]

    @abstractmethod
    def getMoves():
        pass

    @abstractmethod
    def getCoords() -> Point:
        pass

    @abstractmethod
    def move(self, new_coords: Point) -> Point:
        pass


class Player(IPlayer):
    def __init__(self, name: str, coords: Point = Point(0, 0), moves: List[Move] = []):
        self.name = name
        self.coords = coords
        self.moves = moves

    def getMoves(self):
        return self.moves

    def getCoords(self):
        return self.coords

    def move(self, coords: Point):
        self.coords = coords
        return self.coords

    def __repr__(self) -> str:
        return f"{self.name} - {self.getCoords()}"
