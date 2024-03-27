n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
print("INPUT NUMBERS: {},{},{}".format(n1,n2,n3))
if n1 > n2 and n1 > n3:
    print("Number {} is highest between {} and {}".format(n1,n2,n3))
    if n2 < n1 and n2 < n3:
        print("Number {} is lowest between {} and {}".format(n2,n1,n3))
    elif n3 < n1 and n3 < n2:
        print("Number {} is lowest between {} and {}".format(n3,n1,n2))
elif n2 > n1 and n2 > n3:
    print("Number {} is highest between {} and {}".format(n2,n1,n3))
    if n1 < n2 and n1 < n3:
        print("Number {} is lowest between {} and {}".format(n1,n2,n3))
    elif n3 < n1 and n3 < n2:
        print("Number {} is lowest between {} and {}".format(n3,n1,n3))
elif n3 > n1 and n3 > n2:
    print("Number {} is highest between {} and {}".format(n3,n1,n2))
    if n1 < n2 and n1 < n3:
        print("Number {} is lowest between {} and {}".format(n1,n2,n3))
    elif n2 < n1 and n2 < n3:
        print("Number {} is lowest between {} and {}".format(n2,n1,n3))
