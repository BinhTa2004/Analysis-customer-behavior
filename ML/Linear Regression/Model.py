import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
class LinearRegression:
    def __init__(self):
        self.W = None

    def fit(self, X, y):
        one = np.ones((X.shape[0], 1))
        Xbar = np.concatenate((one, X), axis=1)

        A = np.dot(Xbar.T, Xbar)
        b = np.dot(Xbar.T, y)
        self.W = np.dot(np.linalg.pinv(A),b)

    def predict(self, X):
        if self.W is None:
            raise Exception("You must fit before predict")
        one = np.ones((X.shape[0],1))
        Xbar = np.concatenate((one, X), axis=1)

        y_pred = np.dot(Xbar, self.W)
        return y_pred

    def evaluate(self, X, y_true):
        y_pred = self.predict(X)
        r2 = r2_score(y_true, y_pred)
        mse = mean_squared_error(y_true, y_pred)
        return r2, mse