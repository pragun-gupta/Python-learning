#Iterate through the first 10 numbers (0–9).
#  In each iteration, print the current number, the previous number, and their sum.

prev_num = 0
for i in range(10):
    sum = prev_num + i
    print(f"Current number {i}, the previous number {prev_num}, their sum {sum}")
    
    prev_num = i