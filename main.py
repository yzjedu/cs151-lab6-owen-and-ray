# Programmers:  [Owen and Rayan]
# Course:  CS151, [Professor Z]
# Due Date: [10/24/2024]
# Programming Assignment:  [Lab 6]
# Problem Statement:  [Calculating functions of an ATM]
# Data In: [menu choice (d,w,v,e)]
# Data Out:  [What their current balance is, if they input an invalid input]
# Credits: [Lecture note 18]
# Display the purpose of the program: Function as an ATM

# Constants
starting_balance = 1000
penalty_rate = 0.05

# Main function with all other functions
def atm():
    balance = starting_balance
    while True:
        choice = get_choice()
        if choice == 'V':
            view_balance(balance)
        elif choice == 'D':
            balance = deposit(balance)
        elif choice == 'W':
            balance = withdraw(balance)
        elif choice == 'E':
            print("Thank you, have a nice day!")
            break

# View balance Function
def view_balance(balance):
    print(f"Your balance is {balance}")

# Deposit Function
def deposit(balance):
    while True:
        cash = input("How much money would you like to deposit? ")
        if not cash.isdigit():
            print ("Invalid cash") # Error Check for invalid input
            continue
        cash = int(cash)
        if cash < 0: # Check for negative numbers
            print ("Invalid cash")
        else:
            balance += cash
            print ("Your new balance is " + str(balance))
            break
    return balance

def withdraw(balance):
    while True:
        cash = input("How much money would you like to withdraw? ")
        if not cash.isdigit():
            print("Invalid cash amount. Please enter a positive number.") # Number Check
            continue  # Prompt again
        cash = int(cash)
        if cash < 0:
            print("You cannot withdraw negative cash.")
        elif cash > balance:
            balance -= cash  # Negative funds
            print(f"Insufficient funds. A 5% penalty has been applied.")
            print(f"Balance is ${balance:.2f}.")
            break
        else:
            balance -= cash
            print(f"Successfully withdrawn ${cash}. Your new balance is ${balance:.2f}.")
            break  # Exit the loop
    return balance

def get_choice():
    while True: # Main Page
        choice = input("Please select an option: \t- (V)iew Balance\n\t- (D)eposit,\n\t- (W)ithdraw,\n\t- (E)xit:").strip().upper()
        if choice in ('V', 'D', 'W', 'E'):
            return choice
        else:
            print("Invalid Choice Please Enter: V, D, W, E ")

atm() # Run the function














