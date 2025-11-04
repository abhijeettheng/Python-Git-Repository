#Q1. Check if a String is a Pangram
"""
sentence = input("Enter a sentence: ").lower()

if len({ch for ch in sentence if ch.isalpha()}) == 26:
    print("It is a pangram")
else:
    print("Not a pangram")
"""





#Q2. Find the Smallest Number in a List
"""
numbers = []

for i in range(5):
    num = int(input(f"Enter the numbers {i+1}:"))
    numbers.append(num)

smallest_number = min(numbers)
print("List:",numbers)
print("Smallest number is:",smallest_number)
"""



#Q3. Find the Sum of Digits of a Number

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10      
    total += digit        
    num = num // 10       

print("Sum of digits:", total)