from Views.ViewManagers import *
def main():
    while True:
        print("\nBANK")
        print("1.Accounts Management")
        print("2.Customers Management")
        print("3.Employees Management")
        print("4.Loans Management")
        print("5.Transactions Management")
        print("6.Branches Management")
        print("7.Bank Fees Management")
        print("8.Exit")
        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit():
                choice = int(user_input)
                break
            else:
                print("Invalid input. Please enter a valid integer.")
        if choice == 1:
            AccountsMenu()
        elif choice == 2:
            CustomersMenu()
        elif choice == 3:
            EmployeesMenu()
        elif choice == 4:
            LoansMenu()
        elif choice == 5:
            TransactionsMenu()
        elif choice == 6:
            BranchesMenu()
        elif choice == 7:
            BankFeesMenu()
        elif choice == 8:
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()