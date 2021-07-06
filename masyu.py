import tkinter as tk

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates 40 vertical lines 
    for i in range(0, w, int(w/dim)):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates 40 horizontal lines 
    for i in range(0, h, int(h/dim)):
        c.create_line([(0, i), (w, i)], tag='grid_line')

def draw_units(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas

    c.delete('unit') # Will only remove the grid_line

    for i in range(len(colors)):
        for j in range(len(colors[0])):
            if(colors[j][i]=="W"):
                c.create_rectangle(i*int(w/dim), j*int(h/dim), (1+i)*int(w/dim), (1+j)*int(h/dim), fill="white", outline = 'black', tag='unit') 
            elif(colors[j][i]=="B"):
                c.create_rectangle(i*int(w/dim), j*int(h/dim), (1+i)*int(w/dim), (1+j)*int(h/dim), fill="black", outline = 'white', tag='unit') 
            else:
                c.create_rectangle(i*int(w/dim), j*int(h/dim), (1+i)*int(w/dim), (1+j)*int(h/dim), fill="gray", outline = 'mint cream', tag='unit') 
    c.delete('circ') # Will only remove the grid_line

    for i in range(len(board.board)):
        for j in range(len(board.board[0])):
            if board.board[j][i].up_status == 1:
                c.create_circle((.5+i)*int(w/dim), j*int(h/dim), 5, fill="dark green", outline="white", width=1, tag='circ')
                c.create_line([((.5+i)*int(w/dim), (j-.5)*int(h/dim)), ((.5+i)*int(w/dim), (j+.5)*int(h/dim))], width=3, fill="dark green")
            elif board.board[j][i].up_status == -1:
                c.create_circle((.5+i)*int(w/dim), j*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')
            if board.board[j][i].right_status == 1:
                c.create_circle((1+i)*int(w/dim), (.5+j)*int(h/dim), 5, fill="dark green", outline="white", width=1, tag='circ')
                c.create_line([((.5+i)*int(w/dim), (j+.5)*int(h/dim)), ((1.5+i)*int(w/dim), (j+.5)*int(h/dim))], width=3, fill="dark green")
            elif board.board[j][i].right_status == -1:
                c.create_circle((1+i)*int(w/dim), (.5+j)*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')
            if board.board[j][i].down_status == 1:
                c.create_circle((.5+i)*int(w/dim), (1+j)*int(h/dim), 5, fill="dark green", outline="white", width=1, tag='circ')
            elif board.board[j][i].down_status == -1:
                c.create_circle((.5+i)*int(w/dim), (1+j)*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')
            if board.board[j][i].left_status == 1:
                c.create_circle(i*int(w/dim), (.5+j)*int(h/dim), 5, fill="dark green", outline="white", width=1, tag='circ')
            elif board.board[j][i].left_status == -1:
                c.create_circle(i*int(w/dim), (.5+j)*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')

def draw_circles(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas

    c.delete('circ') # Will only remove the grid_line

    for i in range(len(board.board)):
        for j in range(len(board.board[0])):
            if board.board[j][i].up_status == 1:
                c.create_circle((.5+i)*int(w/dim), j*int(h/dim), 5, fill="green", outline="white", width=1, tag='circ')
            elif board.board[j][i].up_status == -1:
                c.create_circle((.5+i)*int(w/dim), j*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')
            if board.board[j][i].right_status == 1:
                c.create_circle((1+i)*int(w/dim), (.5+j)*int(h/dim), 5, fill="green", outline="white", width=1, tag='circ')
            elif board.board[j][i].right_status == -1:
                c.create_circle((1+i)*int(w/dim), (.5+j)*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')
            if board.board[j][i].down_status == 1:
                c.create_circle((.5+i)*int(w/dim), (1+j)*int(h/dim), 5, fill="green", outline="white", width=1, tag='circ')
            elif board.board[j][i].down_status == -1:
                c.create_circle((.5+i)*int(w/dim), (1+j)*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')
            if board.board[j][i].left_status == 1:
                c.create_circle(i*int(w/dim), (.5+j)*int(h/dim), 5, fill="green", outline="white", width=1, tag='circ')
            elif board.board[j][i].left_status == -1:
                c.create_circle(i*int(w/dim), (.5+j)*int(h/dim), 5, fill="red", outline="black", width=1, tag='circ')


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
        self.cooldown = 10
        self.new_cooldown = 10
        if tile_color == 'E':
            self.can_empty = True
        else:
            self.can_empty = False
        self.flooded = False
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
        print(self.x, self.y)
        print(self.up_status)
        print(self.right_status)
        print(self.down_status)
        print(self.left_status)
        print(self.solved)
    def get_all_open(self):
        lst = []
        if self.up_status == 0:
            lst.append("Up")
        if self.right_status == 0:
            lst.append("Right")
        if self.down_status == 0:
            lst.append("Down")
        if self.left_status == 0:
            lst.append("Left")
        return lst
    def get_all_yes(self):
        lst = []
        if self.up_status == 1:
            lst.append("Up")
        if self.right_status == 1:
            lst.append("Right")
        if self.down_status == 1:
            lst.append("Down")
        if self.left_status == 1:
            lst.append("Left")
        return lst 
    def get_first_open(self):
        return self.get_all_open()[0]
    def get_second_open(self):
        return self.get_all_open()[1]
    def get_third_open(self):
        return self.get_all_open()[2]
    def set_to_yes(self, dir):
        if dir == "Up":
            self.up_status = 1
        elif dir == "Right":
            self.right_status = 1
        elif dir == "Down":
            self.down_status = 1
        else:
            self.left_status = 1
    def set_to_no(self, dir):
        if dir == "Up":
            self.up_status = -1
        elif dir == "Right":
            self.right_status = -1
        elif dir == "Down":
            self.down_status = -1
        else:
            self.left_status = -1
    def get_all_yes(self):
        lst = []
        if self.up_status == 1:
            lst.append("Up")
        if self.right_status == 1:
            lst.append("Right")
        if self.down_status == 1:
            lst.append("Down")
        if self.left_status == 1:
            lst.append("Left")
        return lst
    def get_first_yes(self):
        return self.get_all_yes()[0]

def opposite(dir):
    if dir == "Up":
        return "Down"
    elif dir == "Down":
        return "Up"
    elif dir == "Left":
        return "Right"
    else:
        return "Left"

def convert_status_to_char(status):
    if status == 0:
        return "?"
    elif status == -1:
        return "n"
    return "y"

class Board:
    def __init__(self, colors):
        self.board = [[0 for x in range(len(colors[0]))] for y in range(len(colors))]
        self.colors = colors
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
    def copy(self):
        new_board = Board(self.colors)
        for i in range(len(new_board.board)):
            for j in range(len(new_board.board[0])):
                new_board.board[i][j].up_status = self.board[i][j].up_status
                new_board.board[i][j].down_status = self.board[i][j].down_status
                new_board.board[i][j].left_status = self.board[i][j].left_status
                new_board.board[i][j].right_status = self.board[i][j].right_status
                new_board.board[i][j].solved = self.board[i][j].solved
        return new_board

def get_endpoint(board, tile, dir, count):
    #Recursive function that continues down line until it reaches other endpoint
    if dir == "Up":
        if board.board[tile.x - 1][tile.y].get_number_y() == 1:
            return (board.board[tile.x - 1][tile.y], count)
        else:
            if board.board[tile.x - 1][tile.y].up_status == 1:
                return get_endpoint(board, board.board[tile.x - 1][tile.y], "Up", count + 1)
            elif board.board[tile.x - 1][tile.y].right_status == 1:
                return get_endpoint(board, board.board[tile.x - 1][tile.y], "Right", count + 1)
            elif board.board[tile.x - 1][tile.y].left_status == 1:
                return get_endpoint(board, board.board[tile.x - 1][tile.y], "Left", count + 1)
    elif dir == "Right":
        if board.board[tile.x][tile.y + 1].get_number_y() == 1:
            return (board.board[tile.x][tile.y + 1], count)
        else:
            if board.board[tile.x][tile.y + 1].up_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y + 1], "Up", count + 1)
            elif board.board[tile.x][tile.y + 1].down_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y + 1], "Down", count + 1)
            elif board.board[tile.x][tile.y + 1].right_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y + 1], "Right", count + 1)
    elif dir == "Down":
        if board.board[tile.x + 1][tile.y].get_number_y() == 1:
            return (board.board[tile.x + 1][tile.y], count)
        else:
            if board.board[tile.x + 1][tile.y].down_status == 1:
                return get_endpoint(board, board.board[tile.x + 1][tile.y], "Down", count + 1)
            elif board.board[tile.x + 1][tile.y].right_status == 1:
                return get_endpoint(board, board.board[tile.x + 1][tile.y], "Right", count + 1)
            elif board.board[tile.x + 1][tile.y].left_status == 1:
                return get_endpoint(board, board.board[tile.x + 1][tile.y], "Left", count + 1)
    elif dir == "Left":
        if board.board[tile.x][tile.y - 1].get_number_y() == 1:
            return (board.board[tile.x][tile.y - 1], count)
        else:
            if board.board[tile.x][tile.y - 1].up_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y - 1], "Up", count + 1)
            elif board.board[tile.x][tile.y - 1].down_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y - 1], "Down", count + 1)
            elif board.board[tile.x][tile.y - 1].left_status == 1:
                return get_endpoint(board, board.board[tile.x][tile.y - 1], "Left", count + 1)


def get_path_end(board, tile, dir, start_x, start_y):
    #For a hallway tile (two statuses set to no, can either be a fixed path or nothing)
    #Checks in the direction dir and if the tile in direction dir is an endpoint or an open
    #end then it returns that tile otherwise it keeps iterating down the hallway
    if dir == "Up":
        if tile.x - 1 == start_x and tile.y == start_y:
            return board.board[tile.x - 1][tile.y]
        elif board.board[tile.x - 1][tile.y].get_number_y() > 0:
            return board.board[tile.x - 1][tile.y]
        elif board.board[tile.x - 1][tile.y].get_number_n() != 2:
            return board.board[tile.x - 1][tile.y]
        else:
            new_dir = board.board[tile.x - 1][tile.y].get_first_open()
            if new_dir == opposite(dir):
                return get_path_end(board, board.board[tile.x - 1][tile.y], board.board[tile.x - 1][tile.y].get_second_open(), start_x, start_y)
            else:
                return get_path_end(board, board.board[tile.x - 1][tile.y], new_dir, start_x, start_y)
    if dir == "Right":
        if tile.x == start_x and tile.y + 1 == start_y:
            return board.board[tile.x][tile.y + 1]
        elif board.board[tile.x][tile.y + 1].get_number_y() > 0:
            return board.board[tile.x][tile.y + 1]
        elif board.board[tile.x][tile.y + 1].get_number_n() != 2:
            return board.board[tile.x][tile.y + 1]
        else:
            new_dir = board.board[tile.x][tile.y + 1].get_first_open()
            if new_dir == opposite(dir):
                return get_path_end(board, board.board[tile.x][tile.y + 1], board.board[tile.x][tile.y + 1].get_second_open(), start_x, start_y)
            else:
                return get_path_end(board, board.board[tile.x][tile.y + 1], new_dir, start_x, start_y)
    if dir == "Down":
        if tile.x + 1 == start_x and tile.y == start_y:
            return board.board[tile.x + 1][tile.y]
        elif board.board[tile.x + 1][tile.y].get_number_y() > 0:
            return board.board[tile.x + 1][tile.y]
        elif board.board[tile.x + 1][tile.y].get_number_n() != 2:
            return board.board[tile.x + 1][tile.y]
        else:
            new_dir = board.board[tile.x + 1][tile.y].get_first_open()
            if new_dir == opposite(dir):
                return get_path_end(board, board.board[tile.x + 1][tile.y], board.board[tile.x + 1][tile.y].get_second_open(), start_x, start_y)
            else:
                return get_path_end(board, board.board[tile.x + 1][tile.y], new_dir, start_x, start_y)
    if dir == "Left":
        if tile.x == start_x and tile.y - 1== start_y:
            return board.board[tile.x][tile.y - 1]
        elif board.board[tile.x][tile.y - 1].get_number_y() > 0:
            return board.board[tile.x][tile.y - 1]
        elif board.board[tile.x][tile.y - 1].get_number_n() != 2:
            return board.board[tile.x][tile.y - 1]
        else:
            new_dir = board.board[tile.x][tile.y - 1].get_first_open()
            if new_dir == opposite(dir):
                return get_path_end(board, board.board[tile.x][tile.y - 1], board.board[tile.x][tile.y - 1].get_second_open(), start_x, start_y)
            else:
                return get_path_end(board, board.board[tile.x][tile.y - 1], new_dir, start_x, start_y)

def simulate_flood(board, tile, start):
    tile.flooded = True
    if tile.get_number_y() != 1 or start == True:
        dirs = tile.get_all_open()
        for i in dirs:
            if i == "Up":
                if board.board[tile.x-1][tile.y].flooded == False:
                    simulate_flood(board, board.board[tile.x - 1][tile.y], False)
            elif i == "Down":
                if board.board[tile.x+1][tile.y].flooded == False:
                    simulate_flood(board, board.board[tile.x + 1][tile.y], False)
            elif i == "Right":
                if board.board[tile.x][tile.y+1].flooded == False:
                    simulate_flood(board, board.board[tile.x][tile.y + 1], False)
            elif i == "Left":
                if board.board[tile.x][tile.y-1].flooded == False:
                    simulate_flood(board, board.board[tile.x][tile.y - 1], False)

def contained_to_flood(board, tile):
    dirs = tile.get_all_open()
    for i in dirs:
        if i == "Up":
            if board.board[tile.x - 1][tile.y].flooded == False:
                return False
        elif i == "Right":
            if board.board[tile.x][tile.y + 1].flooded == False:
                return False
        elif i == "Down":
            if board.board[tile.x + 1][tile.y].flooded == False:
                return False
        elif i == "Left":
            if board.board[tile.x][tile.y - 1].flooded == False:
                return False
    return True



def is_dead_end(board, tile, end, count):
    # dirs = tile.get_all_open()
    # for dir in dirs:
    #     if dir == "Up":
    #         if board.board[tile.x - 1][tile.y] in acc:
    #             pass
    #         elif tile.x - 1 == end.x and tile.y == end.y:
    #             pass
    #         elif board.board[tile.x - 1][tile.y].get_number_y() == 1:
    #             return False
    #         else:
    #             acc.append(tile)
    #             if not is_dead_end(board, board.board[tile.x - 1][tile.y], acc, end):
    #                 return False
    #     elif dir == "Right":
    #         if board.board[tile.x][tile.y + 1] in acc:
    #             pass
    #         elif tile.x == end.x and tile.y + 1 == end.y:
    #             pass
    #         elif board.board[tile.x][tile.y + 1].get_number_y() == 1:
    #             return False
    #         else:
    #             acc.append(tile)
    #             if not is_dead_end(board, board.board[tile.x][tile.y + 1], acc, end):
    #                 return False
    #     elif dir == "Down":
    #         if board.board[tile.x + 1][tile.y] in acc:
    #             pass
    #         elif tile.x + 1 == end.x and tile.y == end.y:
    #             pass
    #         elif board.board[tile.x + 1][tile.y].get_number_y() == 1:
    #             return False
    #         else:
    #             acc.append(tile)
    #             if not is_dead_end(board, board.board[tile.x + 1][tile.y], acc, end):
    #                 return False
    #     else:
    #         if board.board[tile.x][tile.y - 1] in acc:
    #             pass
    #         elif tile.x == end.x and tile.y - 1 == end.y:
    #             pass
    #         elif board.board[tile.x][tile.y - 1].get_number_y() == 1:
    #             return False
    #         else:
    #             acc.append(tile)
    #             if not is_dead_end(board, board.board[tile.x][tile.y - 1], acc, end):
    #                 return False
    # return True
    simulate_flood(board, tile, True)
    count = 0
    non_count = 0
    all_ends_contained = True
    for row in board.board:
        for t in row:
            if t.flooded == True and t.get_number_y() == 1:
                if contained_to_flood(board, t):
                    (t_end, t_a) = get_endpoint(board, t, t.get_first_yes(), 0)
                    if t_end.flooded == False and (t.x != tile.x or t.y != tile.y):
                        all_ends_contained = False
                    count = count + 1
                else:
                    non_count = non_count + 1
    for row in board.board:
        for t in row:
            t.flooded = False
    if count + non_count == 2 and board.board[end.x][end.y].flooded == True:
        return True
    elif count + non_count == 1:
        return True
    elif count % 2 != 0 and non_count == 0:
        return True
    elif non_count == 0 and all_ends_contained == True:
        return True
    return False


def is_broken(board):
    for i in range(len(board.board)):
        for j in range(len(board.board[0])):
            if (board.board[i][j].get_number_y() == 1 and board.board[i][j].get_number_n() == 3) or (board.board[i][j].get_number_y() == 3 and board.board[i][j].get_number_n() == 1):
                return True
            if board.board[i][j].can_empty == False and board.board[i][j].get_number_n() == 4:
                return True
            if board.board[i][j].get_number_y() == 1 and board.board[i][j].get_number_n() < 3:
                (end, a) = get_endpoint(board, board.board[i][j], board.board[i][j].get_first_yes(), 0)
                if is_dead_end(board, board.board[i][j], end, a):
                    return True
            if board.board[i][j].get_number_y() == 2:
                try:
                    (end, a) = get_endpoint(board, board.board[i][j], board.board[i][j].get_first_yes(), 0)
                except:
                    return True
            if board.board[i][j].color == 'W':
                if board.board[i][j].up_status == 1:
                    if board.board[i-1][j].up_status == 1 and board.board[i+1][j].down_status == 1:
                        return True
                if board.board[i][j].right_status == 1:
                    if board.board[i][j+1].right_status == 1 and board.board[i][j-1].left_status == 1:
                        return True
    return False


def solve_empty_tile(board, tile, debug):
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
    elif tile.get_number_y() == 0 and tile.new_cooldown == 0 and debug == False:
        dirs = tile.get_all_open()
        new_board = board.copy()
        for i in dirs:
            new_board.board[tile.x][tile.y].set_to_no(i)
        new_board.board[tile.x][tile.y].solved = True
        distribute_data(new_board, new_board.board[tile.x][tile.y])
        try:
            for i in range(10):
                solve(new_board, True)
            if is_broken(new_board) == True:
                tile.can_empty = False
        except:
            tile.can_empty = False
        tile.new_cooldown = 10
    elif tile.get_number_y() == 0 and debug == False:
        tile.new_cooldown = tile.new_cooldown - 1
    #If it is a hallway (two statuses are no, so must either be empty or have a fixed path)
    #then it uses get_path_end to extend along the hallway until nothing or an end is reached
    #If two endpoints are reached then get_endpoint is run and if the endpoints match
    #then all statuses are set to false because that means filling the hallway creates
    #a loop
    if (tile.get_number_n() == 2) and (tile.get_number_y() == 0):
        # tile_one = get_path_end(board, tile, tile.get_first_open(), tile.x, tile.y)
        # tile_two = get_path_end(board, tile, tile.get_second_open(), tile.x, tile.y)
        # if tile_one.get_number_y() == 1:
        #     if tile_one.up_status == 1:
        #         (tile_one_end, a) = get_endpoint(board, tile_one, "Up", 0)
        #         if tile_one_end.x == tile_two.x and tile_one_end.y == tile_two.y:
        #             tile.up_status = -1
        #             tile.right_status = -1
        #             tile.down_status = -1
        #             tile.left_status = -1
        #             tile.solved = True
        #     elif tile_one.right_status == 1:
        #         (tile_one_end, a) = get_endpoint(board, tile_one, "Right", 0)
        #         if tile_one_end.x == tile_two.x and tile_one_end.y == tile_two.y:
        #             tile.up_status = -1
        #             tile.right_status = -1
        #             tile.down_status = -1
        #             tile.left_status = -1
        #             tile.solved = True
        #     elif tile_one.down_status == 1:
        #         (tile_one_end, a) = get_endpoint(board, tile_one, "Down", 0)
        #         if tile_one_end.x == tile_two.x and tile_one_end.y == tile_two.y:
        #             tile.up_status = -1
        #             tile.right_status = -1
        #             tile.down_status = -1
        #             tile.left_status = -1
        #             tile.solved = True
        #     else:
        #         (tile_one_end, a) = get_endpoint(board, tile_one, "Left", 0)
        #         if tile_one_end.x == tile_two.x and tile_one_end.y == tile_two.y:
        #             tile.up_status = -1
        #             tile.right_status = -1
        #             tile.down_status = -1
        #             tile.left_status = -1
        #             tile.solved = True
        if tile.can_empty == False:
            dirs = tile.get_all_open()
            for i in dirs:
                tile.set_to_yes(i)
            tile.solved = True
        elif (tile.solved == False and debug == False) and (tile.cooldown == 0):
            new_board = board.copy()
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_first_open())
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_second_open())
            new_board.board[tile.x][tile.y].solved = True
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.set_to_no(tile.get_first_open())
                    tile.set_to_no(tile.get_first_open())
                    tile.solved = True
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_first_open())
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_second_open())
                    new_board_two.board[tile.x][tile.y].solved = True
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.set_to_yes(tile.get_first_open())
                            tile.set_to_yes(tile.get_first_open())
                            tile.solved = True
                    except:
                        tile.set_to_yes(tile.get_first_open())
                        tile.set_to_yes(tile.get_first_open())
                        tile.solved = True
            except:
                tile.set_to_no(tile.get_first_open())
                tile.set_to_no(tile.get_first_open())
                tile.solved = True
            tile.cooldown = 10
        elif (tile.solved == False and debug == False):
            tile.cooldown = tile.cooldown - 1
    elif tile.get_number_y() == 1 and tile.get_number_n() == 1:
        if debug == False and tile.cooldown == 0:
            new_board = board.copy()
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_first_open())
            new_board.board[tile.x][tile.y].set_to_no(tile.get_second_open())
            new_board.board[tile.x][tile.y].solved = True
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.set_to_no(tile.get_first_open())
                    tile.set_to_yes(tile.get_first_open())
                    tile.solved = True
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_first_open())
                    new_board_two.board[tile.x][tile.y].set_to_yes(tile.get_second_open())
                    new_board_two.board[tile.x][tile.y].solved = True
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.set_to_yes(tile.get_first_open())
                            tile.set_to_no(tile.get_first_open())
                            tile.solved = True
                    except:
                        tile.set_to_yes(tile.get_first_open())
                        tile.set_to_no(tile.get_first_open())
                        tile.solved = True
            except:
                tile.set_to_no(tile.get_first_open())
                tile.set_to_yes(tile.get_first_open())
                tile.solved = True
            tile.cooldown = 10
        elif debug == False:
            tile.cooldown = tile.cooldown - 1
    elif tile.get_number_y() == 0 and tile.get_number_n() == 1 and tile.can_empty == False:
        if debug == False and tile.cooldown == 0:
            new_board = board.copy()
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_first_open())
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_second_open())
            new_board.board[tile.x][tile.y].set_to_no(tile.get_third_open())
            new_board.board[tile.x][tile.y].solved = True
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.set_to_yes(tile.get_third_open())
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].set_to_yes(tile.get_first_open())
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_second_open())
                    new_board_two.board[tile.x][tile.y].set_to_yes(tile.get_third_open())
                    new_board_two.board[tile.x][tile.y].solved = True
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.set_to_yes(tile.get_second_open())
                        else:
                            new_board_three = board.copy()
                            new_board_three.board[tile.x][tile.y].set_to_no(tile.get_first_open())
                            new_board_three.board[tile.x][tile.y].set_to_yes(tile.get_second_open())
                            new_board_three.board[tile.x][tile.y].set_to_yes(tile.get_third_open())
                            new_board_three.board[tile.x][tile.y].solved = True
                            distribute_data(new_board_three, new_board_three.board[tile.x][tile.y])
                            try:
                                for i in range(10):
                                    solve(new_board_three, True)
                                if is_broken(new_board_three) == True:
                                    tile.set_to_yes(tile.get_first_open())
                            except:
                                tile.set_to_yes(tile.get_first_open())
                    except:
                        tile.set_to_yes(tile.get_second_open())
            except:
                tile.set_to_yes(tile.get_third_open())
            tile.cooldown = 10
        elif debug == False:
            tile.cooldown = tile.cooldown - 1 
    elif tile.get_number_y() == 1 and tile.get_number_n() == 0:
        if debug == False and tile.cooldown == 0:
            new_board = board.copy()
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_first_open())
            new_board.board[tile.x][tile.y].set_to_no(tile.get_second_open())
            new_board.board[tile.x][tile.y].set_to_no(tile.get_third_open())
            new_board.board[tile.x][tile.y].solved = True
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.set_to_no(tile.get_first_open())
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_first_open())
                    new_board_two.board[tile.x][tile.y].set_to_yes(tile.get_second_open())
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_third_open())
                    new_board_two.board[tile.x][tile.y].solved = True
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.set_to_no(tile.get_second_open())
                        else:
                            new_board_three = board.copy()
                            new_board_three.board[tile.x][tile.y].set_to_no(tile.get_first_open())
                            new_board_three.board[tile.x][tile.y].set_to_no(tile.get_second_open())
                            new_board_three.board[tile.x][tile.y].set_to_yes(tile.get_third_open())
                            new_board_three.board[tile.x][tile.y].solved = True
                            distribute_data(new_board_three, new_board_three.board[tile.x][tile.y])
                            try:
                                for i in range(10):
                                    solve(new_board_three, True)
                                if is_broken(new_board_three) == True:
                                    tile.set_to_no(tile.get_third_open())
                            except:
                                tile.set_to_no(tile.get_third_open())
                    except:
                        tile.set_to_no(tile.get_second_open())
            except:
                tile.set_to_no(tile.get_first_open())
            tile.cooldown = 10
        elif debug == False:
            tile.cooldown = tile.cooldown - 1 

    
def not_ian(board, tile, dir):
    #Must be straight
    if tile.color == 'W':
        return True
    elif tile.get_number_n() == 2:
        if tile.up_status == -1:
            if tile.down_status == -1:
                return True
            else:
                return False
        elif tile.left_status == -1:
            if tile.right_status == -1:
                return True
            else:
                return False
    elif dir == "Up":
        if tile.up_status == 1:
            return True
        else:
            return False
    elif dir == "Right":
        if tile.right_status == 1:
            return True
        else:
            return False
    elif dir == "Down":
        if tile.down_status == 1:
            return True
        else:
            return False
    elif dir == "Left":
        if tile.left_status == 1:
            return True
        else: 
            return False
    else:
        return False


def solve_white_tile(board, tile, debug):
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
                if board.board[tile.x][tile.y - 1].left_status == 0:
                    board.board[tile.x][tile.y - 1].left_status = -1
            elif left_tile.left_status == 1:
                if board.board[tile.x][tile.y + 1].right_status == 0:
                    board.board[tile.x][tile.y + 1].right_status = -1
        else:
            up_tile = board.board[tile.x - 1][tile.y]
            down_tile = board.board[tile.x + 1][tile.y]
            if up_tile.up_status == 1:
                if board.board[tile.x + 1][tile.y].down_status == 0:
                    board.board[tile.x + 1][tile.y].down_status = -1
            elif down_tile.down_status == 1:
                if board.board[tile.x - 1][tile.y].up_status == 0:
                    board.board[tile.x - 1][tile.y].up_status = -1
    #Checks if tile on both sides must be straight, and if so, sets to other orientation
    #For example, if the top and bottom tiles must be straight, it cant go up and down because
    #it has to turn, so it sets it to left to right
    else:
        up_tile = board.board[tile.x - 1][tile.y]
        down_tile = board.board[tile.x + 1][tile.y]
        right_tile = board.board[tile.x][tile.y + 1]
        left_tile = board.board[tile.x][tile.y - 1]
        if (not_ian(board, up_tile, "Up") == True) and (not_ian(board, down_tile, "Down") == True):
            tile.up_status = -1
            tile.right_status = 1
            tile.down_status = -1
            tile.left_status = 1
            tile.solved = True
        elif (not_ian(board, right_tile, "Right") == True) and (not_ian(board, left_tile, "Left") == True):
            tile.up_status = 1
            tile.right_status = -1
            tile.down_status = 1
            tile.left_status = -1
            tile.solved = True
        if (tile.solved == False and debug == False) and (tile.cooldown == 0):
            new_board = board.copy()
            new_board.board[tile.x][tile.y].up_status = 1
            new_board.board[tile.x][tile.y].down_status = 1
            new_board.board[tile.x][tile.y].left_status = -1
            new_board.board[tile.x][tile.y].right_status = -1
            new_board.board[tile.x][tile.y].solved = True
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.up_status = -1
                    tile.down_status = -1
                    tile.left_status = 1
                    tile.right_status = 1
                    tile.solved = True
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].up_status = -1
                    new_board_two.board[tile.x][tile.y].down_status = -1
                    new_board_two.board[tile.x][tile.y].left_status = 1
                    new_board_two.board[tile.x][tile.y].right_status = 1
                    new_board_two.board[tile.x][tile.y].solved = True
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.up_status = 1
                            tile.down_status = 1
                            tile.left_status = -1
                            tile.right_status = -1
                            tile.solved = True
                    except:
                        tile.up_status = 1
                        tile.down_status = 1
                        tile.left_status = -1
                        tile.right_status = -1
                        tile.solved = True
            except:
                tile.up_status = -1
                tile.down_status = -1
                tile.left_status = 1
                tile.right_status = 1
                tile.solved = True
            tile.cooldown = 10
        elif (tile.solved == False and debug == False):
            tile.cooldown = tile.cooldown - 1


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

def solve_black_tile(board, tile, debug):
    #Checks if a two tile extension is allowed, and if not blocks direction
    if tile.up_status == 0:
        up_tile = board.board[tile.x - 1][tile.y]
        if (up_tile.up_status == -1) or (up_tile.left_status == 1) or (up_tile.right_status == 1) or (up_tile.color == 'B'):
            tile.up_status = -1
    if tile.down_status == 0:
        down_tile = board.board[tile.x + 1][tile.y]
        if (down_tile.down_status == -1) or (down_tile.left_status == 1) or (down_tile.right_status == 1) or (down_tile.color == 'B'):
            tile.down_status = -1
    if tile.right_status == 0:
        right_tile = board.board[tile.x][tile.y + 1]
        if (right_tile.right_status == -1) or (right_tile.up_status == 1) or (right_tile.down_status == 1) or (right_tile.color == 'B'):
            tile.right_status = -1
    if tile.left_status == 0:
        left_tile = board.board[tile.x][tile.y - 1]
        if (left_tile.left_status == -1) or (left_tile.up_status == 1) or (left_tile.down_status == 1) or (left_tile.color == 'B'):
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
    if tile.get_number_y() == 2:
        tile.solved = True
    if tile.solved == False:
        if (tile.get_number_y() == 1 and debug == False) and tile.cooldown == 0:
            new_board = board.copy()
            new_board.board[tile.x][tile.y].set_to_yes(tile.get_first_open())
            new_board.board[tile.x][tile.y].set_to_no(tile.get_second_open())
            new_board.board[tile.x][tile.y].solved = True
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.set_to_no(tile.get_first_open())
                    tile.set_to_yes(tile.get_first_open())
                    tile.solved = True
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].set_to_no(tile.get_first_open())
                    new_board_two.board[tile.x][tile.y].set_to_yes(tile.get_second_open())
                    new_board_two.board[tile.x][tile.y].solved = True
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.set_to_yes(tile.get_first_open())
                            tile.set_to_no(tile.get_first_open())
                            tile.solved = True
                    except:
                        tile.set_to_yes(tile.get_first_open())
                        tile.set_to_no(tile.get_first_open())
                        tile.solved = True
            except:
                tile.set_to_no(tile.get_first_open())
                tile.set_to_yes(tile.get_first_open())
                tile.solved = True
            tile.cooldown = 10
        elif debug == False and tile.get_number_y() == 1:
            tile.cooldown = tile.cooldown - 1
        elif debug == False and tile.get_number_y() == 0 and tile.cooldown == 0:
            new_board = board.copy()
            new_board.board[tile.x][tile.y].up_status = 1
            new_board.board[tile.x][tile.y].down_status = -1
            distribute_data(new_board, new_board.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board, True)
                if is_broken(new_board) == True:
                    tile.up_status = -1
                    tile.down_status = 1
                else:
                    new_board_two = board.copy()
                    new_board_two.board[tile.x][tile.y].up_status = -1
                    new_board_two.board[tile.x][tile.y].down_status = 1
                    distribute_data(new_board_two, new_board_two.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_two, True)
                        if is_broken(new_board_two) == True:
                            tile.up_status = 1
                            tile.down_status = -1
                    except:
                        tile.up_status = 1
                        tile.down_status = -1
            except:
                tile.up_status = -1
                tile.down_status = 1
            new_board_three = board.copy()
            new_board_three.board[tile.x][tile.y].right_status = 1
            new_board_three.board[tile.x][tile.y].left_status = -1
            distribute_data(new_board_three, new_board_three.board[tile.x][tile.y])
            try:
                for i in range(10):
                    solve(new_board_three, True)
                if is_broken(new_board_three) == True:
                    tile.right_status = -1
                    tile.left_status = 1
                else:
                    new_board_four = board.copy()
                    new_board_four.board[tile.x][tile.y].right_status = -1
                    new_board_four.board[tile.x][tile.y].left_status = 1
                    distribute_data(new_board_four, new_board_four.board[tile.x][tile.y])
                    try:
                        for i in range(10):
                            solve(new_board_four, True)
                        if is_broken(new_board_four) == True:
                            tile.right_status = 1
                            tile.left_status = -1
                    except:
                        tile.right_status = 1
                        tile.left_status = -1
            except:
                tile.right_status = -1
                tile.left_status = 1
            tile.cooldown = 10
        elif debug == False and tile.get_number_y() == 0:
            tile.cooldown = tile.cooldown - 1
    if tile.get_number_y == 2:
        tile.solved = True

def solve_tile(board, tile, debug):
    #Endpoint tracking
    if (tile.solved == False) and (tile.get_number_y() == 1):
        total = len(board.board) * len(board.board[0])
        if tile.up_status == 1:
            (end, count) = get_endpoint(board, tile, "Up", 0)
            if count < (total * 0.75):
                if end.x == tile.x:
                    if end.y - tile.y == 1:
                        tile.right_status = -1
                    elif tile.y - end.y == 1:
                        tile.left_status = -1
                elif end.y == tile.y:
                    if end.x - tile.x == 1:
                        tile.down_status = -1
        elif tile.right_status == 1:
            (end, count) = get_endpoint(board, tile, "Right", 0)
            if count < (total * 0.75):
                if end.y == tile.y:
                    if end.x - tile.x == 1:
                        tile.down_status = -1
                    elif tile.x - end.x == 1:
                        tile.up_status = -1
                elif end.x == tile.x:
                    if tile.y - end.y == 1:
                        tile.left_status = -1
        elif tile.down_status == 1:
            (end, count) = get_endpoint(board, tile, "Down", 0)
            if count < (total * 0.75):
                if end.x == tile.x:
                    if end.y - tile.y == 1:
                        tile.right_status = -1
                    elif tile.y - end.y == 1:
                        tile.left_status = -1
                elif end.y == tile.y:
                    if tile.x - end.x == 1:
                        tile.up_status = -1
        else:
            (end, count) = get_endpoint(board, tile, "Left", 0)
            if count < (total * 0.75):
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
            solve_empty_tile(board, tile, debug)
    elif tile.color == 'W':
        solve_white_tile(board, tile, debug)
    else:
        solve_black_tile(board, tile, debug)
    distribute_data(board, tile)

def solve(board, debug):
    #Solve all tiles
    count = 0
    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            if board.board[i][j].solved == True:
                count = count + 1
    if debug == True and count > 380:
        pass
    else:
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if debug == False:
                    if board.board[i][j].solved == False:
                        print(board.board[i][j].x, board.board[i][j].y)
                solve_tile(board, board.board[i][j], debug)
        

colors = \
[['E','E','E','W','E','E','E','E','E','W','E','E','E','E','E','B','E','E','W','E'],\
['E','E','E','E','W','W','E','E','W','E','W','E','W','E','B','E','E','E','E','W'],\
['B','E','E','W','E','E','E','W','E','E','E','E','E','E','E','E','E','W','E','B'],\
['E','E','W','E','W','E','W','B','W','E','E','B','E','E','W','E','E','E','E','E'],\
['E','W','E','E','E','E','E','W','E','E','B','W','W','E','E','E','E','E','E','E'],\
['E','B','E','E','E','W','W','E','E','E','E','W','E','W','B','W','E','E','W','E'],\
['E','E','E','E','E','E','E','E','E','W','E','E','E','E','E','E','E','B','E','E'],\
['E','E','W','E','E','B','E','E','E','E','E','E','B','E','W','W','E','E','E','E'],\
['B','E','E','E','E','E','E','B','E','E','E','E','W','E','E','E','E','W','E','W'],\
['E','E','E','E','B','E','B','E','B','E','W','E','E','B','E','E','E','E','W','E'],\
['E','E','E','E','E','E','E','E','W','B','E','E','B','E','W','E','E','E','E','E'],\
['W','E','W','E','B','W','E','E','E','E','B','E','E','E','B','E','E','E','E','E'],\
['E','E','E','W','E','E','E','E','W','E','E','E','E','E','E','E','B','E','B','E'],\
['E','E','E','W','E','B','E','E','E','E','E','E','E','E','B','E','W','E','B','E'],\
['B','E','E','E','W','E','E','E','E','E','E','E','E','E','E','E','E','E','E','E'],\
['E','E','E','E','E','E','W','E','E','B','W','W','E','W','E','W','W','E','W','E'],\
['E','W','E','W','W','B','E','E','E','W','B','E','E','B','E','E','E','W','E','W'],\
['E','E','E','E','E','E','E','W','W','E','E','E','E','W','E','W','E','B','E','E'],\
['E','W','B','W','E','W','E','W','E','W','E','E','W','E','E','W','E','E','W','E'],\
['E','E','E','E','E','B','E','E','E','E','E','E','W','E','E','E','E','E','E','E'],\
]

board = Board(colors)
for i in range(70):
    solve(board, False)
board.print()
for i in board.board:
    for j in i:
        if j.solved == False:
            print(j.x, j.y)

dim = 20

root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)
c.bind('<Configure>', draw_units)

root.mainloop()



