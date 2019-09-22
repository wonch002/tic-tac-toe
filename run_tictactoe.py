from tictactoe import tictactoe as ttt
from model_creation import model_creation
from game_loop import game_loop

def main():
    # Data Collection
    tictactoe = ttt()
    statistics = model_creation()
    turn = 'o' # x goes first
    train = True # Train the game first.
    loop = 10000 # Run 1000000 turns.
    print(f"Collecting data... Running {loop} turns. Please wait...")
    game_loop(tictactoe, statistics, turn, train, loops = loop)

    print("Training model...")
    # Train Model
    tictactoe.clear_board()
    # Select from two models...
    ## Decision Tree Classifier: model = "dt"
    ## KNN: model = "knn"
    model_choice = "dt"
    statistics.train_model(model_choice)

    print("We can play now!")
    # Play against the model.
    game_loop(tictactoe, statistics, turn, not train)

if __name__ == '__main__':
    main()
