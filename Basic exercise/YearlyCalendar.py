#Write a Python program to display a calendar for an entire year.

import calendar

y = int(input("Enter the year for its calendar: "))
print(calendar.calendar(y)) # as a multiline string
#print(calendar.prcal(y))          # directly prints

