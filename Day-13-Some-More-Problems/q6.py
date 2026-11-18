n1 = int(input("First number: "))
n2 = int(input("Second number: "))

smallest = min(len(str(n1)), len(str(n2)))
count = 0

while True:
    if n1%10 == n2%10:
        count += 1
    n1 = n1//2
    n2 = n2//2

    if n1 == 0 or n2 == 0:
        break

print(count)
