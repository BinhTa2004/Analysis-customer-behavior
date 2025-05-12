import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
class KMeans:
    def __init__(self, k, max_iters=100, tol=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
        self.centroids = None
        self.labels = None

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

    def update_centroids(self, X, labels):
        centroids = np.zeros((self.k, X.shape[1]))
        for i in range(self.k):
            points_in_cluster = X[labels == i]
            centroids[i] = np.mean(points_in_cluster, axis=0)
        return centroids
    
    # Hàm tính toán hàm mất mát
    def compute_loss(self, X, labels, centroids):
        loss = 0
        for i in range(X.shape[0]):
            loss += np.linalg.norm(X[i] - centroids[labels[i]])**2
        return loss

    # Cập nhật lại hàm kmeans với việc theo dõi hàm mất mát
    def fit(self,X):
        centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]
        prev_loss = float('inf')
    
        for i in range(self.max_iters):
            # Gán mỗi điểm vào cụm gần nhất
            distances = cdist(X, self.centroids)
            self.labels = np.argmin(distances, axis=1)
        
            # Cập nhật lại tâm cụm
            new_centroids = self.update_centroids(X, self.labels)
        
            # Tính lại hàm mất mát
            loss = self.compute_loss(X, self.labels, new_centroids)
        
            # Kiểm tra sự hội tụ
            if np.abs(prev_loss - loss) < self.tol:
                print(f"Hàm mất mát hội tụ sau {i+1} vòng lặp.")
                break
        
            prev_loss = loss
            self.centroids = new_centroids
    
        return self.centroids, self.labels


    def display(self, X):
        if self.centroids is None or self.labels is None:
            raise Exception("Bạn phải chạy fit() trước khi hiển thị")
            
        X0 = X[self.labels == 0, :]
        X1 = X[self.labels == 1, :]
        X2 = X[self.labels == 2, :]
        
        plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
        plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
        plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)

        plt.axis('equal')
        plt.plot()
        plt.show()
