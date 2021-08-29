m = int(input("Enter the start number: "))
n = int(input("Enter the stop number: "))
for i in range(m, n+1):
    if(i%2 != 0):
        print(i, end=",")
