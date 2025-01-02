from typing import Any, List, Optional

from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.player import Player

EMPTY = "-"


class TicTacToeRules:
    def is_empty(self, value: str) -> bool:
        return value == EMPTY

    def is_valid(self, board: List[List[Any]], move: Move) -> bool:
        if move.row < 0 or move.col < 0:
            return False
        if move.row >= 3 or move.col >= 3:
            return False
        return self.is_empty(board[move.row][move.col])

    def check_diag(self, board: List[List[Any]], diag: List[tuple[int, int]]):
        st = set()
        for x, y in diag:
            st.add(board[x][y])
        if len(st) == 1 and not self.is_empty(symbol := st.pop()):
            return Player(symbol)
        return None

    def check_winner(self, board: List[List[Any]]) -> Optional[Player]:
        for row in board:
            if not self.is_empty(row[0]) and len(set(row)) == 1:
                return Player(row[0])

        for i in range(len(board)):
            st = set()
            for j in range(len(board[0])):
                st.add(board[j][i])
            if len(st) == 1 and not self.is_empty(symbol := st.pop()):
                return Player(symbol)

        diag = [(0, 0), (1, 1), (2, 2)]
        rdiag = [(0, 2), (1, 1), (2, 0)]

        for d in [diag, rdiag]:
            if res := self.check_diag(board, d):
                return res

        return None
