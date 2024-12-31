from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.manager import GameManager

if __name__ == "__main__":
    gm = GameManager()
    while gm.winner is None:
        row = int(input("row::"))
        col = int(input("col::"))
        gm.makeMove(Move(row=row, col=col))
        gm.triggerAi()
        gm.game.printBoard()
    print(f"{gm.winner.symbol} won the game!!")

import unittest


class TicTacToeTest(unittest.TestCase):
    def test_turns(self):
        gm = GameManager()
        hplayer = gm.player
        hsymbol = hplayer.getSymbol()
        gm.makeMove(Move(1, 1))
        self.assertEqual(gm.player.getSymbol(), hplayer.flip().getSymbol())
        self.assertEqual(gm.game.getState()[1][1], hsymbol)
        gm.triggerAi()
        self.assertEqual(gm.player.getSymbol(), hplayer.getSymbol())
        gm.makeMove(Move(2, 2))
        self.assertEqual(gm.game.getState()[2][2], hsymbol)
