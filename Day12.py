#Q1. Write a Python program to find the factorial of a number using a function.
"""
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    return fact

num = int(input("Enter a number:"))
print("Factorial is", factorial(num))
"""



#Q2. Write a Python program to check if a number is prime using a function.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
"""




#Q3. Write a Python program to find the Fibonacci sequence using a function.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

terms = int(input("Enter number of terms: "))
fibonacci(terms)
