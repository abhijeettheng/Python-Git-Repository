#Q1. Count Positive, Negative, and Zero Numbers in a List
"""
numbers = []

for i in range(5):
    num = int(input(f"Enter the numbers {i+1} :"))
    numbers.append(num)

positive = 0
negative = 0
zero = 0

for n in numbers:
    if n>0:
        positive += 1
    elif n<0:
        negative += 1
    else:
        zero += 1
print("Positive :",positive,"Negative :",negative,"Zero :",zero)
"""



#Q2. Find the Largest and Smallest Word in a Sentence
"""
sentence = input("Enter the sentence :")

words = sentence.split()
longest = max(words, key=len)
shortest = min(words, key=len)
print("Longest word is :",longest)
print("Shortest word is :",shortest)
"""





#Q3 Write a program to count how many times each word appears in a sentence.

sentence = input("Enter the sentence: ")
words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
for word, count in freq.items():
    print(word, ":", count)
