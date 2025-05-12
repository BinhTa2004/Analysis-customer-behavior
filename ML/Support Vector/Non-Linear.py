import numpy as np
from cvxopt import matrix, solvers

class SVM:
    def __init__(self, C=1.0, kernel='linear', gamma=1.0):
        self.C = C  # Hệ số điều chỉnh cho ràng buộc
        self.kernel = kernel
        self.gamma = gamma

    def rbf_kernel(self, X1, X2):
        # Tính toán RBF kernel
        return np.exp(-self.gamma * np.linalg.norm(X1[:, None] - X2, axis=2)**2)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Ma trận Q trong bài toán tối ưu
        Q = np.zeros((n_samples, n_samples))
        
        # Sử dụng kernel
        if self.kernel == 'linear':
            for i in range(n_samples):
                for j in range(n_samples):
                    Q[i, j] = y[i] * y[j] * np.dot(X[i], X[j])
        elif self.kernel == 'rbf':
            K = self.rbf_kernel(X, X)
            for i in range(n_samples):
                for j in range(n_samples):
                    Q[i, j] = y[i] * y[j] * K[i, j]

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

        if self.kernel == 'linear':
            self.w = np.sum(self.alpha[:, None] * self.sv_y[:, None] * self.sv_X, axis=0)
            self.b = np.mean(self.sv_y - np.dot(self.sv_X, self.w))
        else:
            self.b = np.mean(self.sv_y - np.dot(self.rbf_kernel(self.sv_X, self.sv_X), self.alpha))

    def predict(self, X):
        if self.kernel == 'linear':
            linear_output = np.dot(X, self.w) - self.b
        elif self.kernel == 'rbf':
            K = self.rbf_kernel(X, self.sv_X)
            linear_output = np.dot(K, self.alpha) - self.b
        return np.sign(linear_output)

if __name__ == "__main__":

    X = np.array([[2, 3], [3, 3], [5, 1], [6, -1]])
    y = np.array([1, 1, -1, -1])

    svm = SVM(C=1.0, kernel='rbf', gamma=0.5)
    svm.fit(X, y)

    X_new = np.array([[4, 2]])
    predictions = svm.predict(X_new)
    print("Dự đoán cho điểm mới (4, 2):", "Lớp +1" if predictions == 1 else "Lớp -1")