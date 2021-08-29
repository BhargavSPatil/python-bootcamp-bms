def inputs():
    lst1 = list(map(int, input("Enter few numbers in a single line: ").split()))
    lst2 = list(map(int, input("Enter some more numbers in a single line: ").split()))
    return lst1, lst2

#sort()
def sort_method(lst1):   
    lst1.sort()
    print("List 1 - using sort() = ", lst1)

#sorted()
def sorted_method(lst2):
    print("List 2 - using sorted() = ", sorted(lst2))

def main():
    lst1, lst2 = inputs()
    sort_method(lst1)
    sorted_method(lst2)

main()
