#Write a program that takes a word as input and prints each character on a new line.
"""
word = input("Enter a word: ")
for ch in word:
    print(ch)
"""



#Q2 Write a program that prints the multiplication table of a given number.
"""
number = int(input("Enter a number: "))
for i in range(1,11):
    print(number,"x",i,"=",number*i)
"""




#Q3 Write a program that asks the user to enter 5 numbers, stores them in a list, and then prints:
"""
The list itself

The sum of all numbers

The average of the numbers
"""
"""
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))
num5 = int(input("Enter number 5 : "))

sum = num1 + num2 + num3 + num4 + num5
print("Sum : ",sum)

avg = num1 + num2 + num3 + num4 + num5 / 5
print("Average : ",avg)
"""
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
avg = total / len(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", avg)
