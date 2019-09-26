import random
import numpy as np
import copy
from tictactoe import tictactoe as ttt

def random_move(tictactoe):
    # Generate a random and valid move.
     row = random.randint(0,2)
     col = random.randint(0,2)
     tictactoe.set_row_col(row,col)
     while not tictactoe.valid_move():
         row = random.randint(0,2)
         col = random.randint(0,2)
         tictactoe.set_row_col(row,col)

def smart_move(tictactoe,statistics,move):
    # Generate a smart move that uses the trained model.
    # Convert dict_board to numpy array.
    dict_board = tictactoe.board_as_dict()
    lst_board = []
    for i in dict_board:
        lst_board += [dict_board[i]]
    arr_board = np.array(lst_board)

    # Get available moves.
    moves = tictactoe.get_available_moves()

    # Define list of numpy arrays for data.
    data_lst = []

    # Fill data_lst to test different combinations.
    for move in moves:
        data_lst += [np.append(arr_board, np.array([move]))]

    # Define a list that will hold our potential moves.
    viable_moves = []
    prediction_to_beat = -2

    # Make a prediction for each set of data and move.
    for data in data_lst:
        prediction = statistics.model.predict(np.array([data]))
        predict = sum(prediction)

        # Better prediction - overwrite the previous moves.
        if predict > prediction_to_beat:
            prediction_to_beat = predict
            viable_moves.clear()
            viable_moves += [(data[len(data)-1], predict)]

        # Same prediction - add to list of moves.
        elif predict == prediction_to_beat:
            # Store the move.
            viable_moves += [(data[len(data)-1], predict)]

    # Print out the model prediction.
    if prediction_to_beat == -1:
        print("Model believes this game will lose...")
    elif prediction_to_beat == 0:
        print("Model believes this game will tie...")
    else:
        print("Model believes this game will win...")

    # Randomly select from the viable moves
    random.shuffle(viable_moves)
    print("Randomly selecting from the following moves...", viable_moves)
    move = viable_moves[0][0]
    print("Move selected...", move)

    # Convert to row, col.
    col = move%3
    row = (move - col) / 3

    # Set the move
    tictactoe.set_row_col(int(row),(col))

def heuristic_move(tictactoe, player):
    # Heuristic -
    ## 1. Select a move if it results in a win.
    ## 2. Block an opponent from winning.
    tic = ttt()
    tic.board = copy.deepcopy(tictactoe.board)
    moves = tic.get_available_moves()

    # Select a move if it wins results in a win.
    for move in moves:
        tic.board = copy.deepcopy(tictactoe.board)
        col = int(move%3)
        row = int((move - col) / 3)
        tic.set_row_col(row,col)
        tic.set_move(player)
        if tic.winner():
            tictactoe.set_row_col(row,col)
            return

    # Set the opponent player.
    opponent = 'o'
    if player == 'o':
        opponent = 'x'

    # Check if opponent will win in any spot. If so, select that move.
    for move in moves:
        tic.board = copy.deepcopy(tictactoe.board)
        col = int(move%3)
        row = int((move - col) / 3)
        tic.set_row_col(row,col)
        tic.set_move(opponent)
        if tic.winner():
            tictactoe.set_row_col(row,col)
            return

    # Select a random move if no moves are beneficial.
    random_move(tictactoe)

def human_move(tictactoe):
    # Prompt the user for a move.
    available_moves = tictactoe.get_available_moves()
    formatted_moves = []
    for move in available_moves:
        col = int(move%3)
        row = int((move - col) / 3)
        formatted_moves += [f"[{row},{col}]"]

    # Ask for a move to be inputted and check bad cases.
    print(f"Your available moves are: {', '.join(formatted_moves)}")
    move = input("Please input your move in the form of row,col: ")

    # Make sure the input is not weird.
    good_input = False
    while not good_input:
        if len(move) != 3:
            move = input("Opps you messed up! Retype: ")
        else:
            good_input = True

    # Set the move and make sure the move is valid.
    row = int(move[0])
    col = int(move[2])
    tictactoe.set_row_col(row, col)
    while not tictactoe.valid_move():
        move = input("Invalid move, please input a new move: ")
        row = int(move[0])
        col = int (move[2])
        tictactoe.set_row_col(row,col)
