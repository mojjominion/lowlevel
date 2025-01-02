from pkgs.tictactoe.game.board import Board
from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.player import Player
from pkgs.tictactoe.game.rules import TicTacToeRules


class Game:
    def __init__(self, rules: TicTacToeRules) -> None:
        self.board = Board()
        self.rules = rules

    def make_move(self, player: Player, gmove: Move):
        self.board.make_move(player, gmove)

    def get_state(self):
        return self.board.state
