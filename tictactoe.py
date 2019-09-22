class tictactoe:

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
                return True
            elif self.board[0][i] == 'o' and self.board[1][i] == 'o' and self.board[2][i] == 'o':
                return True
            elif self.board[i][0] == 'x' and self.board[i][1] == 'x'and self.board[i][2] == 'x':
                return True
            elif self.board[i][0] == 'o' and self.board[i][1] == 'o' and self.board[i][2] == 'o':
                return True
            i += 1
        if self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x':
                return True
        elif self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o':
                return True
        elif self.board[0][2] == 'x' and self.board[1][1] == 'x' and self.board[2][0] == 'x':
                return True
        elif self.board[0][2] == 'o' and self.board[1][1] == 'o' and self.board[2][0] == 'o':
                return True

    def get_available_moves(self):
        # Return a list of all available moves in the form an array.
        moves = []
        for i, row in enumerate(self.board):
            for j, col in enumerate(self.board):
                if self.board[i][j] == '-':
                    moves += [i*3+j]
        return moves

    def board_as_dict(self):
        dict_board = {}
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if self.board[i][j] == '-':
                    dict_board[i*3+j] = 0
                elif self.board[i][j] == 'x':
                    dict_board[i*3+j] = 1
                else:
                    dict_board[i*3+j] = 2
        return dict_board

    def draw(self):
        # Check if there is a draw.
        for row in self.board:
            if '-' in row:
                return False
        return True
