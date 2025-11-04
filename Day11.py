#Q1. Write a Python program to find the sum of all even numbers in a list.
"""
numbers = []

for i in range(5):
    num = int(input(f"Enter the number {i+1} :"))
    numbers.append(num)

total = 0
for num in numbers:
    if num % 2 ==0:
        total += num

print("List:", numbers)
print("Sum of even numbers:", total)
"""



#Q2. Find the Number of Vowels in a Sentence
"""
sentence = input("Write the sentence:").lower()

count = 0
for ch in sentence:
    if ch in "aeiou":
        count += 1

print("Number of vowels in sentence:",count)
"""




#Q3. Find the Factorial of a Number

n = int(input("Enter the number:"))

fact = 1

for i in range(1, n+1):
    fact = fact * i

print(fact)