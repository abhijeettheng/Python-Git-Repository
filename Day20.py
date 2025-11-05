#Q1. Write a Python function to find the sum of digits of a given number.

"""
def sum_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = int(input("Enter a number: "))
print("Sum of digits:",sum_digits(number))
"""





#Q2. Write a Python program to find the smallest number in a list without using min().

"""
numbers = []

for i in range(5):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number


print("List:",list(numbers))
print("This is the smallest number:",smallest)
"""







#Q3. Write a Python function that returns the factorial of a number using recursion.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial is:", factorial(n))
