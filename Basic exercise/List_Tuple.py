#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

#Sample data: 3, 5, 7, 23

values = input("Enter the values with commas ',' : ")

list = values.split(",")
tuple = tuple(list)

print("list: ", list)
print("tuple: ", tuple)
