url = input("URL : ").strip()
print(f"Length: {len(url)}")

digit_count = 0
for ch in url:
    if ch.isdigit():
        digit_count+=1
print(f"Digits: {digit_count}")