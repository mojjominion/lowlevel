from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.player import Player
from pkgs.tictactoe.game.rules import EMPTY


class Board:
    def __init__(self) -> None:
        self.state = [[EMPTY] * 3 for _ in range(3)]

    def make_move(self, player: Player, gmove: Move):
        self.state[gmove.row][gmove.col] = player.get_symbol()

    def print_board(self):
        out = ""
        for row in self.state:
            out += ",".join(row)
            out += "\n"
        print("\nBoard State:::")
        print(out)
