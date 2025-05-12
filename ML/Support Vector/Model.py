import numpy as np
from cvxopt import matrix, solvers

class SVM:
    def __init__(self, C=1.0):
        self.C = C  # Hệ số điều chỉnh cho ràng buộc

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Ma trận Q trong bài toán tối ưu
        Q = np.zeros((n_samples, n_samples))
        for i in range(n_samples):
            for j in range(n_samples):
                Q[i, j] = y[i] * y[j] * np.dot(X[i], X[j])

        # Chuyển đổi thành ma trận cvxopt
        P = matrix(Q)
        q = matrix(-np.ones((n_samples, 1)))
        G = matrix(np.vstack((-np.eye(n_samples), np.eye(n_samples))))
        h = matrix(np.hstack((np.zeros(n_samples), np.ones(n_samples) * self.C)))
        A = matrix(y, (1, n_samples), 'd')
        b = matrix(0.0)

        # Giải bài toán tối ưu
        sol = solvers.qp(P, q, G, h, A, b)
        self.alpha = np.array(sol['x']).flatten()

        # Chỉ lấy các giá trị alpha > 0 (support vectors)
        sv = self.alpha > 1e-6
        self.alpha = self.alpha[sv]
        self.sv_X = X[sv]
        self.sv_y = y[sv]

        # Tính vector w
        self.w = np.sum(self.alpha[:, None] * self.sv_y[:, None] * self.sv_X, axis=0)

        # Tính bias b
        self.b = np.mean(self.sv_y - np.dot(self.sv_X, self.w))

    def predict(self, X):
        linear_output = np.dot(X, self.w) - self.b
        return np.sign(linear_output)
