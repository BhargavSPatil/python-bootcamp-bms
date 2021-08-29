import math
def inputs():
    num = int(input("Enter a number: "))
    return num

def prime_num(num):
    flag = 0    
    for i in range(2, int(math.sqrt(num)+1)):
        if(num%i == 0):
            flag = 1
            break
    return flag

def display(flag, num):
    if(flag == 0):
        print(num, " is a prime number")
    else:
        print(num, " is not a prime number")

def main():
    num = inputs()
    flag = prime_num(num)
    display(flag, num)

main()
