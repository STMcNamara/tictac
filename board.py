import enums


class Board:
    def __init__(self):
        self._init_board()
        pass 

    def _init_board(self):
        i = enums.CellValue.EMPTY.name
        self.board = [[i, i, i], [i, i, i], [i, i, i]]   
        
    def get_board(self):
        return self.board
    
    def print_board(self):
        b = self.board
        board_layout = (b[0][0] + "|" + b[0][1] + "|" + b[0][2] + "\n" 
                        + b[1][0]  + "|" + b[1][1]  + "|" + b[1][2]  + "\n" 
                        + b[2][0] + "|" + b[2][1] + "|" + b[2][2])
        
        return board_layout

    def make_move(self, cell: tuple, value: enums.CellValue):
        self.board[cell[0]][cell[1]] = value.name

    def clear_board(self):
        self._init_board()
        