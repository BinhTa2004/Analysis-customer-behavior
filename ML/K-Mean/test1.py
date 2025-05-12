import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# Hàm tính khoảng cách Euclid (L2 norm)
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# Hàm cập nhật tâm cụm (tính trung bình cộng)
def update_centroids(X, labels, k):
    centroids = np.zeros((k, X.shape[1]))  # Khởi tạo mảng chứa các tâm cụm
    for i in range(k):
        # Lấy ra các điểm trong cụm thứ i và tính trung bình
        points_in_cluster = X[labels == i]
        centroids[i] = np.mean(points_in_cluster, axis=0)
    return centroids

# Hàm tính toán hàm mất mát
def compute_loss(X, labels, centroids):
    loss = 0
    for i in range(X.shape[0]):
        loss += np.linalg.norm(X[i] - centroids[labels[i]])**2
    return loss

# Cập nhật lại hàm kmeans với việc theo dõi hàm mất mát
def kmeans_with_loss(X, k, max_iters=100, tol=1e-4):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    prev_loss = float('inf')
    
    for i in range(max_iters):
        # Gán mỗi điểm vào cụm gần nhất
        distances = cdist(X, centroids)
        labels = np.argmin(distances, axis=1)
        
        # Cập nhật lại tâm cụm
        new_centroids = update_centroids(X, labels, k)
        
        # Tính lại hàm mất mát
        loss = compute_loss(X, labels, new_centroids)
        
        # Kiểm tra sự hội tụ
        if np.abs(prev_loss - loss) < tol:
            print(f"Hàm mất mát hội tụ sau {i+1} vòng lặp.")
            break
        
        prev_loss = loss
        centroids = new_centroids
    
    return centroids, labels


def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()


means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis=0)
K = 3

centroids, labels = kmeans_with_loss(X, K)
print('Centers found by our algorithm:')
print(centroids)

# kmeans_display(X, labels)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, linewidths=3)
plt.title('K-means Clustering Results')
plt.show()
