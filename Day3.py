#Q1 Write a program that prints all even numbers from 1 to 50.
"""
for num in range(1,51):
    if num % 2 == 0:
        print(num)
"""



#Q Write a program that calculates the sum of all numbers from 1 to N, where N is given by the user.
"""
N = int(input("Enter a number : "))
total = 0

for i in range(1,N+1):
    total = total + i

print("The sum is",total)
"""





#Q3 Write a program that checks if a given string is a palindrome (the same forwards and backwards).

word = input("Enter a word : ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")