from tictactoe.game.move import Move
from tictactoe.game.rules import  EMPTY
from tictactoe.game.player import  Player


class Board:
    def __init__(self) -> None:
        self.state = [[EMPTY] * 3 for _ in range(3)]

    def makeMove(self, player:Player, gmove: Move):
        self.state[gmove.row][gmove.col] = player.getSymbol()
