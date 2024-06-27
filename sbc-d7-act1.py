# Initialize an empty dictionary to store accounts
bank_accounts = {}

def create_bank_account(customer_name):
    if customer_name not in bank_accounts:
        bank_accounts[customer_name] = 0
        print(f"Bank account for {customer_name} created successfully.")
    else:
        print(f"Bank account for {customer_name} already exists.")

def check_account_balance(customer_name):
    if customer_name in bank_accounts:
        balance = bank_accounts[customer_name]
        print(f"{customer_name}'s account balance: ₱{balance}")
    else:
        print(f"Bank account for {customer_name} does not exist.")

def deposit_to_account(customer_name, amount):
    if customer_name in bank_accounts:
        bank_accounts[customer_name] += amount
        print(f"Deposited ₱{amount} into {customer_name}'s account.")
    else:
        print(f"Bank account for {customer_name} does not exist.")

def withdraw_from_account(customer_name, amount):
    if customer_name in bank_accounts:
        if bank_accounts[customer_name] >= amount:
            bank_accounts[customer_name] -= amount
            print(f"Withdrew ₱{amount} from {customer_name}'s account.")
        else:
            print(f"Insufficient funds for {customer_name}.")
    else:
        print(f"Bank account for {customer_name} does not exist.")

def delete_bank_account(customer_name):
    if customer_name in bank_accounts:
        del bank_accounts[customer_name]
        print(f"Bank account for {customer_name} deleted successfully.")
    else:
        print(f"Bank account for {customer_name} does not exist.")

# Example usage:
while True:
    print("\nOptions:")
    print("1. Create Bank Account")
    print("2. Check Account Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Bank Account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        create_bank_account(name)
    elif choice == 2:
        name = input("Enter customer name: ")
        check_account_balance(name)
    elif choice == 3:
        name = input("Enter customer name: ")
        amount = float(input("Enter deposit amount: "))
        deposit_to_account(name, amount)
    elif choice == 4:
        name = input("Enter customer name: ")
        amount = float(input("Enter withdrawal amount: "))
        withdraw_from_account(name, amount)
    elif choice == 5:
        name = input("Enter customer name: ")
        delete_bank_account(name)
    elif choice == 6:
        print("Exiting the bank system. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
