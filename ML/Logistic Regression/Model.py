import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = None
        self.b = 0
        
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
        
    def compute_loss(self, X, y):
        N = len(y)
        z = np.dot(X, self.w) + self.b
        h = self.sigmoid(z)
        loss = -(1/N) * np.sum(y * np.log(h) + (1-y) * np.log(1-h))
        return loss
        
    def compute_gradients(self, X, y):
        N = len(y)
        z = np.dot(X, self.w) + self.b
        h = self.sigmoid(z)
        dw = (1/N) * np.dot(X.T, (h-y))
        db = (1/N) * np.sum(h-y)
        return dw, db
        
    def fit(self, X, y):
        n_features = X.shape[1]
        self.w = np.zeros(n_features)
        self.b = 0
        losses = []
        
        for epoch in range(self.epochs):
            dw, db = self.compute_gradients(X, y)
            
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db
            
            loss = self.compute_loss(X, y)
            losses.append(loss)
            
            if epoch % 100 == 0 or epoch == self.epochs - 1:
                print(f"Epoch {epoch + 1}/{self.epochs}, Loss: {loss:.4f}")
                
        return losses

        
    def predict_proba(self, X):
        z = np.dot(X, self.w) + self.b
        return self.sigmoid(z)
        
    def predict(self, X, threshold=0.5):
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)


    def evaluate(self, X, y_true):
        y_pred = self.predict(X)
        accuracy = np.sum(y_pred == y_true) / len(y_true)
        return accuracy




X = np.array([[0.5, 1.5],
              [1.0, 1.0],
              [1.5, 0.5],
              [3.0, 2.5],
              [2.0, 3.0],
              [3.5, 4.5]])
y = np.array([0, 0, 0, 1, 1, 1])


model = LogisticRegression()
model.fit(X, y)
