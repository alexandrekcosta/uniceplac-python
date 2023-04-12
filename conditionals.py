v = int(input("Input a value: \n"))

if v > 10:
    print("{} is above 10".format(v))
elif v <= 10 and v >= 5:
    print("{} is located between 5 and 10".format(v))
else:
    print("{} is bellow 5".format(v))