# class Regression:
#     def __init__(self):
#         self.x = []
#         self.y = []
#         self.coeff = 0
#         self.constTerm = 0
#         self.sum_xy = 0
#         self.sum_x = 0
#         self.sum_y = 0
#         self.sum_x_square = 0
#         self.sum_y_square = 0
#
#     def calculate_coefficient(self):
#         N = len(self.x)
#         numerator = (N * self.sum_xy - self.sum_x * self.sum_y)
#         denominator = (N * self.sum_x_square - self.sum_x * self.sum_x)
#         self.coeff = numerator / denominator
#
#     def calculate_constant_term(self):
#         N = len(self.x)
#         numerator = (self.sum_y * self.sum_x_square - self.sum_x * self.sum_xy)
#         denominator = (N * self.sum_x_square - self.sum_x * self.sum_x)
#         self.constTerm = numerator / denominator
#
#     def size_of_data(self):
#         return len(self.x)
#
#     def coefficient(self):
#         if self.coeff == 0:
#             self.calculate_coefficient()
#         return self.coeff
#
#     def constant(self):
#         if self.constTerm == 0:
#             self.calculate_constant_term()
#         return self.constTerm
#
#     def print_best_fitting_line(self):
#         if self.coeff == 0 and self.constTerm == 0:
#             self.calculate_coefficient()
#             self.calculate_constant_term()
#         print(f"The best fitting line is y = {self.coeff}x + {self.constTerm}")
#
#     def take_input(self, n):
#         for _ in range(n):
#             xi, yi = map(float, input().split(','))
#             self.sum_xy += xi * yi
#             self.sum_x += xi
#             self.sum_y += yi
#             self.sum_x_square += xi * xi
#             self.sum_y_square += yi * yi
#             self.x.append(xi)
#             self.y.append(yi)
#
#     def show_data(self):
#         print("_" * 62)
#         print("\n")
#         print(f"|{'X':>15}{'':>5} {'Y':>15}{'':>5}{'|':>20}")
#
#         for i in range(len(self.x)):
#             print(f"|{self.x[i]:>20} {self.y[i]:>20}{'|':>20}")
#
#         print("_" * 62)
#         print("\n")
#
#     def predict(self, x):
#         return self.coeff * x + self.constTerm
#
#     def error_square(self):
#         ans = 0
#         for i in range(len(self.x)):
#             ans += (self.predict(self.x[i]) - self.y[i]) ** 2
#         return ans
#
#     def error_in(self, num):
#         for i in range(len(self.x)):
#             if num == self.x[i]:
#                 return self.y[i] - self.predict(self.x[i])
#         return 0
#
# # Driver code
# if __name__ == "__main__":
#     import sys
#     #sys.stdin = open("C:/Users/Admin/Desktop/input.csv", "r")
#     sys.stdin = open("input.txt", "r")
#
#     reg = Regression()
#
#     # Number of pairs of (xi, yi) in the dataset
#     n = int(input())
#
#     # Calling function take_input to take input of n pairs
#     reg.take_input(n)
#
#     # Printing the best fitting line
#     reg.print_best_fitting_line()
#     print(f"Predicted value at 2060 = {reg.predict(2060)}")
#     print(f"The errorSquared = {reg.error_square()}")
#     print(f"Error in 2050 = {reg.error_in(2050)}")
#




#









import numpy as np
import pandas as pd

class MultivariateRegression:
    def __init__(self):
        self.X = None
        self.y = None
        self.coefficients = None

    def take_input(self, file_path):
        data = pd.read_csv(file_path, header=None)
        self.X = data.iloc[:, :-1].values
        self.y = data.iloc[:, -1].values

    def calculate_coefficients(self):
        # Add a column of ones to X for the intercept term
        X_b = np.c_[np.ones((self.X.shape[0], 1)), self.X]
        self.coefficients = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(self.y)

    def print_best_fitting_line(self):
        if self.coefficients is None:
            self.calculate_coefficients()
        print(f"The best fitting line is y = {self.coefficients[0]:.4f}", end=" ")
        for i in range(1, len(self.coefficients)):
            print(f"+ {self.coefficients[i]:.4f} * x{i}", end=" ")
        print()

    def predict(self, x):
        if self.coefficients is None:
            self.calculate_coefficients()
        x_b = np.c_[1, x]
        return x_b.dot(self.coefficients)

    def error_square(self):
        if self.coefficients is None:
            self.calculate_coefficients()
        predictions = self.predict(self.X)
        return np.sum((predictions - self.y) ** 2)

    def error_in(self, x):
        if self.coefficients is None:
            self.calculate_coefficients()
        prediction = self.predict(np.array(x).reshape(1, -1))
        for i in range(len(self.X)):
            if np.array_equal(self.X[i], x):
                return self.y[i] - prediction
        return 0

# Driver code
if __name__ == "__main__":
    reg = MultivariateRegression()

    # Path to the input CSV file
    file_path = "input1.csv"

    # Calling function take_input to read data from the file
    reg.take_input(file_path)

    # Printing the best fitting line
    reg.print_best_fitting_line()

    # Example prediction (replace with actual values as needed)
    example_x = [1, 2, 3]  # Replace with actual feature values
    print(f"Predicted value at {example_x} = {reg.predict(np.array(example_x).reshape(1, -1))[0]}")

    print(f"The errorSquared = {reg.error_square()}")

    # Example error calculation (replace with actual values as needed)
    example_error_x = [1.0, 3.0, 0.0]  # Replace with actual feature values
    print(f"Error in {example_error_x} = {reg.error_in(example_error_x)}")

