from typing import List
from utils.coords import CoordsUtil
from src.colors import bcolors
from src.player import IPlayer, IPlayer, Player
from src.board import Board
from src.data import Point
from src.dice import Dice
from src.tunnels import ITunnel, PipeFactory, PipeType


class Game:
    # size: int
    # numberOfDice: int
    # board: Board
    # over: bool
    # activePlayerIndex: int
    # winners: List[str]

    def __init__(self, board: Board, dice) -> None:
        self.board = board
        self.size = self.board.size
        self.activePlayerIndex = 0
        self.winners = []
        self.over = False
        self.numberOfDice = dice
        self.coordsUtil = CoordsUtil(board.size)

    def start(self):
        dices = self._generateDices()
        pipes = self._generatePipes()
        players = self._getRandomPlayers()

        self.board.addDices(dices)
        self.board.addPipes(pipes)
        self.board.addPlayers(players)
        self._printStats()
        self._startLoop()

    def _generateDices(self) -> List[ITunnel]:
        dices = [Dice(6) for _ in range(self.numberOfDice)]
        return dices

    def _generatePipes(self) -> List[ITunnel]:
        pipes = [p for p in self.generateSnakeLadderPair()
                 for _ in range(self.size)]
        return pipes

    def generateSnakeLadderPair(self):
        snake = PipeFactory.createPipe(
            PipeType.snake, self.coordsUtil.generateCoords())
        ladder = PipeFactory.createPipe(
            PipeType.ladder, self.coordsUtil.generateCoords())
        return [snake, ladder]

    def _getRandomPlayers(self):
        players = [Player("Josh"), Player("John"),
                   Player("Mike"), Player("Ross")]
        return players

    def _startLoop(self):
        while not self.over:
            play = input("\nDo you want to play [1]/0?:") or "1"
            if play.isnumeric() and int(play):
                self._nextMove()

        print(f"{bcolors.HEADER}Game Over!{bcolors.ENDC}")

    def _nextMove(self):
        # get player
        player = self._getActivePlayer()
        if not player:
            return

        # roll dice
        rolled_number = self._rollDice()
        coords = player.getCoords()

        # calculate new coords
        # add in winners in case player reached the end
        # use ladder or penalize player if they are on any pipe
        new_coords = self.coordsUtil.calculateCoords(coords, rolled_number)
        print(
            f"{bcolors.OKCYAN}{player.name} rolled dice with value {rolled_number}. Moving to new position {new_coords}{bcolors.ENDC}")

        # move player
        # set next active player
        # print Stats
        self.movePlayer(player, new_coords)
        self._setNextPlayer()
        self._printStats()

    def _getActivePlayer(self):
        if self.activePlayerIndex is None:
            return None

        return self.board.getPlayers()[self.activePlayerIndex]

    def _rollDice(self):
        total = sum([dice.roll() for dice in self.board.getDices()])
        return total

    def _getPipedCoords(self, player: IPlayer, coords: Point):
        tunnel = self.board.tunnelState[coords.row][coords.col]
        if tunnel is None:
            return coords

        entry = tunnel.getEntryCoords()
        if entry.col != coords.col or entry.row != coords.row:
            return coords

        new_point = tunnel.goto()
        print(
            f"\n{tunnel.color}{player.name} encountered a {tunnel.name}\nWill be going to new {new_point}{bcolors.ENDC}")
        return new_point

    def movePlayer(self, player: IPlayer, coords: Point):
        if self._isPointOutside(coords):
            return Exception("Out of bound")

        old_coords = player.getCoords()
        new_coords = self._getPipedCoords(player, coords)

        player.move(new_coords)
        if self._isWinner(new_coords):
            self._updateWinners(player)

        # move player from old_coords to new_coords
        self.board.state[old_coords.row][old_coords.col].remove(player)
        self.board.state[new_coords.row][new_coords.col].add(player)

    def _isWinner(self, p: Point):
        return p.row == self.size-1 and p.col == self.size-1

    def _updateWinners(self, activePlayer: IPlayer):
        self.winners.append(activePlayer.name)
        if len(self.winners) == len(self.board.getPlayers()):
            self.over = True

    def _isPointOutside(self, coords: Point):
        return max(coords.row, coords.col) >= self.size or min(coords.row, coords.col) < 0

    def _setNextPlayer(self):
        next_player_idx = self._getNextPlayerIndex()
        if next_player_idx is None:
            return

        self.activePlayerIndex = next_player_idx
        if next_player_idx >= len(self.board.getPlayers()):
            self.activePlayerIndex == None

        return self.activePlayerIndex

    def _printStats(self):
        players = self.board.getPlayers()
        for player in players:
            start = self._getPlayerColor(player)
            print(
                f"{start}{player.name} - {player.getCoords()}{bcolors.ENDC}")

        self._printRanks()
        player = self._getActivePlayer()
        if player:
            print(f"Active Player: {self._getActivePlayer().name}")

    def _getNextPlayerIndex(self):
        players = self.board.players
        if len(self.winners) == len(players):
            return None

        nxt = self.activePlayerIndex + 1
        nxt %= len(self.board.players)

        while players[nxt].name in self.winners:
            nxt += 1
            nxt %= len(self.board.players)

        return nxt

    def _getPlayerColor(self, player: IPlayer):
        winner = player.name in self.winners
        start_color = bcolors.OKGREEN if winner else bcolors.OKBLUE

        return start_color

    def _printRanks(self):
        if not self.winners:
            return

        print(f"{bcolors.HEADER}Ranks")
        for i, winner in enumerate(self.winners):
            print(f"{bcolors.HEADER}{winner} - {i+1}{bcolors.ENDC}")
