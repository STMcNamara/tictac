from board import Board
import enums

tb = Board()

# Act
tb.make_move(cell=(0,0), value=enums.CellValue.X)
tb.make_move(cell=(0,2), value=enums.CellValue.O)
tb.make_move(cell=(1,1), value=enums.CellValue.X)
tb.make_move(cell=(2,2), value=enums.CellValue.O)

res = tb.get_board()
# Confrim changes made
print(res)

# Wipe the board
res = tb.clear_board()

# Asset
print(res)