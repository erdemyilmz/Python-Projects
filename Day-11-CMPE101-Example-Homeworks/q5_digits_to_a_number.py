count = int(input("How many digits: "))
total = 0

for i in range(count):
    digit = int(input("Digit: "))
    total += digit * (10 ** (count - i - 1))

print(total)
