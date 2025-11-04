#Q1 Take a number and also a range limit as input. Print its multiplication table up to that limit.
"""
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

for i in range(1,limit+1):
    print(num,"x",i,"=",num*i)
"""

#Q2 Take a word as input and count how many vowels (a, e, i, o, u) are present.
"""
word = input("Enter a word: ")
count = 0
for ch in word:
    if ch in "aeiouAEIOU":
        count +=1
print(count)
"""

#Q3 Take a string input and check if it reads the same backward as forward.

word = input("Enter a word : ")

if word == word[::-1]:
    print(word,"is palindrome")

else:
    print(word,"is not palindrome")