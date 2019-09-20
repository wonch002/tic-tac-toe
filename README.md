#README

## Tic-Tac-Toe

Tic-Tac-Toe is a two player game that involves a simple strategy. Try to win the
game by connecting three in a row, and try and prevent your opponent from
connecting three in a row.

In this program, I've attempted to naively teach the computer which moves are
better than others. This is done by letting the computer randomly play against
itself for 10,000 moves. If a sequence of moves results in a win for that
player, then all of their moves are recorded as a win. If that sequence of moves
results in a loss, then all of their moves are recorded as a loss. After the
10,000 moves, each player will have a good idea as to which moves result in a
win and which moves result in a loss.

Using the knowledge of wins and losses, the computer generates a "smart" move to
play against its opponent. Currently, this smart move is determined by selecting
an available move that resulted in the most wins.

To run this program execute the following in a terminal:

`python3 tictactoe.py`
