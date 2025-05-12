import numpy as np
from model import PCA

X = np.loadtxt('C:/Users/Admin/Desktop/data_10_dimensions.csv', delimiter=',')

#X = np.array([[1, 0, 4], [-1, 1, 4], [0, 2, 4], [2, 1, 3]])

# Initialize the PCA object with M = 2
pca = PCA(n_components=2)


# Fit the PCA model to the data
pca.fit(X)


# Transform the data to the new basis
Z = pca.transform(X)

# Project the data back to the original space
X_projected = pca.project_data(X)


print("Original Data X:")
print(X)
print("\nMean:")
print(pca.mean_)
print("\nX_norm: x - Mean")
print(X - pca.mean_)
print("\nCovariance Matrix:")
print(pca.cov_matx)
print("\nEigenvalues:")
print(pca.eigvals)
print("\nEigenvectors:")
print(pca.eigvecs)
print("\nComponents (Top 2 Eigenvectors):")
print(pca.components)
print("\nMatrix of Coordinates Z:")
print(Z)
print("\nProjected Data X:")
print(X_projected)








import matplotlib.pyplot as plt
# Visualize original data (assuming 3D for visualization)
fig = plt.figure(figsize=(12, 5))

# Original data
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X[:, 0], X[:, 1], X[:, 2])
ax1.set_title('Original Data')
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')
ax1.set_zlabel('Feature 3')


# Reduced data
ax2 = fig.add_subplot(122)
ax2.scatter(Z[:, 0], Z[:, 1])
ax2.set_title('Reduced Data (2D)')
ax2.set_xlabel('Principal Component 1')
ax2.set_ylabel('Principal Component 2')

plt.tight_layout()
plt.show()



