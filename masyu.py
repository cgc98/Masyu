class Tile:
    def __init__(self, tile_color):
        self.color = tile_color
        self.up_status = 0 #0 for unknown, -1 for no, 1 for yes
        self.right_status = 0
        self.down_status = 0
        self.left_status = 0
        self.solved = False
 
def convert_status_to_char(status):
    if status == 0:
        return "?"
    elif status == -1:
        return "N"
    return "Y"

class Board:
    def __init__(self, colors):
        self.board = [[0 for x in range(len(colors[0]))] for y in range(len(colors))]
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                self.board[i][j] = Tile(colors[i][j])
    def print(self):
        for i in range((len(self.board))-1):
            string = ""
            for j in range((len(self.board[i]))-1):
                string += self.board[i][j].color + " "
                string += convert_status_to_char(self.board[i][j].right_status) + " "
            string += self.board[i][len(self.board)-1].color
            print(string)
            string_two = ""
            for j in range((len(self.board[i]))-1):
                string_two += convert_status_to_char(self.board[i][j].down_status) + "   "
            string_two += convert_status_to_char(self.board[i][len(self.board)-1].down_status)
            print(string_two)
        string = ""
        for j in range((len(self.board[(len(self.board))-1]))-1):
            string += self.board[(len(self.board))-1][j].color + " "
            string += convert_status_to_char(self.board[(len(self.board))-1][j].right_status) + " "
        string += self.board[(len(self.board))-1][len(self.board)-1].color
        print(string)
        

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
board.print()


