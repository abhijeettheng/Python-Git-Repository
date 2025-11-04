#Q1. Write a Python function to check if a string is a palindrome.

"""
def pallindrome(word):
    word = word.lower()
    if word == word[::-1]:
        print(word,"is a palindrome")
    else:
        print(word,"is not a palindrome")

word = input("Enter a word: ")
pallindrome(word)
"""






#Q2. Write a Python program to find the largest element in a list without using max().

"""
numbers = []

for i in range(5):
    number = int(input(f"Enter a number {i+1} : "))
    numbers.append(number)

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
        print("This is the largesr number",largest)

print("List",numbers)
"""



#Q3. Write a Python function to calculate the square of each number in a list and return the new list.


def square(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Original list:", numbers)
print("Squared list:", square(numbers))
