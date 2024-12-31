from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.player import Player
from pkgs.tictactoe.game.rules import EMPTY


class Board:
    def __init__(self) -> None:
        self.state = [[EMPTY] * 3 for _ in range(3)]

    def makeMove(self, player: Player, gmove: Move):
        self.state[gmove.row][gmove.col] = player.getSymbol()
