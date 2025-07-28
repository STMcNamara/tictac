import unittest
import board
import enums
from board import Board

class BoardTests(unittest.TestCase):

    def test_create(self):
        # Set up
        expected_new_board = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        tb = Board()

        # Act
        res = tb.get_board()
        
        # Assert
        self.assertEqual(res, expected_new_board)

    def test_print_board(self):
        # Set up
        expected_new_board_printed = "EMPTY|EMPTY|EMPTY\nEMPTY|EMPTY|EMPTY\nEMPTY|EMPTY|EMPTY"
        tb = Board()

        #Act
        res = tb.print_board()

        # Assert
        self.assertEqual(res, expected_new_board_printed)

    def test_make_moves(self):
        # Set up
        expected_new_board = [['X', 'EMPTY', 'O'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'EMPTY', 'O']]
        tb = Board()

        # Act
        tb.make_move(cell=(0,0), value=enums.CellValue.X)
        tb.make_move(cell=(0,2), value=enums.CellValue.O)
        tb.make_move(cell=(1,1), value=enums.CellValue.X)
        tb.make_move(cell=(2,2), value=enums.CellValue.O)

        res = tb.get_board()

        # Asset
        self.assertEqual(res, expected_new_board)

    def test_clear_board(self):
        # Set up
        expected_new_board = [['X', 'EMPTY', 'O'], ['EMPTY', 'X', 'EMPTY'], ['EMPTY', 'EMPTY', 'O']]
        expected_cleared_board = [['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY'], ['EMPTY', 'EMPTY', 'EMPTY']]
        tb = Board()

        # Act
        tb.make_move(cell=(0,0), value=enums.CellValue.X)
        tb.make_move(cell=(0,2), value=enums.CellValue.O)
        tb.make_move(cell=(1,1), value=enums.CellValue.X)
        tb.make_move(cell=(2,2), value=enums.CellValue.O)

        res = tb.get_board()
        # Confrim changes made
        self.assertEqual(res, expected_new_board)

        # Wipe the board
        tb.clear_board()
        res2 = tb.get_board()

        # Asset
        self.assertEqual(res2, expected_cleared_board)

    def test_win_conditions(self):
        # Set up
        winning_boards = [[[-1, -1, -1], [0, 0, 0], [0, 0, 0]],
                          [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
                          [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
                          [[-1, 0, 1], [1, -1, -1], [0, 0, -1]],
                          [[0, 0, 1], [0, 1, 1], [1, 0, 1]]]
        
        ongoing_boards = [[[-1, -1, 1], [0, 0, 0], [0, 0, 0]],
                          [[0, 0, 0], [1, -1, 1], [0, 0, 0]],
                          [[0, 0, 1], [0, 0, 1], [0, 0, -1]],
                          [[1, 0, 1], [1, -1, -1], [0, 0, -1]],
                          [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        
        # Winning conditions
        for win in winning_boards:
            # Set up

            tb = Board()
            tb.board = win
            res = tb.is_winner()

            self.assertTrue(res)

        for no_win in ongoing_boards:
            tb = Board()
            tb.board = no_win
            res = tb.is_winner()

            self.assertFalse(res)
            pass




        