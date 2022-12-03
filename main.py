import random

print("This is a new beginning.")

#numberfeature
#output: array with numbers between 32 and 255
def numberfeature():
    m = 32
    n = 255
    num = []
    for i in range (m,n+1):
        num.append(i)
    return num
print(numberfeature())

#random numbers
print(random.randint(0,9))
def zufallszahl():
    return(random.randint(32,255))
print(zufallszahl())

