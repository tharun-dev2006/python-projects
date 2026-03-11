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