from pkgs.tictactoe.ai.engine import AiEngine
from pkgs.tictactoe.game.move import InvalidMove, Move
from pkgs.tictactoe.game.player import Player, Symbol
from pkgs.tictactoe.game.rules import TicTacToeRules
from pkgs.tictactoe.game.tictactoe import Game


class GameManager:
    def __init__(self) -> None:
        self.player = Player(symbol=Symbol.X)
        self.winner = None
        self.winning_streak = None
        self.rules = TicTacToeRules()
        self.game = Game(self.rules)
        self.aiEngine = AiEngine()

    def precheck(self):
        if winner := self.rules.checkWinner(self.game.getState()):
            self.winner = winner
            return
        return True

    def makeMove(self, move: Move):
        if not self.rules.isValid(self.game.getState(), move):
            raise InvalidMove
        self.game.makeMove(self.player, move)
        self.player = self.player.flip()
        if not self.precheck():
            return

    def triggerAi(self):
        m = self.aiEngine.basicMove(self.game.getState())
        if m:
            self.makeMove(m)
