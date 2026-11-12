n = int(input("Enter a number: "))

num1 = 0
count = 0

while num1 ** 2 <= n:
    num2 = 0

    while num2 ** 2 <= n:
        if num1 ** 2 + num2 ** 2 == n:
            print(num1, num2)
            count += 1

        num2 += 1

    num1 += 1

if count == 0:
    print(0)
