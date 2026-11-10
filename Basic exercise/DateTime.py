#Write a Python program to display the current date and time.

# %Y: Year with century (e.g., 2023).
#%m: Month as a zero-padded decimal number (01-12).
#%d: Day of the month as a zero-padded decimal number (01-31).
#%H: Hour (24-hour clock) as a zero-padded decimal number (00-23).
#%M: Minute as a zero-padded decimal number (00-59).
#%S: Second as a zero-padded decimal number (00-59).

import datetime

# Create a datetime object representing the current date and time
now = datetime.datetime.now()

# Display a message indicating what is being printed
print("Current date and time : ")

# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Use the 'strftime' method to format the datetime object as a string with the desired format