from Models.Accounts import Account
from Library.AVLTree import AVlTree
from Database.db_connection import get_db_connection
import pyodbc
import pandas as pd
from tabulate import tabulate
class AccountsManagement:
    def __init__(self):
        self.accounttree = self.load_customers_from_db()
    def add_account(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        while True:
            account_number = input("Enter account number: ")
            if len(account_number) > 10:
                print("Account number must be less than 10 characters")
            else:
                break

        while True:
            cursor.execute("SELECT * FROM AccountTypes")
            rows = cursor.fetchall()

            columns = [column[0] for column in cursor.description]

            # Tạo DataFrame từ dữ liệu và tên cột
            df = pd.DataFrame.from_records(rows, columns=columns)

            # Sử dụng tabulate để in DataFrame với định dạng đẹp
            print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

            account_type_id = int(input("Enter account type: "))
            if account_type_id < 1 or account_type_id > 10:
                print("Account type must be between 1 and 10")
            else:
                break

        while True:
            customer_id = int(input("Enter customer id: "))


        # Chèn khách hàng mới vào cơ sở dữ liệu
        cursor.execute('''
            INSERT INTO Accounts (AccountNumber, AccountTypeID, CustomerID, Balance, CreationDate, BranchID, FeeID)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (account_number, account_type_id, customer_id, balance, creation_date, branch_id, fee_id))

        # Lấy ID tự tăng vừa tạo
        cursor.execute('SELECT SCOPE_IDENTITY()')
        new_customer_id = cursor.fetchone()[0]

        conn.commit()
        conn.close()
        self.accounttree.insert(new_customer_id, accountnumber, accounttypeid, customerid, balance, creationdate, branchid, feeid)

    def update_account(self):
        pass
    def delete_account(self):
        pass
    def search_account(self):
        pass
    def show_transaction(self):
        conn = get_db_connection()  # Sử dụng hàm từ file db_connection.py
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Accounts")
        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        # Tạo DataFrame từ dữ liệu và tên cột
        df = pd.DataFrame.from_records(rows, columns=columns)

        # Sử dụng tabulate để in DataFrame với định dạng đẹp
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

    def load_customers_from_db(self):
        avltree = AVlTree()
        conn = get_db_connection()  # Sử dụng hàm từ file db_connection.py
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Accounts")
        rows = cursor.fetchall()
        for row in rows:
            avltree.insert(avltree.root,Account(
                row.AccountID,
                row.AccountNumber,
                row.AccountTypeID,
                row.CustomerID,
                row.Balance,
                row.CreationDate,
                row.BranchID,
                row.FeeID)
                           )
        conn.close()
        return avltree