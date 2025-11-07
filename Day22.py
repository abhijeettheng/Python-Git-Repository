#Q1. Write a Python program to check if a number is a palindrome or not.

"""
number = input("Enter a number: ")
if number == number [::-1]:
    print(number, "is a pallindrome number.")
else:
    print(number, "is not a pallindrome number.")
"""





#Q2. Write a Python function to find the sum of elements in a list.

"""
def sum_elements_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = []

for i in range(5):
    num = int(input(f"Enter a number{i+1} : "))
    numbers.append(num)

print("Sum of elemets is:",sum_elements_list(numbers))
"""



#Q3. Write a Python function to return the largest word in a sentence.


def largest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

sentence = input("Enter a sentence: ")
print("Largest word:", largest_word(sentence))
