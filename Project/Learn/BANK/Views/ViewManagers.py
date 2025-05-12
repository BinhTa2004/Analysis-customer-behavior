from Controller.AccountsManagement import AccountsManagement
from Controller.CustomersManagement import CustomersManagement
from Controller.EmployeesManagement import EmployeesManagement
from Controller.BankFeesManagement import BankFeesManagement
from Controller.BranchesManagement import BranchesManagement
from Controller.LoansManagement import LoanManagement
from Controller.TransactionsManagement import TransactionsManagement
from Controller.CreateTransaction import CreateTransaction

def AccountsMenu():
    while True:
        print("\nAccounts Menu")
        print("1.Add account")
        print("2.Update account")
        print("3.Delete account")
        print("4.Search account")
        print("5.Show Trasaction")
        print("6.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            AccountsManagement().add_account()
        elif option == 2:
            AccountsManagement().update_account()
        elif option == 3:
            AccountsManagement().delete_account()
        elif option == 4:
            AccountsManagement().search_account()
        elif option == 5:
            AccountsManagement().show_transaction()
        elif option == 6:
            return
        else:
            print("Invalid option")

def CustomersMenu():
    while True:
        print("\nCustomers Menu")
        print("1.Add customer")
        print("2.Update customer")
        print("3.Delete customer")
        print("4.Search customer")
        print("5.Show account customer")
        print("6.Show loan customer")
        print("7.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            CustomersManagement().add_customer()
        elif option == 2:
            CustomersManagement().update_customer()
        elif option == 3:
            CustomersManagement().delete_customer()
        elif option == 4:
            CustomersManagement().search_customer()
        elif option == 5:
            CustomersManagement().show_accounts_customer()
        elif option == 6:
            CustomersManagement().show_loans_customer()
        elif option == 7:
            return
        else:
            print("Invalid option")

def EmployeesMenu():
    while True:
        print("\nEmployees Menu")
        print("1.Add employee")
        print("2.Update employee")
        print("3.Delete employee")
        print("4.Search employee")
        print("5.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            EmployeesManagement().add_employee()
        elif option == 2:
            EmployeesManagement().update_employee()
        elif option == 3:
            EmployeesManagement().delete_employee()
        elif option == 4:
            EmployeesManagement().search_employee()
        elif option == 5:
            return
        else:
            print("Invalid option")

def BankFeesMenu():
    while True:
        print("\nBank Fees Menu")
        print("1.Add bank")
        print("2.Update bank")
        print("3.Delete bank")
        print("4.Search bank")
        print("5.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            BankFeesManagement().add_BankFees()
        elif option == 2:
            BankFeesManagement().update_BankFees()
        elif option == 3:
            BankFeesManagement().delete_BankFees()
        elif option == 4:
            BankFeesManagement().search_BankFees()
        elif option == 5:
            return
        else:
            print("Invalid option")

def BranchesMenu():
    while True:
        print("\nBranches Menu")
        print("1.Add branche")
        print("2.Update branche")
        print("3.Delete branche")
        print("4.Search branche")
        print("5.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            BranchesManagement().add_branches()
        elif option == 2:
            BranchesManagement().update_branches()
        elif option == 3:
            BranchesManagement().delete_branches()
        elif option == 4:
            BranchesManagement().search_branches()
        elif option == 5:
            return
        else:
            print("Invalid option")

def LoansMenu():
    while True:
        print("\nLoans Menu")
        print("1.Add loan")
        print("2.Update loan")
        print("3.Delete loan")
        print("4.Search loan")
        print("5.Check loan")
        print("6.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            LoanManagement().add_loan()
        elif option == 2:
            LoanManagement().update_loan()
        elif option == 3:
            LoanManagement().delete_loan()
        elif option == 4:
            LoanManagement().search_loan()
        elif option == 5:
            LoanManagement().check_loan()
        elif option == 6:
            return
        else:
            print("Invalid option")

def TransactionsMenu():
    while True:
        print("\nTransactions Menu")
        print("1.Add transaction")
        print("2.Update transaction")
        print("3.Delete transaction")
        print("4.Search transaction")
        print("5.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            TransactionsManagement().add_transaction()
        elif option == 2:
            TransactionsManagement().update_transaction()
        elif option == 3:
            TransactionsManagement().delete_transaction()
        elif option == 4:
            TransactionsManagement().search_transaction()
        elif option == 5:
            return
        else:
            print("Invalid option")

def CreateTransactions():
    while True:
        print("\nTransactions Menu")
        print("1.Recharge transaction")
        print("2.Withdraw transaction")
        print("3.Deposit transaction")
        print("4.Pay transaction")
        print("5.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                option = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if option == 1:
            CreateTransaction().recharge()
        elif option == 2:
            CreateTransaction().withdraw()
        elif option == 3:
            CreateTransaction().transfer()
        elif option == 4:
            CreateTransaction().pay()
        elif option == 5:
            return
        else:
            print("Invalid option")
