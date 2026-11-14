#Write a Python program to get the volume of a sphere with radius six.

from math import pi

r = float(input("Enter the radius to find volumn of sphere: "))

vol = 4.0/3.0 * pi * r**3

print(f"Volumn of the sphere is {vol}")
