import pyodbc
from sqlalchemy import create_engine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Thông tin kết nối đến MS SQL Server
server = r'ADMIN-PC\SQLEXPRESS'
database = 'EmailSpam'

# Tạo chuỗi kết nối với MS SQL Server
connection_string = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Tạo engine kết nối với MS SQL Server
engine = create_engine(connection_string)

# Đọc dữ liệu từ file CSV
data = pd.read_csv(r'C:\Users\Admin\Desktop\email_classification.csv')
#print(data.head())  # Hiển thị một vài dòng đầu tiên của dữ liệu

# Tiền xử lý dữ liệu
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['email'])  # Giả sử cột văn bản là 'email'
y = data['label']  # Giả sử cột nhãn là 'label' với giá trị 'spam' và 'ham'

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng Mô hình Phân loại
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá Mô hình
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='spam')
recall = recall_score(y_test, y_pred, pos_label='spam')
f1 = f1_score(y_test, y_pred, pos_label='spam')

print(f'Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1-Score: {f1:.2f}')

# Lưu Kết quả vào Bảng SQL
model_performance_data = {
    'model_id': [1],  # Định danh của mô hình
    'model_name': ['Random Forest'],
    'accuracy': [accuracy],
    'precision': [precision],
    'recall': [recall],
    'f1_score': [f1],
    'roc_auc': [None],
    'training_time': [None],
    'testing_time': [None],
    'timestamp': [pd.Timestamp.now()]
}
model_performance_df = pd.DataFrame(model_performance_data)

# Lưu kết quả vào bảng Model_Performance trên MS SQL Server
model_performance_df.to_sql('ModelPerformance', con=engine, if_exists='append', index=False)

# Lưu Dữ liệu Vào Bảng Email_Data
email_data = data[['email', 'label']].copy()
email_data['model_id'] = 1  # Đặt model_id cho tất cả các bản ghi

# Lưu dữ liệu vào bảng Email_Data trên MS SQL Server
email_data.to_sql('Email_Data', con=engine, if_exists='append', index=False)



from sklearn.metrics import confusion_matrix
import pandas as pd

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Tính toán ma trận nhầm lẫn
conf_matrix = confusion_matrix(y_test, y_pred, labels=['spam', 'ham'])

# Tạo DataFrame từ ma trận nhầm lẫn
conf_matrix_df = pd.DataFrame(conf_matrix, index=['Thực tế: Spam', 'Thực tế: Ham'], columns=['Dự đoán: Spam', 'Dự đoán: Ham'])

# In ra ma trận nhầm lẫn
print("Ma trận nhầm lẫn:")
print(conf_matrix_df)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Tính toán ma trận nhầm lẫn
conf_matrix = confusion_matrix(y_test, y_pred, labels=['spam', 'ham'])

# Tạo DataFrame từ ma trận nhầm lẫn
conf_matrix_df = pd.DataFrame(conf_matrix, index=['Thực tế: Spam', 'Thực tế: Ham'], columns=['Dự đoán: Spam', 'Dự đoán: Ham'])

# In ra ma trận nhầm lẫn
print("Ma trận nhầm lẫn:")
print(conf_matrix_df)

# In ra tổng số email mà mô hình đã dự đoán
total_predicted_emails = len(y_pred)
print(f'Tổng số email mà mô hình dự đoán: {total_predicted_emails}')
