import operator

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

class model_creation:

    def __init__(self):
        self.moves = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0}
        self.temp_history = pd.DataFrame(columns = [0,1,2,3,4,5,6,7,8,'move','outcome'])
        self.header = True
        self.history = None
        # Different types of models.
        self.model = None
        self.dt = None
        self.knn = None
        self.xgb = None
        self.nb = None

    def update(self, move, tictactoe, data_exists):
        # Update the statistics for winners.

        # Win = 1
        if move == 'x' and tictactoe.winner():
            self.temp_history['outcome'] = 1
        # Tie = 0
        elif tictactoe.draw():
            self.temp_history['outcome'] = 0
        # Loss = 0
        else:
            self.temp_history['outcome'] = -1

        # Write to csv and then reset temp_history
        if self.header and not data_exists:
            self.temp_history.to_csv('data.csv',index=False)
        else:
            with open('data.csv', 'a') as f:
                self.temp_history.to_csv(f, header = False, index = False)

        self.temp_history = self.temp_history.iloc[0:0]

    def update_temp_history(self, tictactoe):
        # Update temporary board state and moves.

        temp = {}
        # Update the state of the board.
        for i, row in enumerate(tictactoe.board):
            for j, col in enumerate(row):
                if tictactoe.board[i][j] == '-':
                    temp[i*3+j] = 0
                elif tictactoe.board[i][j] == 'x':
                    temp[i*3+j] = 1
                else:
                    temp[i*3+j] = 2
        # Set the move.
        temp['move'] = tictactoe.get_row()*3 + tictactoe.get_col()
        # We do not know the outcome yet. Randomly set to None.
        temp['outcome'] = None

        # Append the old temp_hisotry with the next temp_history.
        self.temp_history = self.temp_history.append(temp, ignore_index = True)

    def train_model(self, model_choice):
        # Train our model with the data found in data.csv.
        self.history = pd.read_csv('data.csv')

        data = self.history[['0','1','2','3','4','5','6','7','8', 'move']]
        target = self.history['outcome']
        target = target.astype('int')

        # Split the training data into to sets.
        x_train, x_test, y_train, y_test = train_test_split(data.values, target.values, test_size = 0.5)

        # Decide which model to train...

        # Decision Tree Classifier
        if model_choice == "dt":
            self.dt = tree.DecisionTreeClassifier()
            self.dt = self.dt.fit(x_train, y_train)
            outTree = self.dt.predict(x_test)
            self.model = self.dt
            print("Accuracy for Decision Tree Classifier: " + str(accuracy_score(y_test, outTree)*100)+"%")

        # KNN
        elif model_choice == "knn":
            k_range = range(1,20)
            scores = {}
            scores_list = []
            for k in k_range:
                knn = KNeighborsClassifier(n_neighbors=k)
                knn.fit(x_train, y_train)
                y_pred = knn.predict(x_test)
                scores[k] = accuracy_score(y_test, y_pred)
                print(f"K = {k} accuracy = {accuracy_score(y_test, y_pred)}")
                scores_list.append(accuracy_score(y_test, y_pred))
            max_knn = max(scores.items(), key = operator.itemgetter(1))[0]
            print(f"Max Accuracy for KNN: K = {max_knn} Score = {scores[max_knn]}")
            self.knn = KNeighborsClassifier(n_neighbors=max_knn)
            self.knn.fit(x_train, y_train)
            self.model = self.knn

        ## XGBoost
        elif model_choice == "xgb":
            self.xgb = XGBClassifier()
            self.xgb = self.xgb.fit(x_train, y_train)
            y_pred = self.xgb.predict(x_test)
            predictions = [round(value) for value in y_pred]
            accuracy = accuracy_score(y_test, predictions)
            print("Accuracy for XGBoost: " + str(accuracy * 100) + "%")
            self.model = self.xgb

        ## Naive Bayes
        elif model_choice == "nbayes":
            self.nb = GaussianNB()
            self.nb = self.nb.fit(x_train, y_train)
            y_pred = self.nb.predict(data.values)
            print(y_pred)
            print(f"Number of mislabled points for GaussianNB: {(target.values != y_pred).sum()} out of {data.shape[0]}")
            print(f"Accuracy is {(data.shape[0] - (target.values != y_pred).sum()) / data.shape[0] * 100}%")
            self.model = self.nb

        ## Model not implemented.
        else:
            raise ValueError(f"{model_choice} not yet implemented")
