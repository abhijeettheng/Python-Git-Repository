#Q1 Write a program to calculate the factorial of a given number using a loop.
"""
num = int(input("Enter a number : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)
"""

#Q2 Fibonacci Sequence (n terms) – Generate the first n terms of the Fibonacci sequence.
"""
n = int(input("Enter a number : "))

a = 0
b = 1

for i in range(n):
    print(a,end=" ")
    a,b = b, a + b
"""




#Q3 Check Prime Number – Take a number as input and check if it is prime or not.
num = int(input("Enter a number : "))

if num > 1:
    for i in range(2,num):
        if num % 1 == 0:
            print(num,"is not a prime")
            break
    else:
        print(num, "is prime")
else:
    print(num, "is not prime")        