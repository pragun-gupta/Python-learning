# Write a function to remove characters from a string starting from index 0 up to n and return a new string.
# Given Input:
#remove_chars("pynative", 4)
#remove_chars("pynative", 2)

def remove_chars(w,n):
    print("original string", w)

    str = w[n:]
    print(str)

remove_chars("pynative", 4)
remove_chars("pynative", 2)
