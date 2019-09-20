import random

class moves:

    def __init__(self):
        self.row = 0
        self.col = 0
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_board(self):
        return self.board

    def set_row_col(self,row,col):
        self.row = row
        self.col = col

    def valid_move(self):
        if self.row >=0 and self.row <=2 and self.col>=0 and self.col<=2:
            if self.board[self.row][self.col] == '-':
                return True
            else:
                return False

    def set_move(self,move):
            self.board[self.row][self.col] = move

    def print_board(self):
        counter = 0
        while counter < 3:
            i = 0
            print(self.board[counter][i], self.board[counter][i+1],self.board[counter][i+2])
            counter = counter + 1
        print("\n")

    def clear_board(self):
        counter = 0
        while counter < 3:
            i = 0
            while i < 3:
                self.board[i][counter] = '-'
                i += 1
            counter += 1

    def winner(self):
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
        i = 0
        while i < 3:
            counter = 0
            while counter < 3:
                if self.board[i][counter] == '-':
                    return False
                counter +=1
            i += 1
        return True


class stats:
    def __init__(self):
        self.moves = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0}
        self.moves_two = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0}


    def get_stats(self):
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
    tictactoe.set_row_col(row,col)
    while tictactoe.valid_move() == False:
        move = input("Invalid move, please input a new move: ")
        row = int(move[0])
        col = int (move[2])
        tictactoe.set_row_col(row,col)


def main():
    # counters to keep track of wins and draws
    counterrandx = 0
    countersmartx = 0
    counterrando = 0
    countersmarto = 0
    counterdrawrand = 0
    counterdrawsmart = 0
    i = 0
    tictactoe = moves()
    statistics = stats()
    move = 'o' # x goes first
    while i <= 10000:
        if move == 'x':
            move = 'o'
        else:
            move = 'x'
        random_move(tictactoe)
        tictactoe.set_move(move)
        if tictactoe.winner():
            if move == 'x':
                statistics.update(tictactoe.get_board(),-1,'o')
                counterrandx += 1
                statistics.update(tictactoe.get_board(),1,'x')
            else:
                statistics.update(tictactoe.get_board(),-1,'x')
                counterrando +=1
                statistics.update(tictactoe.get_board(),1,'o')
            tictactoe.clear_board()
            move = 'o'
        if tictactoe.draw():
            statistics.update_draw(tictactoe.get_board())
            counterdrawrand += 1
            tictactoe.clear_board()
            move = 'o'
        i = i + 1
    i = 0
    move = 'o'
    tictactoe.clear_board()
    while i <= 10000:
        if move == 'x':
            move = 'o'
        else:
            move = 'x'
        if move == 'x':
            ### UNCOMMENT FOR SMART X
            smart_move(tictactoe,statistics,move)
            ### UNCOMMENT FOR RANDOM X
            # random_move(tictactoe)
        else:
            ### UNCOMMENT FOR SMART O
            smart_move(tictactoe,statistics,move)
            ### UNCOMMENT FOR RANDOM O
            # random_move(tictactoe)
        tictactoe.set_move(move)
        if tictactoe.winner():
            if move == 'x':
                statistics.update(tictactoe.get_board(),-1,'o')
                countersmartx += 1
                statistics.update(tictactoe.get_board(),1,'x')
            else:
                statistics.update(tictactoe.get_board(),-1,'x')
                statistics.update(tictactoe.get_board(),1,'o')
                countersmarto += 1
            tictactoe.clear_board()
            move = 'o'
        if tictactoe.draw():
            statistics.update_draw(tictactoe.get_board())
            counterdrawsmart += 1
            tictactoe.clear_board()
            move = 'o'
        i = i + 1
    i = 0
    move = 'o'
    tictactoe.clear_board()
    while i <= 10000:
        if move == 'x':
            move = 'o'
        else:
            move = 'x'
        if move == 'x':
            ### UNCOMMENT FOR SMART X
            smart_move(tictactoe,statistics,move)
            ### UNCOMMENT FOR RANDOM X
            # random_move(tictactoe)
        else:
            ### UNCOMMENT FOR SMART O
            human_move(tictactoe)
            ### UNCOMMENT FOR RANDOM O
            # random_move(tictactoe)
        tictactoe.set_move(move)
        tictactoe.print_board()
        if tictactoe.winner():
            if move == 'x':
                statistics.update(tictactoe.get_board(),-1,'o')
                countersmartx += 1
                statistics.update(tictactoe.get_board(),1,'x')
            else:
                statistics.update(tictactoe.get_board(),-1,'x')
                statistics.update(tictactoe.get_board(),1,'o')
                countersmarto += 1
            tictactoe.clear_board()
            move = 'o'
        if tictactoe.draw():
            statistics.update_draw(tictactoe.get_board())
            counterdrawsmart += 1
            tictactoe.clear_board()
            move = 'o'
        i = i + 1
    statistics.get_stats()
    print("Random wins X: %d\nRandom wins O: %d\nRandom draws: %d\nSmart wins X: %d\nSmart wins O: %d\nSmart draws: %d"%(counterrandx, counterrando, counterdrawrand, countersmartx, countersmarto, counterdrawsmart))
    total_rand = counterrandx + counterrando + counterdrawrand
    total_smart = countersmartx + countersmarto + counterdrawsmart
    print("Total games random: %d\nTotal games smart: %d\n"%(total_rand,total_smart))
if __name__ == '__main__':
    main()
