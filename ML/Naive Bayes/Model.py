import numpy as np
from collections import defaultdict

class NaiveBayes:
    def __init__(self):
        self.class_probs = {}  # P(y)
        self.feature_probs = {}  # P(x|y)
        self.classes = None
        
    def fit(self, X, y):
        self.classes = np.unique(y)
        n_samples = len(y)
        
        # Calculate class probabilities P(y)
        for c in self.classes:
            self.class_probs[c] = np.sum(y == c) / n_samples
            
        # Calculate feature probabilities P(x|y) for each class
        for c in self.classes:
            class_samples = X[y == c]
            self.feature_probs[c] = {}
            
            # For each feature, calculate mean and variance
            for feature in range(X.shape[1]):
                feature_values = class_samples[:, feature]
                self.feature_probs[c][feature] = {
                    'mean': np.mean(feature_values),
                    'var': np.var(feature_values) + 1e-9  # Add small value to avoid division by zero
                }
    
    def _calculate_likelihood(self, x, mean, var):
        exponent = np.exp(-((x - mean) ** 2) / (2 * var))
        return (1 / np.sqrt(2 * np.pi * var)) * exponent
    
    def predict(self, X):
        """
        Predict class labels for samples in X
        
        Parameters:
        X: array-like of shape (n_samples, n_features)
        
        Returns:
        y_pred: array-like of shape (n_samples,)
        """
        y_pred = []
        
        for x in X:
            class_scores = {}
            
            # Calculate posterior probability for each class
            for c in self.classes:
                # Start with prior probability
                class_scores[c] = np.log(self.class_probs[c])
                
                # Add log-likelihood for each feature
                for feature in range(len(x)):
                    mean = self.feature_probs[c][feature]['mean']
                    var = self.feature_probs[c][feature]['var']
                    likelihood = self._calculate_likelihood(x[feature], mean, var)
                    class_scores[c] += np.log(likelihood + 1e-9)  # Add small value to avoid log(0)
            
            # Select class with highest posterior probability
            y_pred.append(max(class_scores, key=class_scores.get))
        
        return np.array(y_pred)


