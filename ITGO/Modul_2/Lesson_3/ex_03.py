a = int(input("Enter the number:"))

if not a % 2 and not a % 3:
    print("Kratno 2 and 3")

if not a % 2 and not a % 5:
    print("Kratno 2 and 5")

if a <= 10 or a >= 50:
    print("a not belong to rande (10; 50)")

if a > 10 and a < 50:
    print("a belong to rande (10; 50)")
