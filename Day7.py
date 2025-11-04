#Q1 Take a string input and print it in reverse.
"""
word = input("Enter a word to reverse it : ")
print("Reversed word :",word[::-1])
"""



#Q2 Take a string input and count how many alphabets and how many digits are in it.
"""
string = input("Enter the string :")

alphabets = 0
digits = 0

for ch in string:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1

print("Alphabets", alphabets)
print("Digits", digits)
"""





#Q3 Take a number and check if it’s an Armstrong number or not.

num = int(input("Enter a number :"))
power = len(str(num))
total = 0

for d in str(num):
    total += int(d) ** power

if total == num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")