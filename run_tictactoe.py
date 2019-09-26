from tictactoe import tictactoe as ttt
from model_creation import model_creation
from game_loop import game_loop

def main():
    DATA_EXISTS = True # Is there a csv file that exists with data in it?
    TRAIN = True # Should we Train and Collect Data?
    LOOP = 100000 # Number of moves to collect data for.

    # Instance of tic-tac-toe and model.
    tictactoe = ttt()
    statistics = model_creation()

    # Train if we want to collect Data.
    if TRAIN:
        print(f"Collecting data... Running {LOOP} turns. Please wait...")
        game_loop(tictactoe, statistics, TRAIN, loops = LOOP, data_exists = DATA_EXISTS)

    # Train Model
    print("Training model...")
    tictactoe.clear_board()
    """
    Select from the following models...
    Decision Tree Classifier: model_choice = "dt"
    KNN: model_choice = "knn"
    XGBoost : model_choice = "xgb"
    GuassianNB : model_choice = "nbayes"
    """
    model_choice = "dt"
    statistics.train_model(model_choice)

    # Play against the model.
    print("We can play now!")
    TRAIN = False
    game_loop(tictactoe, statistics, TRAIN, model_choice = model_choice)

if __name__ == '__main__':
    main()
