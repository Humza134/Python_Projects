import time
import os
import random
import json

# File to store accounts
ACCOUNTS_FILE = 'accounts_details.json'

# Load existing accounts from file if it exists
if os.path.exists(ACCOUNTS_FILE):
    with open(ACCOUNTS_FILE, 'r') as file:
        bank_all_accounts = json.load(file)
else:
    bank_all_accounts = []

def create_account():
    # create a sample account
    account_name = input("Enter account name: ")
    account_balance = float(input("Enter initial balance: "))
    contact_number = input("Enter contact number: ")
    email = input("Enter email: ")
    return {
        "account_name": account_name,
        "account_number": generate_account_number(),
        "password": generate_password(),
        "balance": account_balance,
        "contact_number": contact_number,
        "email": email,
        "transactions": []
    }

def record_transaction(account_number, transaction_type, amount, balance_after, file_path="statement.txt"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    transaction = f"{timestamp} | Account {account_number} | {transaction_type} | Amount: {amount} | Balance after: {balance_after}\n"
    with open(file_path, "a") as file:
        file.write(transaction)

def deposit(account, amount, file_path="statement.txt"):
    if amount <=0:
        print("Deposit amount must be positive")
        return account
    
    account['balance'] += amount
    
    transaction = {
                "type": "deposit",
                "amount": amount,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
    account["transactions"].append(transaction)

    # Save updated accounts to file
    with open(ACCOUNTS_FILE, 'w') as file:
        json.dump(bank_all_accounts, file)

    record_transaction(account['account_number'], "Deposit", amount, account['balance'], file_path)
    print(f"Deposited {amount} into account {account['account_number']}. New balance: {account['balance']}")
    return account

def withdraw(account, amount, file_path="statement.txt"):
    if amount <= 0:
        print("Withdrawal amount must be positive")
        return account

    if amount > account['balance']:
        print("Insufficient funds")
        return account
    
    account['balance'] -= amount
    transaction = {
                    "type": "withdraw",
                    "amount": amount,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
    account["transactions"].append(transaction)

    # Save updated accounts to file
    with open(ACCOUNTS_FILE, 'w') as file:
        json.dump(bank_all_accounts, file)

    record_transaction(account['account_number'], "Withdrawal", amount, account['balance'], file_path)
    print(f"Withdrew {amount} from account {account['account_number']}. New balance: {account['balance']}")
    return account

#function to load and print the transaction history
def print_bank_statement(file_path="statement.txt"):
    if not os.path.exists(file_path):
        print("No transactions found.")
        return
    with open(file_path, "r") as file:
        transactions = file.readlines()

    if not transactions:
        print("No transactions found.")
        return
    
    print("\nBank Statement")
    for transaction in transactions:
        print(transaction.strip())
    
#function to generate account number
def generate_account_number():
    #Generate a random 5-digit account number (between 10000 and 99999)
    account_number = random.randint(10000, 99999)
    #Check if the generated account number already exists
    while any(account['account_number'] == account_number for account in bank_all_accounts):
        account_number = random.randint(10000, 99999)

    return account_number

#function to generate password
def generate_password():
    #Generate a random 4-digit password (between 1000 and 9999)
    password = random.randint(1000, 9999)
    #check if the generated password already exists
    while any(account['password'] == password for account in bank_all_accounts):
        password = random.randint(1000, 9999)

    return password

#function balance inquiry
def balance_inquiry():
    account_number = int(input("Enter account number: "))
    for acc in bank_all_accounts:
        if acc['account_number'] == account_number:
            pwd = int(input("Enter password: "))
            if acc['password'] == pwd:
                return f"Your account balance is: {acc['balance']}"
            else:
                return "Invalid password"

def account_transaction_statement():
    # Find the account
    account_number = int(input("Enter account number: "))
    for account in bank_all_accounts:
        if account["account_number"] == account_number:
            pwd = int(input("Enter password: "))
            if account['password'] == pwd:
                print(f" Transaction Statement for {account['account_name']} Account:")
                balance = account["balance"]

                # Process transactions in reverse to calculate previous balances
                transactions = list(reversed(account["transactions"]))
                for transaction in transactions:
                    current_balance = balance

                    # Reverse the transaction to get the previous balance
                    if transaction["type"] == "deposit":
                        previous_balance = current_balance - transaction["amount"]
                    elif transaction["type"] == "withdraw":
                        previous_balance = current_balance + transaction["amount"]
                    else:
                        previous_balance = current_balance  # Safety fallback

                    # Print the details
                    print(f"Previous Balance: {previous_balance}, "
                        f"{transaction['type'].capitalize()}: {transaction['amount']} Time: {transaction['timestamp']}, "
                        f"New Balance: {current_balance}")

                    # Update the running balance for the next iteration
                    balance = previous_balance
                return  # Exit the function after printing the statement

    raise ValueError("Account not found.")

def bank_accounts_details():
    ADMIN_PASS = 980
    pwd = int(input("Enter password"))
    if pwd == ADMIN_PASS:
        print(bank_all_accounts)


def main():
    print("Welcome to the Bank")
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Print Bank Statement")
        print("5. Balance Inquiry")
        print("6. Account Transaction History")
        print("7. Bank accounts details")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            account = create_account()
            bank_all_accounts.append(account)
            # Save accounts to file
            with open(ACCOUNTS_FILE, 'w') as file:
                json.dump(bank_all_accounts, file)
            print(f"""
                    Your Account opened successfully.
                    Your account name is: {account['account_name']}
                    Your account number is: {account['account_number']}
                    Your account balance is: {account['balance']}
                    Your account password is: {account['password']}
                    """)
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            for account in bank_all_accounts:
                if account['account_number'] == account_number:
                    account = deposit(account, amount)
                    break
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            for account in bank_all_accounts:
                if account['account_number'] == account_number:
                    account = withdraw(account, amount)
                    break
            else:
                print("Account not found.")
        elif choice == "4":
            print_bank_statement()
        elif choice == "5":
            print(balance_inquiry())
        elif choice == "6":
            account_transaction_statement()
        elif choice == "7":
            accounts = bank_accounts_details()
            print(accounts)
        elif choice == "8":
            print("Thank you for using the bank.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

