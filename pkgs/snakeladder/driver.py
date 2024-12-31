
from utils.promt import get_promt_num
from src.game import Board, Game


if __name__ == "__main__":
    size = get_promt_num("Enter Size of board: ", default_val=10)
    dice = get_promt_num("Enter Number of dices: ", default_val=3)

    board = Board(size)
    game = Game(board, dice)
    game.start()
