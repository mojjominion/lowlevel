from pkgs.tictactoe.game.board import Board
from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.player import Player
from pkgs.tictactoe.game.rules import TicTacToeRules


class Game:
    def __init__(self, rules: TicTacToeRules) -> None:
        self.board = Board()
        self.rules = rules

    def printBoard(self):
        out = ""
        for row in self.getState():
            out += ",".join(row)
            out += "\n"
        return print(out)

    def makeMove(self, player: Player, gmove: Move):
        self.board.makeMove(player, gmove)

    def getState(self):
        return self.board.state
