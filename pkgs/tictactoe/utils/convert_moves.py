from typing import List

from pkgs.tictactoe.game.move import Move


def coords_to_moves(coords: List[tuple[int, int]]):
    return [Move(x, y) for x, y in coords]
