def input_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2

def add(a, b):
    return a+b

def display(a, b, sum):
    print("%d + %d = %d" %(a, b, sum))

def main():
    a, b = input_numbers()
    summation = add(a, b)
    display(a, b, summation)

main()
