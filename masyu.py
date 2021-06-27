class Tile:
    def __init__(self, x_coord, y_coord, tile_color):
        self.x = x_coord
        self.y = y_coord
        self.color = tile_color
        self.up_status = 0 #0 for unknown, -1 for no, 1 for yes
        self.right_status = 0
        self.down_status = 0
        self.left_status = 0
        self.solved = False
    def get_number_n(self): #
        count = 0
        if self.up_status == -1:
            count += 1
        if self.right_status == -1:
            count += 1
        if self.down_status == -1:
            count += 1
        if self.left_status == -1:
            count += 1   
        return count
    def get_number_y(self):
        count = 0
        if self.up_status == 1:
            count += 1
        if self.right_status == 1:
            count += 1
        if self.down_status == 1:
            count += 1
        if self.left_status == 1:
            count += 1   
        return count
    def print(self):
        print(self.up_status)
        print(self.right_status)
        print(self.down_status)
        print(self.left_status)
        print(self.solved)

 
def convert_status_to_char(status):
    if status == 0:
        return "?"
    elif status == -1:
        return "n"
    return "y"


class Board:
    def __init__(self, colors):
        self.board = [[0 for x in range(len(colors[0]))] for y in range(len(colors))]
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                self.board[i][j] = Tile(i, j, colors[i][j])
                if i == 0:
                    self.board[i][j].up_status = -1
                if i == (len(colors)-1):
                    self.board[i][j].down_status = -1
                if j == 0:
                    self.board[i][j].left_status = -1
                if j == (len(colors)-1):
                    self.board[i][j].right_status = -1
    def print(self):
        for i in range((len(self.board))-1):
            string = ""
            for j in range((len(self.board[i]))-1):
                string += self.board[i][j].color + " "
                string += convert_status_to_char(self.board[i][j].right_status) + " "
            string += self.board[i][(len(self.board[i]))-1].color
            print(string)
            string_two = ""
            for j in range((len(self.board[i]))-1):
                string_two += convert_status_to_char(self.board[i][j].down_status) + "   "
            string_two += convert_status_to_char(self.board[i][(len(self.board[i]))-1].down_status)
            print(string_two)
        string = ""
        for j in range((len(self.board[(len(self.board))-1]))-1):
            string += self.board[(len(self.board))-1][j].color + " "
            string += convert_status_to_char(self.board[(len(self.board))-1][j].right_status) + " "
        string += self.board[(len(self.board))-1][(len(self.board[(len(self.board))-1]))-1].color
        print(string)


def solve_empty_tile(board, tile):
    #If already solved, set to solved
    if tile.get_number_n() + tile.get_number_y() == 4:
        tile.solved = True
    #If 3 are blocked, all statuses are -1
    elif tile.get_number_n() >= 3:
        if tile.up_status == 0:
            tile.up_status = -1
        elif tile.right_status == 0:
            tile.right_status = -1
        elif tile.down_status == 0:
            tile.down_status = -1
        elif tile.left_status == 0:
            tile.left_status = -1
        tile.solved = True
    #If two are yes, the rest are no
    elif tile.get_number_y() == 2:
        if tile.up_status == 0:
            tile.up_status = -1
        if tile.right_status == 0:
            tile.right_status = -1
        if tile.down_status == 0:
            tile.down_status = -1
        if tile.left_status == 0:
            tile.left_status = -1
        tile.solved = True
    #If two are no and one is yes, the other is yes
    elif (tile.get_number_n() == 2) and (tile.get_number_y() == 1):
        if tile.up_status == 0:
            tile.up_status = 1
        elif tile.right_status == 0:
            tile.right_status = 1
        elif tile.down_status == 0:
            tile.down_status = 1
        elif tile.left_status == 0:
            tile.left_status = 1
        tile.solved = True


def solve_white_tile(board, tile):
    if (tile.get_number_y() + tile.get_number_n() > 0) and (tile.solved == False):
        #One status tells all status, so checks for any nonzero statuses
        if tile.up_status != 0:
            tile.down_status = tile.up_status
            tile.left_status = -1 * tile.up_status
            tile.right_status = -1 * tile.up_status
            tile.solved = True
        elif tile.right_status != 0:
            tile.left_status = tile.right_status
            tile.down_status = -1 * tile.right_status
            tile.up_status = -1 * tile.right_status
            tile.solved = True
        elif tile.down_status != 0:
            tile.up_status = tile.down_status
            tile.left_status = -1 * tile.down_status
            tile.right_status = -1 * tile.down_status
            tile.solved = True
        elif tile.left_status != 0:
            tile.right_status = tile.left_status
            tile.down_status = -1 * tile.left_status
            tile.up_status = -1 * tile.left_status
            tile.solved = True
    #Ensures that one bend is made for solved tiles (if one side is straight, the other cannot be)
    if tile.solved == True:
        if tile.right_status == 1:
            right_tile = board.board[tile.x][tile.y + 1]
            left_tile = board.board[tile.x][tile.y - 1]
            if right_tile.right_status == 1:
                board.board[tile.x][tile.y - 1].left_status = -1
            elif left_tile.left_status == 1:
                board.board[tile.x][tile.y + 1].right_status = -1
        else:
            up_tile = board.board[tile.x - 1][tile.y]
            down_tile = board.board[tile.x + 1][tile.y]
            if up_tile.up_status == 1:
                board.board[tile.x + 1][tile.y].down_status = -1
            elif down_tile.down_status == 1:
                board.board[tile.x - 1][tile.y].up_status = -1

def distribute_data(board, tile):
    #Make the status of surrounding tiles match any updates
    if (tile.up_status != 0) and (tile.x != 0):
        up_tile = board.board[tile.x - 1][tile.y]
        if up_tile.down_status == 0:
            board.board[tile.x - 1][tile.y].down_status = tile.up_status
    if (tile.right_status != 0) and (tile.y != (len(board.board[0]) - 1)):
        right_tile = board.board[tile.x][tile.y + 1]
        if right_tile.left_status == 0:
            board.board[tile.x][tile.y + 1].left_status = tile.right_status
    if (tile.down_status != 0) and (tile.x != (len(board.board) - 1)):
        down_tile = board.board[tile.x + 1][tile.y]
        if down_tile.up_status == 0:
            board.board[tile.x + 1][tile.y].up_status = tile.down_status
    if (tile.left_status != 0) and (tile.y != 0):
        left_tile = board.board[tile.x][tile.y - 1]
        if left_tile.right_status == 0:
            board.board[tile.x][tile.y - 1].right_status = tile.left_status

def solve_black_tile(board, tile):
    #Checks if a two tile extension is allowed, and if not blocks direction
    if tile.up_status == 0:
        up_tile = board.board[tile.x - 1][tile.y]
        if (up_tile.up_status == -1) or (up_tile.left_status == 1) or (up_tile.right_status == 1):
            tile.up_status = -1
    if tile.down_status == 0:
        down_tile = board.board[tile.x + 1][tile.y]
        if (down_tile.down_status == -1) or (down_tile.left_status == 1) or (down_tile.right_status == 1):
            tile.down_status = -1
    if tile.right_status == 0:
        right_tile = board.board[tile.x][tile.y + 1]
        if (right_tile.right_status == -1) or (right_tile.up_status == 1) or (right_tile.down_status == 1):
            tile.right_status = -1
    if tile.left_status == 0:
        left_tile = board.board[tile.x][tile.y - 1]
        if (left_tile.left_status == -1) or (left_tile.up_status == 1) or (left_tile.down_status == 1):
            tile.left_status = -1
    #Makes opposite sides opposite status
    if tile.up_status != 0:
        tile.down_status = -1 * tile.up_status
    if tile.down_status != 0:
        tile.up_status = -1 * tile.down_status
    if tile.left_status != 0:
        tile.right_status = -1 * tile.left_status
    if tile.right_status != 0:
        tile.left_status = -1 * tile.right_status
    #Extends any branches another tile and distributes next tile's data
    if tile.up_status == 1:
        board.board[tile.x - 1][tile.y].up_status = 1
        distribute_data(board, board.board[tile.x - 1][tile.y])
    if tile.down_status == 1:
        board.board[tile.x + 1][tile.y].down_status = 1
        distribute_data(board, board.board[tile.x + 1][tile.y])
    if tile.left_status == 1:
        board.board[tile.x][tile.y - 1].left_status = 1
        distribute_data(board, board.board[tile.x][tile.y - 1])
    if tile.right_status == 1:
        board.board[tile.x][tile.y + 1].right_status = 1
        distribute_data(board, board.board[tile.x][tile.y + 1])
    #If two branches exist, solve
    if tile.get_number_y == 2:
        tile.solved = True

def get_endpoint(board, tile, dir):
    #Recursive function that continues down line until it reaches other endpoint
    if dir == "Up":
        if board.board[tile.x - 1][tile.y].get_number_y() == 1:
            return board.board[tile.x - 1][tile.y]
        else:
            if board.board[tile.x - 1][tile.y].up_status == 1:
                return get_endpoint(board, board.board[tile.x - 1][tile.y], "Up")
            elif board.board[tile.x - 1][tile.y].right_status == 1:
                return get_endpoint(board, board.board[tile.x - 1][tile.y], "Right")
            elif board.board[tile.x - 1][tile.y].left_status == 1:
                return get_endpoint(board, board.board[tile.x - 1][tile.y], "Left")
    elif dir == "Right":
        if board.board[tile.x][tile.y + 1].get_number_y() == 1:
            return board.board[tile.x][tile.y + 1]
        else:
            if board.board[tile.x][tile.y + 1].up_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y + 1], "Up")
            elif board.board[tile.x][tile.y + 1].down_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y + 1], "Down")
            elif board.board[tile.x][tile.y + 1].right_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y + 1], "Right")
    elif dir == "Down":
        if board.board[tile.x + 1][tile.y].get_number_y() == 1:
            return board.board[tile.x + 1][tile.y]
        else:
            if board.board[tile.x + 1][tile.y].down_status == 1:
                return get_endpoint(board, board.board[tile.x + 1][tile.y], "Down")
            elif board.board[tile.x + 1][tile.y].right_status == 1:
                return get_endpoint(board, board.board[tile.x + 1][tile.y], "Right")
            elif board.board[tile.x + 1][tile.y].left_status == 1:
                return get_endpoint(board, board.board[tile.x + 1][tile.y], "Left")
    elif dir == "Left":
        if board.board[tile.x][tile.y - 1].get_number_y() == 1:
            return board.board[tile.x][tile.y - 1]
        else:
            if board.board[tile.x][tile.y - 1].up_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y - 1], "Up")
            elif board.board[tile.x][tile.y - 1].down_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y - 1], "Down")
            elif board.board[tile.x][tile.y - 1].left_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y - 1], "Left")

def solve_tile(board, tile):
    #Endpoint tracking
    if (tile.solved == False) and (tile.get_number_y() == 1):
        if tile.up_status == 1:
            end = get_endpoint(board, tile, "Up")
            if end.x == tile.x:
                if end.y - tile.y == 1:
                    tile.right_status = -1
                elif tile.y - end.y == 1:
                    tile.left_status = -1
            elif end.y == tile.y:
                if end.x - tile.x == 1:
                    tile.down_status = -1
        elif tile.right_status == 1:
            end = get_endpoint(board, tile, "Right")
            if end.y == tile.y:
                if end.x - tile.x == 1:
                    tile.down_status = -1
                elif tile.x - end.x == 1:
                    tile.up_status = -1
            elif end.x == tile.x:
                if tile.y - end.y == 1:
                    tile.left_status = -1
        elif tile.down_status == 1:
            end = get_endpoint(board, tile, "Down")
            if end.x == tile.x:
                if end.y - tile.y == 1:
                    tile.right_status = -1
                elif tile.y - end.y == 1:
                    tile.left_status = -1
            elif end.y == tile.y:
                if tile.x - end.x == 1:
                    tile.up_status = -1
        else:
            end = get_endpoint(board, tile, "Left")
            if end.y == tile.y:
                if end.x - tile.x == 1:
                    tile.down_status = -1
                elif tile.x - end.x == 1:
                    tile.up_status = -1
            elif end.x == tile.x:
                if end.y - tile.y == 1:
                    tile.right_status = -1
    #Solve by color
    if tile.color == 'E':
        if tile.solved == False:
            solve_empty_tile(board, tile)
    elif tile.color == 'W':
        solve_white_tile(board, tile)
    else:
        if tile.solved == False:
            solve_black_tile(board, tile)
    distribute_data(board, tile)

def solve(board):
    #Solve all tiles
    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            solve_tile(board, board.board[i][j])
        

colors = [['E','W','E','E','E','E','W','E','E','E',],\
['E','E','E','W','E','E','E','E','E','W',],\
['B','W','E','W','E','W','E','W','W','E',],\
['W','E','B','W','E','B','E','E','W','E',],\
['E','E','E','E','E','E','E','E','E','E',],\
['E','E','B','E','E','E','W','B','E','W',],\
['W','E','E','W','E','E','E','W','E','E',],\
['E','E','E','W','W','E','E','E','E','E',],\
['E','E','E','W','W','E','W','W','E','E',],\
['B','W','E','E','E','E','E','E','E','B',]]

board = Board(colors)
for i in range(30):
    solve(board)
board.board[1][9].print()
board.print()


