
from tictactoe.game.move import Move
from tictactoe.game.rules import TicTacToeRules
from tictactoe.game.player import  Player
from tictactoe.game.board import Board

class Game:

    def __init__(self, rules: TicTacToeRules) -> None:
        self.board = Board()
        self.rules = rules

    def printBoard(self):
        out = ""
        for row in self.getState():
            out += ",".join(row)
            out += '\n'
        return print(out)

    def makeMove(self,player:Player, gmove: Move):
        self.board.makeMove(player, gmove)

    def getState(self):
        return self.board.state
