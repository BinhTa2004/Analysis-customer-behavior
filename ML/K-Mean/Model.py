import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

class KMeans:
    def __init__(self, k, max_iter = 100, tol = 1e-4):
        self.K = k
        self.max_iters = max_iter
        self.tol = tol
        self.controids = None
        self.label = None
    
    # Hàm tính khoảng cách Euclid (L2 norm)
    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))
    
    # Hàm cập nhật tâm cụm (tính trung bình cộng)
    def update_centroids(self, X, labels):
        centroids = np.zeros((self.K, X.shape[1]))  # Khởi tạo mảng chứa các tâm cụm

        for i in range(self.K):
            # Lấy ra các điểm trong cụm thứ i và tính trung bình
            points_in_cluster = X[labels == i]
            centroids[i] = np.mean(points_in_cluster, axis=0)
        return centroids
    
    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.K, replace=False)]

        for i in range(self.max_iters):
            # Bước 2: Gán mỗi điểm dữ liệu vào cụm gần nhất
            distances = cdist(X, self.centroids)
            self.labels = np.argmin(distances, axis=1)
        
            # Bước 3: Cập nhật lại tâm cụm
            new_centroids = self.update_centroids(X, self.labels)
        
            # Kiểm tra xem tâm cụm có thay đổi ít không
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                print(f"Hàm mất mát hội tụ sau {i+1} vòng lặp.")
                break

            self.centroids = new_centroids
    
        return self.centroids, self.labels
    