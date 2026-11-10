#Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

num1 = input("Enter first number")
num2 = input("Enter the second number")

product = int(num1)*int(num2)

if product <= 1000:
    print(product)
else:
    sum = int(num1)+int(num2)
    print(sum)