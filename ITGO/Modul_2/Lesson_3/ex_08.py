# Програма, яка знаходить у введеному числі  найбільшу та найменшу цифри

n = input("Enter a number:")  # Programm count a number of zeros

max = int(n[0])
min = int(n[0])

for char in n:
    num = int(char)
    if num > max:
        max = num
    if num < min:
        min = num
print(max, min)
