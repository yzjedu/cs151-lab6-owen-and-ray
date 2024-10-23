# Programmers:  [Owen and Rayan]
# Course:  CS151, [Professor Z]
# Due Date: [10/24/2024]
# Programming Assignment:  [Lab 6]
# Problem Statement:  [Calculating functions of an ATM]
# Data In: [menu choice (d,w,v,e)]
# Data Out:  [What their current balance is, if they input a invalid input]
# Credits: [Lecture note 18]
# Display the purpose of the program ......

# Constants
starting_balance = 1000
penalty_rate = 0.05

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


def view_balance(balance):
    print(f"Your balance is {balance}")


def deposit(balance):
    while True:
        cash = input("How much money would you like to deposit? ")
        if not cash.isdigit():
            print ("Invalid cash")
        else:
            cash = int(cash)
        if cash < 0:
            print ("Invalid cash")
        else:
            balance += cash
            print ("Your new balance is " + str(balance))
            break
        return balance

def withdraw(balance):
    while True:
        cash = int(input("How much money would you like to withdraw? "))
        if cash > balance:
            print (balance * penalty_rate)
        elif cash < 0:
            print ("You cannot withdraw negative cash")
        else:
            balance -= cash
            print ("Succesfully withdrawn balance " + str(balance))
            break
        return balance

def get_choice():
    while True:
        choice = input(" ")











