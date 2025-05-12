# import pyodbc
# import pandas as pd
#
# # Thông tin kết nối
# server = 'ADMIN-PC\SQLEXPRESS'
# database = 'BANK'
#
# # Chuỗi kết nối
# connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
#
# # Tạo kết nối
# connection = pyodbc.connect(connection_string)
# cursor = connection.cursor()
#
# # Thực hiện câu lệnh SQL
# cursor.execute("SELECT * FROM Customers")
#
# # Lấy dữ liệu
# rows = cursor.fetchall()
#
# # Lấy tên cột từ cursor
# columns = [column[0] for column in cursor.description]
#
# # Tạo DataFrame từ dữ liệu và tên cột
# df = pd.DataFrame.from_records(rows, columns=columns)
#
# # Thiết lập tùy chọn để không cắt ngắn dữ liệu
# pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
# pd.set_option('display.max_rows', None)     # Hiển thị tất cả các hàng
# pd.set_option('display.max_colwidth', None) # Hiển thị toàn bộ nội dung của mỗi cột
#
# # In DataFrame ra màn hình
# print(df)
#
# # Đóng kết nối
# connection.close()
#





import pyodbc
import pandas as pd
from tabulate import tabulate

# Thông tin kết nối
server = r'ADMIN-PC\SQLEXPRESS'
database = 'BANK'

# Chuỗi kết nối
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Tạo kết nối
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Thực hiện câu lệnh SQL
cursor.execute("SELECT * FROM Loans")

# Lấy dữ liệu
rows = cursor.fetchall()

# Lấy tên cột từ cursor
columns = [column[0] for column in cursor.description]

# Tạo DataFrame từ dữ liệu và tên cột
df = pd.DataFrame.from_records(rows, columns=columns)

# Sử dụng tabulate để in DataFrame với định dạng đẹp
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# Đóng kết nối
connection.close()
