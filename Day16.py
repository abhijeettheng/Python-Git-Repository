#Q1. Write a Python function to calculate the average of numbers in a list.

"""
def avg_num(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers:", numbers)
print("Average:", avg_num(numbers))
"""



#Q2. Write a Python function to reverse a string.

"""
def reverse_string(sentence):
    sentence = sentence[::-1]
    return sentence
sentence = input("Enter sentence: ")
print(reverse_string(sentence))
"""

#Q3. Write a Python function to find the factorial of a number using recursion.

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter n: "))
print(factorial(n))