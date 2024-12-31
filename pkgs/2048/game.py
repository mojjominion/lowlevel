from src.board import Board
from src.printer import BoardPrinter

if __name__ == "__main__":
    printer = BoardPrinter()
    board = Board(printer)
    board.startGame()
