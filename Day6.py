#Q1 Take n numbers from the user, store them in a list, and find the largest number.
"""
numbers = []
for i in range(5):
    num = int(input("Enter numbers : "))
    numbers.append(num)

print("List : ",numbers)
print("largest number is :", max(numbers))
"""




#Q2 Take n numbers from the user and calculate the sum of only the even numbers.
"""
numbers = []
for i in range (5):
    num = int(input("Enter numbers :"))
    numbers.append(num)

even_sum = 0
for n in numbers:
    if n % 2 == 0:
        even_sum += n

print("Sum of even numbers: ", even_sum)
"""

#Q3 Take a sentence from the user and count how many times each word appears.

sentence = input("Enter a sentence :")
words = sentence.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)