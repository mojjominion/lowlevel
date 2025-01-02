from pkgs.tictactoe.game.board import Board
from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.player import Player
from pkgs.tictactoe.game.rules import TicTacToeRules


class Game:
    def __init__(self, rules: TicTacToeRules) -> None:
        self.board = Board()
        self.rules = rules

    def print_board(self):
        out = ""
        for row in self.get_state():
            out += ",".join(row)
            out += "\n"
        print("\nBoard State:::")
        print(out)

    def make_move(self, player: Player, gmove: Move):
        self.board.make_move(player, gmove)

    def get_state(self):
        return self.board.state
