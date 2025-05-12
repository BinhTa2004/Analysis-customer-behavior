import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

class KMeans:
    def __init__(self, k, max_iter = 500, tol = 1e-4):
        self.K = k
        self.max_iters = max_iter
        self.tol = tol
        self.controids = None
        self.label = None

    def fit(self, X):
        # Bước 1: Chọn tâm cụm ban đầu bằng KMeans++
        self.centroids = self._initialize_centroids(X)

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

    def _initialize_centroids(self, X):
        # Chọn ngẫu nhiên một điểm làm tâm cụm đầu tiên
        centroids = [X[np.random.randint(X.shape[0])]]
        
        for _ in range(1, self.K):
            # Tính khoảng cách từ các điểm đến tâm cụm đã chọn
            distances = cdist(X, np.array(centroids))
            min_distances = np.min(distances, axis=1)
            # Chọn tâm cụm tiếp theo với xác suất tỷ lệ với bình phương khoảng cách
            probabilities = min_distances ** 2
            probabilities /= probabilities.sum()
            next_centroid = X[np.random.choice(X.shape[0], p=probabilities)]
            centroids.append(next_centroid)

        return np.array(centroids)
    
    def update_centroids(self, X, labels):
        centroids = np.zeros((self.K, X.shape[1]))  # Khởi tạo mảng chứa các tâm cụm

        for i in range(self.K):
            # Lấy ra các điểm trong cụm thứ i và tính trung bình
            points_in_cluster = X[labels == i]
            centroids[i] = np.mean(points_in_cluster, axis=0)
        return centroids