#Question 1 
"""
name = "Abhijeet"
print("Hello",name, "Welcome to Python!")
"""




#Question 2
#Takes a number as input and prints whether it is even or odd.
"""
number = int(input("Enter a number: "))

if(number %2 == 0):
    print(number,"is even")
else:
    print(number,"is odd")
"""





#Q3:
#Takes 5 numbers as input (from the user), stores them in a list, and then prints the largest number.
"""
number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))
number3 = int(input("Enter Number 3 : "))
number4 = int(input("Enter Number 4 : "))
number5 = int(input("Enter Number 5 : "))

print(number1)
print(number2)
print(number3)
print(number4)
print(number5)

largest = max(number1, number2, number3, number4, number5)
print("The largest number is ", largest)
"""


numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = max(numbers)
print("The largest number is", largest)
