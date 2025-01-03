from abc import ABC, abstractmethod
from typing import Any, List, Optional

from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.rules import TicTacToeRules


class IAiEngine(ABC):
    @abstractmethod
    def basic_move(self, board: List[List[Any]]) -> Optional[Move]:
        return

    # @abstractmethod
    # def smart_move(self, board: List[List[Any]]) -> Optional[Move]:
    #     return


class AiEngine(IAiEngine):
    def __init__(self) -> None:
        self.rules = TicTacToeRules()

    def basic_move(self, board: List[List[Any]]):
        for i in range(3):
            for j in range(3):
                if self.rules.is_empty(board[i][j]):
                    return Move(row=i, col=j)
        return None

    def smart_move(self, board: List[List[Any]]):
        for i in range(3):
            for j in range(3):
                if self.rules.is_empty(board[i][j]):
                    return Move(row=i, col=j)
        return None
