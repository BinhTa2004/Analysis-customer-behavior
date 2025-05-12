import numpy as np
class PCA:

    def __init__(self, n_components):
        self.mean = None
        self.covariance_matrix = None 
        self.num_components = n_components
        self.principal_components = None
        self.eigenvalues = None
        self.eigenvectors = None
        self.num_samples, self.num_features = None, None

    def eig(self, X):
        self.eigenvalues, self.eigenvectors = np.linalg.eig(X)
        self.eigenvalues, self.eigenvectors = np.real(self.eigenvalues), np.real(self.eigenvectors)
        idx_sort = np.argsort(self.eigenvalues)[::-1]
        self.eigenvalues, self.eigenvectors = self.eigenvalues[idx_sort], self.eigenvectors[:, idx_sort]

    def fit(self, X):
        self.num_samples, self.num_features = X.shape
        # Covariance matrix
        self.mean = np.mean(X, axis=0)
        X_centered = (X - self.mean)
        self.covariance_matrix = np.dot(X_centered.T, X_centered) / self.num_samples

        # Eigenvalues, Eigenvectors
        self.eig(self.covariance_matrix)
        self.principal_components = self.eigenvectors[:, :self.num_components]

    def transform(self, X):
        X_centered = (X - self.mean)
        return X_centered @ self.principal_components

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def information_percent(self):
        proportion = self.eigenvalues / sum(self.eigenvalues)
        cumulative = proportion.cumsum()
        return cumulative[:self.num_components]

    def project_data(self, X):
        X_centered = (X - self.mean)
        projection = (self.principal_components @ self.principal_components.T @ X_centered.T).T + self.mean
        return projection