from typing import List, Sequence

from src.dice import Dice
from src.player import IPlayer
from src.tunnels import ITunnel


class Board:
    # size: int
    # players: List[IPlayer]
    # pipes: List[ITunnel]
    # dices: List[Dice]
    state: List[List[set[IPlayer]]]
    tunnelState: List[List[ITunnel | None]]

    def __init__(
        self, size: int, players: List[IPlayer] = [], pipes: List[ITunnel] = []
    ):
        self.size = size
        self.players = players
        self.pipes = pipes
        self.dices = []
        self.state = [[set() for _ in range(size)] for _ in range(size)]
        self.tunnelState = [[None for _ in range(size)] for _ in range(size)]

    def addPlayers(self, players: Sequence[IPlayer]):
        self.players.extend(players)
        for player in players:
            coords = player.getCoords()
            self.state[coords.row][coords.col].add(player)

    def getPlayers(self):
        return self.players

    def addDices(self, dices: List[Dice]):
        self.dices.extend(dices)

    def getDices(self):
        return self.dices

    def addPipes(self, pipes: List[ITunnel]):
        self.pipes.extend(pipes)
        for pipe in pipes:
            entry = pipe.getEntryCoords()
            self.tunnelState[entry.row][entry.col] = pipe

    def _initPipes(self):
        self.pipes = []
        self.tunnelState = [[None for _ in range(self.size)] for _ in range(self.size)]

    def getPipes(self):
        return self.pipes

    def printPlayers(self):
        for player in self.players:
            print(f"{player.name} : {player.coords}")

    def printBoard(self):
        for i, row in enumerate(self.state):
            for j, players in enumerate(row):
                lst = [p.name for p in players]
                pipe = self.tunnelState[i][j]
                if pipe:
                    lst += [pipe.name]
                print(lst, end="")
            print("\n")
