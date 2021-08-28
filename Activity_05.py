numbers = input("Enter the 5 numbers in a single line: ")
list = numbers.split()
sum = 0
for i in list:
	sum = sum + int(i)
print("The sum of all the numbers is: %d" %(sum))
