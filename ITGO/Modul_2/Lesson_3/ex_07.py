n = input("Enter a number:") # Programm count a number of zeros

count_zero = 0

for ch in n:
    if ch == "0":
        count_zero += 1

print(count_zero)