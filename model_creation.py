import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
import operator

class model_creation:

    def __init__(self):
        self.moves = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0}
        self.temp_history = pd.DataFrame(columns = [0,1,2,3,4,5,6,7,8,'move','outcome'])
        self.history = pd.DataFrame(columns = [0,1,2,3,4,5,6,7,8,'move','outcome'])
        self.model = None
        self.dt = None
        self.knn = None

    def update(self, move, tictactoe):
        # Update the statistics for winners.
        if move == 'x' and tictactoe.winner():
            self.temp_history['outcome'] = 2
        elif tictactoe.draw():
            self.temp_history['outcome'] = 1
        else:
            self.temp_history['outcome'] = 0
        self.history = self.history.append(self.temp_history)
        self.temp_history = self.temp_history.iloc[0:0]

    def reset_temp_history(self):
        self.temp_history = pd.DataFrame(columns = [0,1,2,3,4,5,6,7,8,'move','outcome'])

    def update_temp_history(self, tictactoe):
        temp = {}
        for i, row in enumerate(tictactoe.board):
            for j, col in enumerate(row):
                if tictactoe.board[i][j] == '-':
                    temp[i*3+j] = 0
                elif tictactoe.board[i][j] == 'x':
                    temp[i*3+j] = 1
                else:
                    temp[i*3+j] = 2
        temp['move'] = tictactoe.get_row()*3 + tictactoe.get_col()
        temp['outcome'] = 0
        self.temp_history = self.temp_history.append(temp, ignore_index = True)

    def train_model(self, model_choice):
        data = self.history[[0,1,2,3,4,5,6,7,8, 'move']]
        target = self.history['outcome']
        target = target.astype('int')
        x_train, x_test, y_train, y_test = train_test_split(data.values, target.values, test_size = 0.5)

        # Decision Tree Classifier
        self.dt = tree.DecisionTreeClassifier()
        self.dt = self.dt.fit(x_train, y_train)
        outTree = self.dt.predict(x_test)
        print("Accuracy for Decision Tree Classifier: " + str(accuracy_score(y_test, outTree)*100)+"%")

        # KNN
        k_range = range(1,30)
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

        if model_choice == "dt":
            self.model = self.dt
        elif model_choice == "knn":
            self.model = self.knn
        else:
            raise ValueError(f"{model_choice} not yet implemented")
