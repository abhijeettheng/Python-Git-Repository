#Q1. Find the Second Largest Number in a List
"""
numbers = []

for i in range(5):
    num = int(input(f"Enter the numbers {i+1} :"))
    numbers.append(num)

sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]
print("Second Largest: ", second_largest)
print("List :",numbers)
"""

#Q2 Count the Frequency of Each Character in a String
"""
word = input("Enter the word:")

freq = {}
for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
"""


#Q3 Remove Duplicates from a List

numbers = []

for i in range(5):
    num = int(input(f"Enter the numbers {i+1} :"))
    numbers.append(num)

unique_numbers = list(set(numbers))
print(unique_numbers)
print("List :",numbers)