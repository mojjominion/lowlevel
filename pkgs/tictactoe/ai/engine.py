
from tictactoe.game.rules import TicTacToeRules
from typing import List, Any
from tictactoe.game.move import Move

class AiEngine:

    def __init__(self) -> None:
        self.rules = TicTacToeRules()

    def basicMove(self, board: List[List[Any]]):
        for i in range(3):
            for j in range(3):
                if self.rules.isEmpty(board[i][j]):
                    return Move(row=i, col=j)
