import random

class board:

    def __init__(self):
        # Define the board
        self.row = 0
        self.col = 0
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]

    def get_row(self):
        # Return the row.
        return self.row

    def get_col(self):
        # Return the column.
        return self.col

    def get_board(self):
        # Return the state of the board.
        return self.board

    def set_row_col(self,row,col):
        # Set the row and column.
        self.row = row
        self.col = col

    def valid_move(self):
        # Check if a move is valid.
        if self.row >= 0 and self.row <= 2 and self.col >= 0 and self.col <= 2:
            return self.board[self.row][self.col] == '-'

    def set_move(self,move):
        # Set the current row and column to the move.
        self.board[self.row][self.col] = move

    def print_board(self):
        # Print the state of the board.
        for row in self.board:
            print(" ".join(row))

    def clear_board(self):
        # Clear the board.
        for i, row in enumerate(self.board):
            self.board[i] = ['-']*3

    def winner(self):
        # Check if there is a winner.
        i = 0
        while i <= 2:
            if self.board[0][i] == 'x' and self.board[1][i] == 'x'and self.board[2][i] == 'x':
                print("X wins!")
                return True
            elif self.board[0][i] == 'o' and self.board[1][i] == 'o' and self.board[2][i] == 'o':
                print("O wins!")
                return True
            elif self.board[i][0] == 'x' and self.board[i][1] == 'x'and self.board[i][2] == 'x':
                print("X wins!")
                return True
            elif self.board[i][0] == 'o' and self.board[i][1] == 'o' and self.board[i][2] == 'o':
                print("O wins!")
                return True
            i += 1
        if self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x':
                print("X wins!")
                return True
        elif self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o':
                print("O wins!")
                return True
        elif self.board[0][2] == 'x' and self.board[1][1] == 'x' and self.board[2][0] == 'x':
                print("X wins!")
                return True
        elif self.board[0][2] == 'o' and self.board[1][1] == 'o' and self.board[2][0] == 'o':
                print("O wins!")
                return True

    def draw(self):
        # Check if there is a draw.
        for row in self.board:
            if '-' in row:
                return False
        return True

class stats:
    def __init__(self):
        # Keep track of winning moves and the amount of games each player wins.
        self.moves = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0}
        self.moves_two = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0}
        self.x = 0
        self.o = 0
        self.draw = 0

    def update_winner_count(self, move):
        if move == 'o':
            self.o += 1
        elif move == 'x':
            self.x += 1
        else:
            self.draw += 1

    def get_stats(self):
        # Print out useful statistics
        output = ""
        output_two = ""
        counter = 0
        while counter < 3:
            i = 0
            while i < 3:
                output = output + "(%d,%d):%d"%(i,counter,self.moves[(i,counter)])
                output_two = output_two + "(%d,%d):%d"%(i,counter,self.moves_two[(i,counter)])
                i += 1
            counter = counter + 1
        print("\nStats for move X:\n" + output + "\n")
        print("\nStats for move O:\n" + output_two + "\n")
        print(f"x won {self.x} times")
        print(f"o won {self.o} times")
        print(f"There were {self.draw} draws")

    def update(self,board,num,move):
        counter = 0
        while counter < 3:
            i = 0
            while i < 3:
                if move == 'x' and board[i][counter] == move:
                    self.moves[(i,counter)] += num
                elif move == 'o' and board[i][counter] == move:
                    self.moves_two[(i,counter)] += num
                i += 1
            counter = counter + 1


    def update_draw(self,board):
        counter = 0
        a = random.randint(0,2)
        while counter < 3:
            i = 0
            while i < 3:
                b = random.randint(0,2)
                if b == a:
                    self.moves[(i,counter)] -= 1
                    self.moves_two[(i,counter)] -= 1
                i += 1
            counter = counter + 1

    def get_best_move(self,board,move):
        counter = 0
        row = -1
        col = -1
        while counter < 3:
            i = 0
            while i < 3:
                if i >=0 and i <=2 and counter>=0 and counter<=2:
                    if board[i][counter] == '-':
                        if row == -1 and col == -1:
                            row = i
                            col = counter
                        if self.moves[(row,col)] < self.moves[(i,counter)] and move == 'x':
                            row = i
                            col = counter
                        elif self.moves_two[(row,col)] < self.moves_two[(i,counter)] and move == 'o':
                            row = i
                            col = counter
                i += 1
            counter += 1
        return [row,col]

def random_move(tictactoe):
     row = random.randint(0,2)
     col = random.randint(0,2)
     tictactoe.set_row_col(row,col)
     while tictactoe.valid_move() == False:
         row = random.randint(0,2)
         col = random.randint(0,2)
         tictactoe.set_row_col(row,col)

def smart_move(tictactoe,statistics,move):
    row_col = statistics.get_best_move(tictactoe.get_board(),move)
    tictactoe.set_row_col(row_col[0],row_col[1])

def human_move(tictactoe):
    move = input("Please input your move in the form of row,col: ")
    row = int(move[0])
    col = int(move[2])
    tictactoe.set_row_col(row, col)
    while tictactoe.valid_move() == False:
        move = input("Invalid move, please input a new move: ")
        row = int(move[0])
        col = int (move[2])
        tictactoe.set_row_col(row,col)
    return tictactoe

def game_loop(tictactoe, statistics, move, train):
    move = 'o' # x goes first
    exit = False
    i = 0
    while i <= 10000 and exit == False:
        # Change the move.
        if move == 'x':
            move = 'o'
        else:
            move = 'x'
        # Collect data first if training is True.
        if train:
            random_move(tictactoe)
        # Play a human against against a "smart" computer
        else:
            tictactoe.print_board()
            if move == 'x':
                print("It is x turn.\n")
                smart_move(tictactoe,statistics,move)
            else:
                print("It is o turn.\n")
                tictactoe = human_move(tictactoe)
        tictactoe.set_move(move)
        if tictactoe.winner() or tictactoe.draw():
            finish_game(tictactoe, statistics, move)
            tictactoe.clear_board()
            move = 'o'
            if not train:
                quit = input("Do you want to keep playing? yes/no: ")
                if quit.lower()[0] == 'n':
                    exit = True

        i = i + 1
def finish_game(tictactoe, statistics, move):
    tictactoe.print_board()
    if tictactoe.draw():
        statistics.update_draw(tictactoe.get_board())
        statistics.update_winner_count('draw')
        tictactoe.clear_board()
    elif move == 'x':
        statistics.update(tictactoe.get_board(),-1,'o')
        statistics.update_winner_count('x')
        statistics.update(tictactoe.get_board(),1,'x')
    else:
        statistics.update(tictactoe.get_board(),-1,'x')
        statistics.update_winner_count('o')
        statistics.update(tictactoe.get_board(),1,'o')

def main():
    # Instantiate Board and Stats object.
    tictactoe = board()
    statistics = stats()
    turn = 'o' # x goes first
    train = True # Train the game first.
    game_loop(tictactoe, statistics, turn, train)
    tictactoe.clear_board()
    statistics.get_stats()
    # Play the game normally.
    game_loop(tictactoe, statistics, turn, not train)

if __name__ == '__main__':
    main()
