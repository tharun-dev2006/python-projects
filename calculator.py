# Project: CLI Calculator
# Author: Tharun
# Description: A simple command line calculator supporting basic arithmetic operations.

def add(a, b):
    print("Total:", a + b)

def sub(a, b):
    print("Difference:", a - b)

def multiply(a, b):
    print("Product:", a * b)

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Division:", a / b)


def main():
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        op = input("Enter your operation (1-4): ")

        if op == '1':
            add(a, b)
        elif op == '2':
            sub(a, b)
        elif op == '3':
            multiply(a, b)
        elif op == '4':
            divide(a, b)
        else:
            print("Invalid choice!")

        again = input("\nDo you want another calculation? (y/n): ")

        if again.lower() != 'y':
            print("Goodbye!")
            break


main()