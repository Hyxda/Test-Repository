class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount): 
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, minimum_balance=0):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Transaction rejected. Minimum balance must be maintained.")
        else:
            super().withdraw(amount)

class ChequingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Transaction rejected. You have insufficient funds and exceeded your overdraft limit.")
        else:
            super().withdraw(amount)

class Bank:
    def __init__(self):
        self.accounts = []
        self.create_accounts()

    def create_accounts(self):
        self.accounts.append(SavingsAccount("SA1001", 10000, 5000))
        self.accounts.append(SavingsAccount("SA1002", 5000, 2000))
        self.accounts.append(ChequingAccount("CA1001", 10000, 5000))
        self.accounts.append(ChequingAccount("CA1002", 5000, 2000))
        self.accounts.append(Account("A1001", 1000))

    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None

    def open_account(self, account_type, account_number, balance=0, minimum_balance=0, overdraft_limit=0):
        if account_type == "savings":
            self.accounts.append(SavingsAccount(account_number, balance, minimum_balance))
        elif account_type == "chequing":
            self.accounts.append(ChequingAccount(account_number, balance, overdraft_limit))
        else:
            self.accounts.append(Account(account_number, balance))
        print("Account opened successfully. \n=========================")



class Program:
    def __init__(self):
        self.accounts = []

    def show_main_menu(self):
        while True:
            print("Welcome to the Bank!"
            "\n1. Open Account"
            "\n2. Select Account"
            "\n3. Exit")
            choice = input("Enter your choice: \n> ")
            if choice == "1":
                account_number = input("Enter account number: \n> ")
                self.accounts.append(Account(account_number))
                print("Account opened successfully! \n=========================\n")
            elif choice == "2":
                account_number = input("Enter account number: \n> ")
                for account in self.accounts:
                    if account.account_number == account_number:
                        self.show_account_menu(account)
                        break
                else:
                    print("Account not found. \n=========================\n")
            elif choice == "3":
                print("Thank you for using our Bank!")
                break
            else:
                print("Invalid choice.")

    def show_account_menu(self, account):
        while True:
            print(f"Account {account.account_number}\n")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: \n> ")
            if choice == "1":
                print(f"\n========================= \nBalance: {account.check_balance()}")
            elif choice == "2":
                amount = float(input("Enter amount to deposit: \n> "))
                account.deposit(amount)
                print("Deposit successful!\n")
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: \n> "))
                if account.withdraw(amount):
                    print("Withdrawal successful!\n")
                else:
                    print("Insufficient balance.\n")
            elif choice == "4":
                print("Exiting account...")
                break
            else:
                print("Invalid choice.")

    def run(self):
        self.show_main_menu()

program = Program()
program.run()
