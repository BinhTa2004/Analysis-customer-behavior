import numpy as np


# Hàm sigmoid
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Hàm tính mất mát (Binary Cross-Entropy Loss)
def compute_loss(X, y, w, b):
    N = len(y)  # Số mẫu
    z = np.dot(X, w) + b  # Giá trị z
    h = sigmoid(z)  # Xác suất dự đoán
    # Cross-entropy loss
    loss = -(1 / N) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return loss


# Gradient của loss function
def compute_gradients(X, y, w, b):
    N = len(y)
    z = np.dot(X, w) + b
    h = sigmoid(z)  # Xác suất dự đoán
    # Gradient với w và b
    dw = (1 / N) * np.dot(X.T, (h - y))  # Gradient w.r.t. w
    db = (1 / N) * np.sum(h - y)  # Gradient w.r.t. b
    return dw, db


# Hàm huấn luyện Logistic Regression
def logistic_regression(X, y, learning_rate=0.01, epochs=1000):
    n_features = X.shape[1]  # Số đặc trưng
    w = np.zeros(n_features)  # Khởi tạo w ban đầu là 0
    b = 0  # Khởi tạo b ban đầu là 0
    losses = []  # Lưu loss mỗi epoch

    for epoch in range(epochs):
        # Tính toán gradients
        dw, db = compute_gradients(X, y, w, b)

        # Cập nhật tham số
        w -= learning_rate * dw
        b -= learning_rate * db

        # Tính loss
        loss = compute_loss(X, y, w, b)
        losses.append(loss)

        # Theo dõi quá trình học
        if epoch % 100 == 0 or epoch == epochs - 1:
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")

    return w, b, losses


# Hàm dự đoán
def predict(X, w, b, threshold=0.5):
    z = np.dot(X, w) + b
    probabilities = sigmoid(z)  # Xác suất dự đoán
    return (probabilities >= threshold).astype(int)  # Chuyển thành nhãn 0 hoặc 1


# Dữ liệu mẫu (2 đặc trưng, nhãn nhị phân)
X = np.array([[0.5, 1.5],
              [1.0, 1.0],
              [1.5, 0.5],
              [3.0, 2.5],
              [2.0, 3.0],
              [3.5, 4.5]])
y = np.array([0, 0, 0, 1, 1, 1])  # Nhãn thực tế

# Huấn luyện mô hình
learning_rate = 0.1
epochs = 1000
w, b, losses = logistic_regression(X, y, learning_rate, epochs)

# Dự đoán
X_new = np.array([[1.5, 2.0], [3.0, 3.0]])  # Dữ liệu mới
predictions = predict(X_new, w, b)
print("Dự đoán nhãn:", predictions)















