num = int(input("Enter a number: "))
flag = 0
for i in range(2, int((num/2)+1)):
    if(num%i == 0):
        flag = 1
        break

if(flag == 0):
    print("The number entered is a prime number")
else:
    print("The number entered is not a prime number")
