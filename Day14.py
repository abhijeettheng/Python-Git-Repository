#Q1. Write a Python function to check if a string is a palindrome.
"""
def check_palindrome(word):
    if word == word[::-1]:
        print(word,"is a palindrome")
    else:
        print(word,"is not a plaindrome")

word = input("Enter the word:")
check_palindrome(word)
"""



#Q2. Write a Python function to count vowels and consonants in a string.
"""
def vowels_consonants(sentence):
    vowels = 0
    consonants = 0

    for ch in sentence:  # loop through each character
        if ch.lower() in "aeiou":      # if it's a vowel
            vowels += 1
        elif ch.isalpha():             # if it's a consonant
            consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
sentence = input("Enter a sentence: ")
vowels_consonants(sentence)
"""



#Q3. Write a Python function to find the factorial of a number (using recursion).

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
