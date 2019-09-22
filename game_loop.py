import random

from move_selection import random_move
from move_selection import smart_move
from move_selection import human_move

def game_loop(tictactoe, statistics, move, train, loops = 10000):
    # Game loop where tic-tac-toe is played.
    move = 'o' # x goes first
    exit = False
    i = 0
    print_counter = 0
    while i <= loops and exit == False:
        # Print counter.
        if print_counter == 1000:
            print(i)
            print_counter = 0
        print_counter += 1

        # Change the move.
        if move == 'x':
            move = 'o'
        else:
            move = 'x'
        # Collect data first if training is True.
        if train:
            random_move(tictactoe)
            statistics.update_temp_history(tictactoe)
        # Play a human against against a "smart" computer
        else:
            tictactoe.print_board()
            if move == 'x':
                print("It is x turn.\n")
                smart_move(tictactoe,statistics,move)
            else:
                print("It is o turn.\n")
                human_move(tictactoe)
        tictactoe.set_move(move)
        if tictactoe.winner() or tictactoe.draw():
            finish_game(tictactoe, statistics, move, train)
            tictactoe.clear_board()
            move = 'o'
            if not train:
                quit = input("Do you want to keep playing? yes/no: ")
                if quit.lower()[0] == 'n':
                    exit = True
        i = i + 1

def finish_game(tictactoe, statistics, move, train):
    # Finish the game and update statistics.
    if not train:
        tictactoe.print_board()
    statistics.update(move, tictactoe)
    # print(statistics.history)
