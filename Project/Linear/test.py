#
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import numpy as np
#
# # Đọc dữ liệu từ file CSV
# file_path = "C:/Users/Admin/Desktop/input1.csv"
# df = pd.read_csv(file_path)
#
# # Chọn các biến độc lập và biến mục tiêu
# X = df[['Feature1', 'Feature2', 'Feature3']]
# y = df['Target y']
#
# # Tạo mô hình hồi quy
# model = LinearRegression()
# model.fit(X, y)
#
# # Lấy các hệ số hồi quy
# theta_0 = model.intercept_
# theta_1, theta_2, theta_3 = model.coef_
#
# # Tạo ma trận theta
# Theta = np.array([theta_0, theta_1, theta_2, theta_3]).reshape(-1, 1)
#
# print("Ma trận hệ số Theta:")
# print(Theta)




# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# import numpy as np
#
# # Đọc dữ liệu từ file CSV
# file_path = "C:/Users/Admin/Desktop/input1.csv"
# df = pd.read_csv(file_path)
#
# # In ra các cột của DataFrame để kiểm tra
# print("Columns in the DataFrame:", df.columns)
#
# # Chọn các biến độc lập và biến mục tiêu
# # Kiểm tra xem các cột có tồn tại trong DataFrame không
# required_columns = ['Feature2', 'Target y']
# missing_columns = [col for col in required_columns if col not in df.columns]
#
# if missing_columns:
#     raise ValueError(f"Missing columns in the CSV file: {missing_columns}")
#
# # Tạo biến mới là bình phương của Feature2
# df['Feature2_squared'] = df['Feature2'] ** 2
#
# # Chọn các biến độc lập và biến mục tiêu
# X = df[['Feature2', 'Feature2_squared']]
# y = df['Target y']
#
# # Tạo mô hình hồi quy
# model = LinearRegression()
# model.fit(X, y)
#
# # Dự đoán giá trị mục tiêu
# y_pred = model.predict(X)
#
# # Tính RMSE
# rmse = np.sqrt(mean_squared_error(y, y_pred))
#
# print("RMSE of the quadratic regression model:", rmse)







import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Đọc dữ liệu từ file CSV
file_path = "C:/Users/Admin/Desktop/input1.csv"
df = pd.read_csv(file_path)

# In ra các cột của DataFrame để kiểm tra
print("Columns in the DataFrame:", df.columns)

# Chọn các biến độc lập và biến mục tiêu
# Kiểm tra xem các cột có tồn tại trong DataFrame không
required_columns = ['Feature2', 'Target y']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns in the CSV file: {missing_columns}")

# Tạo biến mới là bình phương của Feature2
df['Feature2_squared'] = df['Feature2'] ** 2

# Chọn các biến độc lập và biến mục tiêu
X = df[['Feature2', 'Feature2_squared']]
y = df['Target y']

# Tạo mô hình hồi quy
model = LinearRegression()
model.fit(X, y)

# Lấy các hệ số hồi quy
theta_0 = model.intercept_
theta_1, theta_2 = model.coef_

# Tạo ma trận theta
Theta = np.array([theta_0, theta_1, theta_2]).reshape(-1, 1)

# Dự đoán giá trị mục tiêu
y_pred = model.predict(X)

# Tính RMSE
rmse = np.sqrt(mean_squared_error(y, y_pred))

# In ra ma trận hệ số Theta
print("Ma trận hệ số Theta:")
print(Theta)

# In ra RMSE
print("RMSE of the quadratic regression model:", rmse)
