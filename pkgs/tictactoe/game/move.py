from dataclasses import dataclass

class InvalidMove(Exception):
    def __repr__(self) -> str:
        return "Invalid move"

@dataclass()
class Move:
    row: int
    col: int
