import unittest
from src.board import Board
from src.data import Point
from src.game import Game
from src.player import Player


class BoardStateTests(unittest.TestCase):
    def setUp(self):
        self.size = 15
        self.dice = 2
        self.board = Board(self.size)
        self.game = Game(self.board, self.dice)
        self.start = Point(0, 0)
        self.end = Point(self.size-1, self.size-1)

    def test_ladder_effect(self):
        for _ in range(5):  # 225 cells - 20 * 10 = 200 pipe points
            self.board.addPipes(self.game._generatePipes())
            state = self.board.tunnelState

            self.assertIsNone(state[0][0], "Start point is not empty")
            self.assertIsNone(state[-1][-1], "End point is not empty")

            self.game.occupied = set()
            self.board._initPipes()

    def test_ladder_effect(self):
        _, ladder = self.game.generateSnakeLadderPair()

        player = Player("Test_Player", self.start)
        self.board.addPipes([ladder])
        self.board.addPlayers([player])
        self.game.movePlayer(player, ladder.getEntryCoords())

        top, coords = ladder.goto(),  player.getCoords()
        player_at_old_position = player in self.board.state[self.start.row][self.start.col]
        player_at_new_position = player in self.board.state[top.row][top.col]

        self.assertEqual(coords, top, "Player didn't follow the ladder")
        self.assertFalse(player_at_old_position,
                         "Player is still at old position")
        self.assertTrue(player_at_new_position,
                        "Player has not reached new position")

    def test_snake_effect(self):
        snake, _ = self.game.generateSnakeLadderPair()

        player = Player("Test_Player", self.start)
        self.board.addPipes([snake])
        self.board.addPlayers([player])
        self.game.movePlayer(player, snake.getEntryCoords())

        tail, coords = snake.goto(), player.getCoords()
        player_at_old_position = player in self.board.state[self.start.row][self.start.col]
        player_at_new_position = player in self.board.state[tail.row][tail.col]

        self.assertEqual(coords, tail, "Player didn't follow the snake")
        self.assertFalse(player_at_old_position,
                         "Player is still at old position")
        self.assertTrue(player_at_new_position,
                        "Player has not reached new position")

    def test_winner_effect(self):
        player = Player("Test_Player", self.start)
        self.board.addPlayers([player])
        self.game.movePlayer(player, self.end)

        self.assertTrue(self.game._isWinner(player.getCoords()),
                        f"{player.name} has not reached end")
        self.assertTrue(player.name in self.game.winners,
                        f"{player.name} is not in winners")

    def test_coinciding_tunnels(self):
        for _ in range(5):  # 225 cells - 20 * 10 = 200 pipe points
            self.board.addPipes(self.game._generatePipes())
            state = self.board.tunnelState

            self.assertIsNone(state[0][0], "Start point is not empty")
            self.assertIsNone(state[-1][-1], "End point is not empty")

            self.game.occupied = set()
            self.board._initPipes()
