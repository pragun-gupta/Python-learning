#Write a Python program to calculate the number of days between two dates.
from datetime import date

dt1 = date(2026,11,2)
dt2 = date(2026,11,20)

final = dt2 - dt1

print(final.days)