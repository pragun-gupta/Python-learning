# Python Cheatsheet

## Terminal commands
- cd: Opens the directory file
- python --version: Shows the version of python installed
- python ____.py: Runs the files and provides the output 

## Input and output
- input("text"): asks the user to type something and gives it back as a string.
- print(x): shows a value. 
- print(f"Length: {len(url)}") puts values inside text.

## Strings
- len(s): number of characters
- s.isdigit(): True if the character is a digit
- s.startswith('https'): True if the string begins with that text
- input('URL: '): returns what the user typed.
- len(): counts characters in a string.
- strip(): So it doesn't count spaces

## Loopa and Conditions
- for ch in url: goes through a string one character at a time.
- if condition: runs the indented lines only when the condition is True.

## Counting pattern
- Start count = 0 before the loop, if inside it, count += 1 when it matches, then print after the loop.

## Lists and dictionaries
- (add)

## Files
- (add)

## Git
- git status: see what changed
- git add .: stage everything
- git commit -m "msg": save a snapshot
- git push: send it to GitHub

## Mistakes I made 

- I stored True/False in my counter and it overwrote the tally. Use a separate counter and an if.
- Printing inside versus after the loop changes how many times it runs.
- A terminal command runs in the folder shown in the prompt, so python file.py fails if the file is in another folder.
- Typing python then >>> means I’m inside Python, and exit() gets me out.