v1 = int(input("Enter 1st value: \n"))
v2 = int(input("Enter 2nd value: \n"))
o = int(input("Enter operation you wish to calculate: 1-Sum,2-Subtraction,3-Multiplication,4-Division: \n"))
r = 0

if o == 1:
    r = v1 + v2
    print("Sum of {} + {} equals {}".format(v1,v2,r))
elif o == 2:
    r = v1 - v2
    print("Subtraction of {} - {} equals {}".format(v1,v2,r))
elif o == 3:
    r = v1 * v2
    print("Multiplication of {} * {} equals {}".format(v1,v2,r))
elif o == 4:
    r = v1 / v2
    print("Division of {} / {} equals {}".format(v1,v2,r))
else:
    print("Invalid option")