import unittest
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
        gm.make_move(Move(row=row, col=col))
        gm.trigger_ai()
        gm.game.board.print_board()
    print(f"{gm.winner.symbol} won the game!!")


class TestAiEngine(IAiEngine):
    def __init__(self, moves: List[Move]) -> None:
        self.rules = TicTacToeRules()
        self.moves = moves
        self.index = 0

    def basic_move(self, board: List[List[Any]]):
        res = self.moves[self.index]
        self.index += 1
        return res


class TicTacToeTest(unittest.TestCase):
    def test_turns(self):
        gm = GameManager(AiEngine())
        hplayer = gm.player
        hsymbol = hplayer.get_symbol()
        gm.make_move(Move(1, 1))
        self.assertEqual(gm.player.get_symbol(), hplayer.flip().get_symbol())
        self.assertEqual(gm.game.get_state()[1][1], hsymbol)
        gm.trigger_ai()
        self.assertEqual(gm.player.get_symbol(), hplayer.get_symbol())
        gm.make_move(Move(2, 2))
        self.assertEqual(gm.game.get_state()[2][2], hsymbol)

    def test_first_row_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(2, 0), (2, 1), (2, 2)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 0), (0, 1), (0, 2)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_second_row_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(2, 0), (2, 1), (2, 2)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(1, 0), (1, 1), (1, 2)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_third_row_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(0, 0), (0, 1), (0, 2)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(2, 0), (2, 1), (2, 2)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_first_col_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(0, 1), (1, 1), (2, 1)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 0), (1, 0), (2, 0)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_second_col_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(0, 0), (1, 0), (2, 0)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 1), (1, 1), (2, 1)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_third_col_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(0, 0), (1, 0), (2, 0)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 2), (1, 2), (2, 2)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_diag_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(0, 1), (1, 0), (2, 0)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(0, 0), (1, 1), (2, 2)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())

    def test_rdiag_win(self):
        ai_engine = TestAiEngine(coords_to_moves([(0, 1), (1, 0), (2, 0)]))
        gm = GameManager(ai_engine)
        hplayer = gm.player
        for m in coords_to_moves([(2, 0), (1, 1), (0, 2)]):
            gm.make_move(m)
            gm.trigger_ai()
        self.assertIsNotNone(gm.winner)
        if gm.winner:
            self.assertEqual(gm.winner.get_symbol(), hplayer.get_symbol())
