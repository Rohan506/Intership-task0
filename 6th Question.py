#Write a python program to print the Fibonacci series and
#also check if a given input number is Fibonacci number or not.
def fib(n):
    a=0
    b=1

    if n==1:
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("Enter a number"))
fib(n)

#Checking a number whether it is fibonacci or not
import math
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False
def isFibonacciNumber(n):
    res1 = 5*n*n+4
    res2 = 5*n*n-4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False

num = int(input("Enter an integer number: "))

if isFibonacciNumber(num):
    print (num, "is a Fibonacci number")
else:
    print (num, "is not a Fibonacci number")

