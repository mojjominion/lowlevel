from typing import Any, List

from pkgs.tictactoe.ai.engine import AiEngine, IAiEngine
from pkgs.tictactoe.game.move import Move
from pkgs.tictactoe.game.rules import TicTacToeRules
from pkgs.tictactoe.manager import GameManager
from pkgs.tictactoe.utils.convert_moves import coords_to_moves

if __name__ == "__main__":
    gm = GameManager(AiEngine())
    while gm.winner is None:
        row = int(input("row::"))
        col = int(input("col::"))
        gm.makeMove(Move(row=row, col=col))
        gm.triggerAi()
        gm.game.printBoard()
    print(f"{gm.winner.symbol} won the game!!")

import unittest


class TestAiEngine(IAiEngine):
    def __init__(self, moves: List[Move]) -> None:
        self.rules = TicTacToeRules()
        self.moves = moves
        self.index = 0

    def basicMove(self, board: List[List[Any]]):
        res = self.moves[self.index]
        self.index += 1
        return res


class TicTacToeTest(unittest.TestCase):
    def test_turns(self):
        gm = GameManager(AiEngine())
        hplayer = gm.player
        hsymbol = hplayer.getSymbol()
        gm.makeMove(Move(1, 1))
        self.assertEqual(gm.player.getSymbol(), hplayer.flip().getSymbol())
        self.assertEqual(gm.game.getState()[1][1], hsymbol)
        gm.triggerAi()
        self.assertEqual(gm.player.getSymbol(), hplayer.getSymbol())
        gm.makeMove(Move(2, 2))
        self.assertEqual(gm.game.getState()[2][2], hsymbol)

    def test_first_row_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(2, 0), (2, 1), (2, 2)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 0), (0, 1), (0, 2)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_second_row_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(2, 0), (2, 1), (2, 2)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(1, 0), (1, 1), (1, 2)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_third_row_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(0, 0), (0, 1), (0, 2)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(2, 0), (2, 1), (2, 2)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_first_col_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(0, 1), (1, 1), (2, 1)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 0), (1, 0), (2, 0)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_second_col_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(0, 0), (1, 0), (2, 0)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 1), (1, 1), (2, 1)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_third_col_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(0, 0), (1, 0), (2, 0)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 2), (1, 2), (2, 2)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_diag_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(0, 1), (1, 0), (2, 0)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 0), (1, 1), (2, 2)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())

    def test_rdiag_win(self):
        aiEngine = TestAiEngine(coords_to_moves([(0, 1), (1, 0), (2, 0)]))
        gm = GameManager(aiEngine)
        hplayer = gm.player
        for m in coords_to_moves([(2, 0), (1, 1), (0, 2)]):
            gm.makeMove(m)
            gm.triggerAi()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.getSymbol(), hplayer.getSymbol())
