#proportion
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.stats as stats
#
# # Sample proportion, hypothesized proportion, and other parameters
# p_hat = 11/43
# p_0 = 0.5
# n = 43
# z_alpha_over_2 = 1.96  # Critical value for a 95% confidence interval
#
# # Calculate the margin of error for the confidence interval
# E = z_alpha_over_2 * np.sqrt((p_hat * (1 - p_hat)) / n)
#
# # Define the confidence interval
# ci_lower = p_hat - E
# ci_upper = p_hat + E
#
# # Calculate the test statistic (z-value) for the sample proportion
# z_hat = (p_hat - p_0) / np.sqrt((p_0 * (1 - p_0)) / n)
#
# # Create standard normal distribution curve
# x = np.linspace(-3, 3, 1000)
# y = stats.norm.pdf(x, 0, 1)
#
# # Plot the normal distribution
# plt.plot(x, y, label="Standard Normal Distribution", color='blue')
#
# # Shade the confidence interval area (-z_alpha/2 to +z_alpha/2)
# plt.fill_between(x, y, where=(x >= -z_alpha_over_2) & (x <= z_alpha_over_2), color='lightblue', alpha=0.5)
#
# # Mark the critical values
# plt.axvline(-z_alpha_over_2, color='red', linestyle='--', label=f'Critical value = {-z_alpha_over_2}')
# plt.axvline(z_alpha_over_2, color='red', linestyle='--', label=f'Critical value = {z_alpha_over_2}')
#
# # Mark the test statistic (z-value) for the sample proportion
# plt.axvline(z_hat, color='green', linestyle='-', label=f'Test statistic z = {z_hat:.2f}')
#
# # Add labels and title
# plt.title('Confidence Interval and Hypothesis Testing')
# plt.xlabel('z-values')
# plt.ylabel('Probability Density')
# plt.legend()
#
# # Show the plot
# plt.show()



#mean
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample mean, hypothesized mean, and other parameters
x_bar = 5.01556  # Sample mean
mu_0 = 5.0   # Hypothesized mean
n = 500     # Sample size
sigma = 2.991514835 # Standard deviation of the sample
z_alpha_over_2 = 1.96  # Critical value for a 95% confidence interval

# Calculate the margin of error for the confidence interval
E = z_alpha_over_2 * (sigma / np.sqrt(n))

# Define the confidence interval
ci_lower = x_bar - E
ci_upper = x_bar + E

# Calculate the test statistic (z-value) for the sample mean
z_hat = (x_bar - mu_0) / (sigma / np.sqrt(n))

# Create standard normal distribution curve
x = np.linspace(-3, 3, 1000)
y = stats.norm.pdf(x, 0, 1)

# Plot the normal distribution
plt.plot(x, y, label="Standard Normal Distribution", color='blue')

# Shade the confidence interval area (-z_alpha/2 to +z_alpha_over_2)
plt.fill_between(x, y, where=(x >= -z_alpha_over_2) & (x <= z_alpha_over_2), color='lightblue', alpha=0.5)

# Mark the critical values
plt.axvline(-z_alpha_over_2, color='red', linestyle='--', label=f'Critical value = {-z_alpha_over_2}')
plt.axvline(z_alpha_over_2, color='red', linestyle='--', label=f'Critical value = {z_alpha_over_2}')

# Mark the test statistic (z-value) for the sample mean
plt.axvline(z_hat, color='green', linestyle='-', label=f'Test statistic z = {z_hat:.2f}')

# Add labels and title
plt.title('Confidence Interval and Hypothesis Testing for Sample Mean')
plt.xlabel('z-values')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.show()







# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
#
# # Đọc dữ liệu từ file Excel
# file_path = r'C:/Users/Admin/Desktop/mental_health_and_technology_usage_2024.xlsx'  # Thay 'path_to_your_file.xlsx' bằng đường dẫn tới file của bạn
# data = pd.read_excel(file_path)
#
# # Giả sử file có hai cột 'x' và 'y'
# x = data['Social_Media_Usage_Hours'].values
# y = data['Physical_Activity_Hours'].values
#
# # Thực hiện hồi quy tuyến tính
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
#
# # In phương trình đường hồi quy
# print(f"Regression line: y = {slope:.2f}x + {intercept:.2f}")
#
# # Tính giá trị y dự đoán dựa trên đường hồi quy để vẽ
# y_pred = slope * x + intercept
#
# # Vẽ biểu đồ scatter plot và đường hồi quy
# plt.scatter(x, y, color='blue', label='Data Points')
# plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')
#
# # Thêm nhãn và tiêu đề
# plt.xlabel('Social_Media_Usage_Hours')
# plt.ylabel('Physical_Activity_Hours')
# plt.title('Physical_Activity_Hours Line Fit Plot')
# plt.legend()
# plt.show()
