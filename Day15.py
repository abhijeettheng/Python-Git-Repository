#Q1. Write a Python program to find the second largest number in a list.


numbers = []

for i in range(5):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)

sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]

print("List:", numbers)
print("Second largest number is:", second_largest)







#Q2 Write a Python function to count the number of words in a given sentence.

"""
def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    return word_count

sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))
"""





#Q3. Write a Python function to check if a number is a prime number or not.

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
