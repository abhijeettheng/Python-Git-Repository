#Q1. Write a Python function that takes a list of numbers and returns the largest number.
"""
def list_numbers(numbers):
    return max(numbers)

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}:"))
    numbers.append(num)

print("List:", numbers)
print("Largest number is:", list_numbers(numbers))
"""

#Q2. Write a Python function to check if a number is even or odd.
"""
def even_odd(number):
    return (number)

number = int(input("Enter a number:"))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")
"""



#Q3. Write a Python function that returns the sum of all elements in a list.

def sum_list(numbers):
    return sum(numbers)

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("List:", numbers)
print("Sum of all numbers:", sum_list(numbers))