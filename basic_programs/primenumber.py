# Project: Prime Number Checker
# Author: Tharun
# Description: A Python program that checks whether a given number
#              is prime using loop-based divisibility logic.


a = int(input("Enter a number to check if it's prime: "))

is_prime = True

for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break

if is_prime and a > 1:
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")
