#Q1. Write a Python function to check if a given list is sorted in ascending order.

"""
def is_sorted(numbers):
    return numbers == sorted(numbers)

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("List:", numbers)

if is_sorted(numbers):
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted.")
"""






#Q2. Write a Python program to remove duplicates from a list without using set().

"""
def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

numbers = []

for i in range(6):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Original List:", numbers)
print("List without duplicates:", remove_duplicates(numbers))
"""






#Q3. Write a Python function to count the frequency of each character in a string.


def char_frequency(string):
    freq = {}  # empty dictionary

    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


# User input
text = input("Enter a string: ")
print("Character Frequency:", char_frequency(text))
