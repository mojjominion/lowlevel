from typing import Any, List

from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.rules import TicTacToeRules


class AiEngine:
    def __init__(self) -> None:
        self.rules = TicTacToeRules()

    def basicMove(self, board: List[List[Any]]):
        for i in range(3):
            for j in range(3):
                if self.rules.isEmpty(board[i][j]):
                    return Move(row=i, col=j)
