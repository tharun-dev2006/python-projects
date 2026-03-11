# Project: Fibonacci Generator
# Author: Tharun
# Description: A simple Python program that generates Fibonacci numbers
#              up to a given limit using loops and basic logic.

num = 20
a = 0
b = 1
count = 1

while count > num :
    print (a , end = " ")

    c = a + b
    a = b
    b = c
    count += 1 