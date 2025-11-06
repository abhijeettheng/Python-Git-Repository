#Q1. Write a Python function to check whether a number is perfect number or not.

"""
def perfect(n):
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div == (n)

n = int(input("Enter the number:"))
if perfect(n):
    print(n, "is a perfect number.")
else:
    print(n, "is not a perfect number.")
"""








#Q2. Write a Python program to print all even numbers from a list.

"""
numbers = []

for i in range(5):
    num = int(input(f"Enter the number {i+1}: "))
    numbers.append(num)
print("List:",numbers)

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers:",even_numbers)
"""



#Q3. Write a Python function to return the count of words in a file.


def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

filename = "Day21Q3.txt"
print("Total words in file:", count_words_in_file(filename))
