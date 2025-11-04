#Q1. Write a Python function to reverse a string.

"""
def reverse(string):
    return string[::-1]

string = input("Enter a sentence: ")
print(reverse(string))
"""





#Q2. Write a Python function that takes a list and returns a new list with unique elements.

"""
def unique(numbers):
    unique_list = []
    for n in numbers:
        if n not in unique_list:
            unique_list.append(n)
    return unique_list

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Unique numbers:", unique(numbers))
"""








#Q3. Write a Python function to count how many vowels are present in a given string.


def count_vowels(sentence):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in sentence:
        if ch in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))
