#Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

num1 = 20
num2 = 40

product = num1*num2

if product <= 1000:
    print(product)
else:
    print(num1+num2)