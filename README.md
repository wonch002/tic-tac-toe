
# Tic-Tac-Toe
### Author and Date
Cameron Wonchoba - 09/21/2019

### What is tic-tac-toe?
Tic-Tac-Toe is a two player game that involves a simple strategy. Try to win the
game by connecting three in a row, and try and prevent your opponent from
connecting three in a row.

### What does this program do?
In this program, I've attempted to teach the computer which moves are
better than others at certain states in the game. This is done by letting the
computer randomly play against itself for 10,000 moves (this can be adjusted). During these iterations,
the following data is collected and recorded into data.csv:
* The state of the board when a move is made.
* The move that the player makes.
* Whether that moves ends up as a Win, Draw, or Loss.

Using the data collected, the computer generates several models:
* DecisionTreeClassifier
* K-Nearest Neighbors
* XGBoost
* Guassian Naive Bayes

These models are pulled from the sklearn library. I selected these models
because I have learned about them in either class or at work, and I wanted to
see how they performed on this type of data. Further, I wanted to see how they
performed against each other.

### How does it perform?
Currently, these models do not perform very well. However, the point of this
program was for me to learn and practice the following:
* How to collect data.
* How to perform Machine Learning on said data-set.
* Gain practice using various packages such as:
  * pandas
  * numpy
  * sklearn

Overall, the models that are trained perform quite poorly. In fact, I know that
there are various other methods that will optimize and beat tic-tac-toe
such as Alpha-Beta pruning.

### How to execute the program?
The following packages are needed to run this program:
* random
* numpy
* pandas
* sklearn
* xgboost

After these dependencies are met, execute the following in the terminal:

* `python3 -i run_tictactoe.py`

To see results of each model, and how all of the files work together, navigate
to [tic-tac-toe](tictactoe_nb.ipynb), which is a Jupyter Notebook that has
annotations and analysis for all methods and model results. Additionally, two
sample games are demonstrated for each model to show an example of what kind of
moves each model makes.
