def inputs():
    m = int(input("Enter the start number: "))
    n = int(input("Enter the stop number: "))
    return m, n

def odd_num(m, n):
    for i in range(m, n+1):
        if(i%2 != 0):
            print(i, end=",")

def main():
    m, n = inputs()
    odd_num(m, n)

main()
