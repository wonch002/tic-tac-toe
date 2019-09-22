import random
import numpy as np

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
    # Generate a smart move.
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

    viable_moves = []
    prediction_to_beat = -1

    # Make a prediction for each data_list and capture the best move.
    for data in data_lst:
        prediction = statistics.model.predict(np.array([data]))
        prediction = sum(prediction)

        if prediction == prediction_to_beat:
            # Store the move.
            viable_moves += [data[len(data)-1]]
        elif prediction > prediction_to_beat:
            prediction_to_beat = prediction
            viable_moves.clear()
            viable_moves += [data[len(data)-1]]

    print("Model believes this game will...", prediction_to_beat)
    # Randomly select from the viable moves
    random.shuffle(viable_moves)
    print(viable_moves)
    move = viable_moves[0]

    # Convert to row, col.
    col = move%3
    row = (move - col) / 3

    # Set the move
    tictactoe.set_row_col(int(row),(col))

def human_move(tictactoe):
    # Prompt the user for a move.
    available_moves = tictactoe.get_available_moves()
    formatted_moves = []
    for move in available_moves:
        col = int(move%3)
        row = int((move - col) / 3)
        formatted_moves += [f"[{row},{col}]"]
    print(f"Your available moves are: {', '.join(formatted_moves)}")
    move = input("Please input your move in the form of row,col: ")
    row = int(move[0])
    col = int(move[2])
    tictactoe.set_row_col(row, col)
    while not tictactoe.valid_move():
        move = input("Invalid move, please input a new move: ")
        row = int(move[0])
        col = int (move[2])
        tictactoe.set_row_col(row,col)
