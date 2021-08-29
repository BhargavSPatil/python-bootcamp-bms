def compare(a, b, c):
    if(a>=b and a>=c):
        return a
    elif(b>a and b>=c):
        return b
    else:
        return c

num1, num2, num3 = map(int, input("Enter the three numbers: "). split())

large_num = compare(num1, num2, num3)

print("%d is the greatest number among %d, %d and %d" %(large_num, num1, num2, num3))
