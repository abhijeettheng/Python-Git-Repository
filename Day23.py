#Q1. Write a Python function to count the number of vowels in a given string.

"""
def count_vowels(sentence):
    count = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            count += 1
    return count

sentence = input("Enter a sentence: ")
print(count_vowels(sentence))
"""






#Q2. Write a Python program to reverse a list without using the reverse() method.

"""
numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

reversed_list = numbers[::-1]
print("Original list:", numbers)
print("Reversed list:", reversed_list)
"""







#Q3. Write a Python function to check if two strings are anagrams of each other.


def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if anagram(word1, word2):
    print("The words are anagrams!")
else:
    print("The words are not anagrams.")
