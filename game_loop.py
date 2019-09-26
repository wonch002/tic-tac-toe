import random

from move_selection import random_move
from move_selection import smart_move
from move_selection import human_move
from move_selection import heuristic_move

def game_loop(tictactoe, statistics, train, loops = 10000, model_choice = None, data_exists = True):
    # Game loop where tic-tac-toe is played.

    move = 'o' # x goes first
    exit = False
    i = 0
    print_counter = 0

    while i <= loops and exit == False:
        # Print counter to track how much data has been collected.
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
            # Select a heuristic move (Might simulate a move that a human would make)
            heuristic_move(tictactoe, move)
            # Only record the stastics for 'x' moves.
            if move == 'x':
                statistics.update_temp_history(tictactoe)
            tictactoe.set_move(move)

        # Play a human against against a "smart" computer
        else:
            tictactoe.print_board()
            # If 'x' select a smart move.
            if move == 'x':
                print("It is x turn.\n")
                smart_move(tictactoe, statistics, move)
                statistics.update_temp_history(tictactoe)

            # If 'o' Human selects a move.
            else:
                print("It is o turn.\n")
                human_move(tictactoe)
            tictactoe.set_move(move)

        # Determine if there is a winner or a tie.
        if tictactoe.winner() or tictactoe.draw():
            finish_game(tictactoe, statistics, move, train, data_exists)
            tictactoe.clear_board()
            move = 'o'
            if not train:
                quit = input("Do you want to keep playing? yes/no: ")
                if quit.lower()[0] == 'n':
                    exit = True
                if not exit:
                    # Retrain model.
                    print("Retraining model...")
                    statistics.train_model(model_choice)

        i = i + 1

def finish_game(tictactoe, statistics, move, train, data_exists):
    # Finish the game and update statistics.
    if not train:
        tictactoe.print_board()
    statistics.update(move, tictactoe, data_exists)
    statistics.header = False
