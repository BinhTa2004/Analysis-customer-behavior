# # decision_tree.py
#
# import numpy as np
#
# class DecisionTreeNode:
#     def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
#         self.feature = feature
#         self.threshold = threshold
#         self.left = left
#         self.right = right
#         self.value = value
#
# def mean_squared_error(y):
#     mean_y = np.mean(y)
#     return np.mean((y - mean_y) ** 2)
#
# def split(X, y, feature, threshold):
#     left_mask = X[:, feature] <= threshold
#     right_mask = X[:, feature] > threshold
#     return X[left_mask], X[right_mask], y[left_mask], y[right_mask]
#
# def best_split(X, y):
#     m, n = X.shape
#     if m <= 1:
#         return None, None
#
#     best_mse = float('inf')
#     best_feature, best_threshold = None, None
#
#     for feature in range(n):
#         thresholds = np.unique(X[:, feature])
#         for threshold in thresholds:
#             left_X, right_X, left_y, right_y = split(X, y, feature, threshold)
#             if len(left_y) > 0 and len(right_y) > 0:
#                 mse = (len(left_y) * mean_squared_error(left_y) + len(right_y) * mean_squared_error(right_y)) / m
#                 if mse < best_mse:
#                     best_mse = mse
#                     best_feature = feature
#                     best_threshold = threshold
#
#     return best_feature, best_threshold
#
# def build_tree(X, y, depth=0, max_depth=None):
#     predicted_value = np.mean(y)
#     node = DecisionTreeNode(value=predicted_value)
#
#     if depth < max_depth:
#         feature, threshold = best_split(X, y)
#         if feature is not None:
#             left_X, right_X, left_y, right_y = split(X, y, feature, threshold)
#             node.feature = feature
#             node.threshold = threshold
#             node.left = build_tree(left_X, left_y, depth + 1, max_depth)
#             node.right = build_tree(right_X, right_y, depth + 1, max_depth)
#
#     return node
#
# def predict(node, X):
#     if node.value is not None:
#         return node.value
#
#     feature_value = X[node.feature]
#     branch = node.left if feature_value <= node.threshold else node.right
#     return predict(branch, X)






#
# import numpy as np
#
# class DecisionTreeNode:
#     def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
#         self.feature = feature
#         self.threshold = threshold
#         self.left = left
#         self.right = right
#         self.value = value
#
# def mean_squared_error(y):
#     mean_y = np.mean(y)
#     return np.mean((y - mean_y) ** 2)
#
# def split(X, y, feature, threshold):
#     left_mask = X[:, feature] <= threshold
#     right_mask = X[:, feature] > threshold
#     return X[left_mask], X[right_mask], y[left_mask], y[right_mask]
#
# def best_split(X, y):
#     m, n = X.shape
#     if m <= 1:
#         return None, None
#
#     best_mse = float('inf')
#     best_feature, best_threshold = None, None
#
#     for feature in range(n):
#         thresholds = np.unique(X[:, feature])
#         for threshold in thresholds:
#             left_X, right_X, left_y, right_y = split(X, y, feature, threshold)
#             if len(left_y) > 0 and len(right_y) > 0:
#                 mse = (len(left_y) * mean_squared_error(left_y) + len(right_y) * mean_squared_error(right_y)) / m
#                 if mse < best_mse:
#                     best_mse = mse
#                     best_feature = feature
#                     best_threshold = threshold
#
#     return best_feature, best_threshold
#
# def build_tree(X, y, depth=0, max_depth=None):
#     predicted_value = np.mean(y)
#     node = DecisionTreeNode(value=predicted_value)
#
#     print(f"Depth {depth}: Predicted value = {predicted_value}")
#
#     if depth < max_depth:
#         feature, threshold = best_split(X, y)
#         if feature is not None:
#             left_X, right_X, left_y, right_y = split(X, y, feature, threshold)
#             node.feature = feature
#             node.threshold = threshold
#             print(f"Depth {depth}: Splitting on feature {feature} with threshold {threshold}")
#             node.left = build_tree(left_X, left_y, depth + 1, max_depth)
#             node.right = build_tree(right_X, right_y, depth + 1, max_depth)
#
#     return node
#
# def predict(node, X):
#     if node.value is not None:
#         return node.value
#
#     feature_value = X[node.feature]
#     branch = node.left if feature_value <= node.threshold else node.right
#     return predict(branch, X)
#
# def print_tree(node, depth=0):
#     indent = "  " * depth
#     if node.value is not None:
#         print(f"{indent}Leaf: Value = {node.value}")
#     else:
#         print(f"{indent}Split: Feature = {node.feature}, Threshold = {node.threshold}")
#         print_tree(node.left, depth + 1)
#         print_tree(node.right, depth + 1)



# decision_tree.py

import numpy as np
import matplotlib.pyplot as plt

class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

def mean_squared_error(y):
    mean_y = np.mean(y)
    return np.mean((y - mean_y) ** 2)

def split(X, y, feature, threshold):
    left_mask = X[:, feature] <= threshold
    right_mask = X[:, feature] > threshold
    return X[left_mask], X[right_mask], y[left_mask], y[right_mask]

def best_split(X, y):
    m, n = X.shape
    if m <= 1:
        return None, None

    best_mse = float('inf')
    best_feature, best_threshold = None, None

    for feature in range(n):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_X, right_X, left_y, right_y = split(X, y, feature, threshold)
            if len(left_y) > 0 and len(right_y) > 0:
                mse = (len(left_y) * mean_squared_error(left_y) + len(right_y) * mean_squared_error(right_y)) / m
                if mse < best_mse:
                    best_mse = mse
                    best_feature = feature
                    best_threshold = threshold

    return best_feature, best_threshold

def build_tree(X, y, depth=0, max_depth=None):
    predicted_value = np.mean(y)
    node = DecisionTreeNode(value=predicted_value)

    print(f"Depth {depth}: Predicted value = {predicted_value}")

    if depth < max_depth:
        feature, threshold = best_split(X, y)
        if feature is not None:
            left_X, right_X, left_y, right_y = split(X, y, feature, threshold)
            node.feature = feature
            node.threshold = threshold
            print(f"Depth {depth}: Splitting on feature {feature} with threshold {threshold}")
            node.left = build_tree(left_X, left_y, depth + 1, max_depth)
            node.right = build_tree(right_X, right_y, depth + 1, max_depth)

    return node

def predict(node, X):
    if node.value is not None:
        return node.value

    feature_value = X[node.feature]
    branch = node.left if feature_value <= node.threshold else node.right
    return predict(branch, X)

def print_tree(node, depth=0, feature_names=None):
    indent = "  " * depth
    if node.value is not None:
        print(f"{indent}Leaf: Value = {node.value:.2f}")
    else:
        feature_name = feature_names[node.feature] if feature_names else f"Feature {node.feature}"
        print(f"{indent}Split: {feature_name} <= {node.threshold:.2f}")
        print_tree(node.left, depth + 1, feature_names)
        print_tree(node.right, depth + 1, feature_names)

def plot_tree(node, ax, x=0, y=0, dx=1, dy=1, feature_names=None):
    if node.value is not None:
        ax.text(x, y, f"Value = {node.value:.2f}", ha='center', va='center', bbox=dict(facecolor='lightblue', alpha=0.5))
    else:
        feature_name = feature_names[node.feature] if feature_names else f"Feature {node.feature}"
        ax.text(x, y, f"{feature_name} <= {node.threshold:.2f}", ha='center', va='center', bbox=dict(facecolor='lightgreen', alpha=0.5))
        ax.plot([x, x - dx], [y, y - dy], 'k-')
        plot_tree(node.left, ax, x - dx, y - dy, dx / 2, dy / 2, feature_names)
        ax.plot([x, x + dx], [y, y - dy], 'k-')
        plot_tree(node.right, ax, x + dx, y - dy, dx / 2, dy / 2, feature_names)

def visualize_tree(node, feature_names=None):
    fig, ax = plt.subplots(figsize=(10, 10))
    plot_tree(node, ax, feature_names=feature_names)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    plt.show()

