class Tile:
    def __init__(self, tile_color):
        self.color = tile_color
        self.up_status = 0 #0 for unknown, -1 for no, 1 for yes
        self.right_status = 0
        self.down_status = 0
        self.left_status = 0
        self.solved = False
    def print(self):
        print(self.color)

class Board:
    def __init__(self, colors):
        self.board = [[0 for x in range(len(colors[0]))] for y in range(len(colors))]
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                self.board[i][j] = Tile(colors[i][j])
    def print(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].print()

colors = [['E','E','E','E','E','E','E','E','E','E',],\
['W','E','W','E','E','W','B','E','B','W',],\
['E','W','E','E','E','E','W','E','W','E',],\
['E','E','E','B','E','W','E','E','E','E',],\
['E','W','E','E','E','B','E','E','E','B',],\
['E','B','E','E','E','W','E','E','E','E',],\
['W','E','E','E','E','E','W','E','E','B',],\
['B','W','W','E','W','E','W','E','E','W',],\
['E','E','W','W','B','W','E','E','E','E',],\
['E','E','E','E','E','B','E','B','W','B',]]

board = Board(colors)


