#Q1. Write a Python function to check whether a number is even or odd.

"""
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input("Enter n: "))
(even_odd(n))
"""


#Q2. Write a Python function that takes a list and returns the sum of all positive numbers.

"""
def sum_pos(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

numbers = []

for i in range(5):
    num = int(input(f"Enter num {i+1} : "))
    numbers.append(num)

print("List of numbers: ", numbers)
print("Sum of positive numbers: ",sum_pos(numbers))
"""






#Q3. Write a Python function to count the number of uppercase and lowercase letters in a given string.


def count_case(sentence):
    count_uppercase = 0
    count_lowercase = 0

    for letter in sentence:
        if letter.isupper():
            count_uppercase += 1
        elif letter.islower():
            count_lowercase += 1

    print("Number of Uppercase letters:", count_uppercase)
    print("Number of Lowercase letters:", count_lowercase)

sentence = input("Enter a sentence: ")
count_case(sentence)
