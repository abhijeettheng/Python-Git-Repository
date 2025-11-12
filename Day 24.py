#Q1. Write a Python function to find the second smallest number in a list.

"""
def second_smallest(numbers):
    numbers = sorted(numbers)
    return numbers[1]

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("List:", numbers)
print("Second smallest number:", second_smallest(numbers))
"""




#Q2. Write a Python function that returns the count of even and odd numbers in a list.

"""
def count_even_odd(numbers):
    count_even = 0
    count_odd = 0

    for num in numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return count_even, count_odd

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_count, odd_count = count_even_odd(numbers)

print("List:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
"""




#Q3. Write a Python function to check if a string contains only digits.


def check_digits(string):
    if string.isdigit():
        return True
    else:
        return False

string = input("Enter a string: ")

if check_digits(string):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
