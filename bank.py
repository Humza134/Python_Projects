import json
import os

# File to store accounts
ACCOUNTS_FILE = 'accounts.json'

# Load existing accounts from file if it exists
if os.path.exists(ACCOUNTS_FILE):
    with open(ACCOUNTS_FILE, 'r') as file:
        bank_all_accounts = json.load(file)
else:
    bank_all_accounts = []

def create_account(name: str, balance):
    account = {
        "name": name,
        "balance": balance,
        "transactions": []
    }
    bank_all_accounts.append(account)
    # Save accounts to file
    with open(ACCOUNTS_FILE, 'w') as file:
        json.dump(bank_all_accounts, file)
    return account

# create_account("Ali", 4000)

# print(bank_all_accounts)

# create deposit function and add transaction record

# Update the deposit function
def deposit(account_name: str, amount: float):
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    # Find the account
    for account in bank_all_accounts:
        if account["name"] == account_name:
            account["balance"] += amount
            transaction = {
                "type": "deposit",
                "amount": amount
            }
            account["transactions"].append(transaction)

            # Save updated accounts to file
            with open(ACCOUNTS_FILE, 'w') as file:
                json.dump(bank_all_accounts, file)
            return account  # Return updated account

    raise ValueError("Account not found.")

# deposit("Ali", 1500)
# print(bank_all_accounts)

# Update the withdraw function
def withdraw(account_name: str, amount: float):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")

    # Find the account
    for account in bank_all_accounts:
        if account["name"] == account_name:
            if account["balance"] >= amount:
                account["balance"] -= amount
                transaction = {
                    "type": "withdraw",
                    "amount": amount
                }
                account["transactions"].append(transaction)

                # Save updated accounts to file
                with open(ACCOUNTS_FILE, 'w') as file:
                    json.dump(bank_all_accounts, file)
                return account  # Return updated account
            else:
                raise ValueError("Insufficient funds.")

    raise ValueError("Account not found.")

# withdraw("Ali", 500)
# print(bank_all_accounts)

# Fix the get_balance function to fetch the updated data
def get_balance(account_name: str):
    # Reload accounts from the file
    with open(ACCOUNTS_FILE, 'r') as file:
        bank_all_accounts = json.load(file)

    # Find the account
    for account in bank_all_accounts:
        if account["name"] == account_name:
            print(f"Account balance for {account_name} is {account['balance']}")
            return account["balance"]  # Return balance directly

    raise ValueError("Account not found.")

# get_balance("Ahmed")

# create get_transaction_history function

def get_transaction_history(account_name: str):
    # Find the account
    for account in bank_all_accounts:
        if account["name"] == account_name:
            # return account["transactions"]
            print(f"Transaction history for {account_name}:")
            for transaction in account["transactions"]:
                print(f"{transaction['type'].capitalize()}: {transaction['amount']}")
            return  # Exit the function after printing the transaction history

    raise ValueError("Account not found.")

# get_transaction_history("Ahmed")

# get_transaction_history("Hamza")

# The print_statement function will display all transactions made on the account (deposits and withdrawals) and the balance after each transaction.
# def print_statement(account_name: str):
    # Find the account
    # for account in bank_all_accounts:
    #     if account["name"] == account_name:
    #         print(f"Statement for {account_name}:")
    #         balance = account["balance"]
    #         for transaction in account["transactions"]:
    #             if transaction["type"] == "deposit":
    #                 balance += transaction["amount"]
    #             elif transaction["type"] == "withdraw":
    #                 balance -= transaction["amount"]
    #             print(f"{transaction['type'].capitalize()}: {transaction['amount']}, Balance: {balance}")
    #         return  # Exit the function after printing the statement

    # raise ValueError("Account not found.")

def print_statement(account_name: str):
    # Find the account
    for account in bank_all_accounts:
        if account["name"] == account_name:
            print(f"Statement for {account_name}:")
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
                      f"{transaction['type'].capitalize()}: {transaction['amount']}, "
                      f"New Balance: {current_balance}")

                # Update the running balance for the next iteration
                balance = previous_balance
            return  # Exit the function after printing the statement

    raise ValueError("Account not found.")

# Example usage
print_statement("Ali")