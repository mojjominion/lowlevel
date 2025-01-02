from pkgs.tictactoe.ai.engine import IAiEngine
from pkgs.tictactoe.game.move import InvalidMove, Move
from pkgs.tictactoe.game.player import Player, Symbol
from pkgs.tictactoe.game.rules import TicTacToeRules
from pkgs.tictactoe.game.tictactoe import Game


class GameManager:
    def __init__(self, ai_engine: IAiEngine) -> None:
        self.player = Player(symbol=Symbol.X)
        self.winner = None
        self.winning_streak = None
        self.rules = TicTacToeRules()
        self.game = Game(self.rules)
        self.ai_engine = ai_engine

    def pre_check(self):
        if winner := self.rules.check_winner(self.game.get_state()):
            self.winner = winner
            return
        return True

    def make_move(self, move: Move):
        if not self.pre_check():
            # self.game.printBoard()
            return InvalidMove
        if not self.rules.is_valid(self.game.get_state(), move):
            raise InvalidMove
        self.game.make_move(self.player, move)
        self.player = self.player.flip()

    def trigger_ai(self):
        m = self.ai_engine.basic_move(self.game.get_state())
        if m:
            self.make_move(m)
