n = int(input("Enter a number which is bigger than 0: "))

remainder = 0
temp_n = n
mylist = []

while temp_n != 0:
    remainder = temp_n % 2
    temp_n = temp_n //2
    mylist.append(remainder)

for i in range(len(mylist)):
    print(mylist[len(mylist)-i-1], end="")