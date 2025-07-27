from copy import deepcopy
import enums


class Board:
    def __init__(self):
        self._init_board()
        pass 

    def _init_board(self):
        i = enums.CellValue.EMPTY.value
        self.board = [[i, i, i], [i, i, i], [i, i, i]]
    
    def get_board(self):
        return self.board_to_names()

    def board_to_names(self):
        name_board = deepcopy(self.board)
        for r in range(len(name_board)):
            for c in range(len(name_board[0])):
                name_board[r][c] = enums.CellValue(name_board[r][c]).name

        return name_board
    
    def print_board(self):
        b = self.board_to_names()
        board_layout = (b[0][0] + "|" + b[0][1] + "|" + b[0][2] + "\n" 
                        + b[1][0]  + "|" + b[1][1]  + "|" + b[1][2]  + "\n" 
                        + b[2][0] + "|" + b[2][1] + "|" + b[2][2])
        
        return board_layout

    def make_move(self, cell: tuple, value: enums.CellValue):
        self.board[cell[0]][cell[1]] = value.value

    def clear_board(self):
        self._init_board()

    def is_winner() -> bool: 
        """
        Returns True if there is win condition.
        Hard coded for 3x3 boards
        """

        return False
        