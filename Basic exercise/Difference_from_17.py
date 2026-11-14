#Write a Python program to calculate the difference between a given number and 17. 
#If the number is greater than 17, return twice the absolute difference.

print("The difference between a given number and 17. /nIf the number is greater than 17, returns twice the absolute difference.")
num = int(input("Enter a number: "))

if num < 17:
    a = 17 - num
    print("The difference is",a)
else: 
    b = (num - 17)*2
    print("The difference is",b)
