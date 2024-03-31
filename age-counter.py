aq = 0
uq = 0
for c in range(1,7 +1):
    age = int(input("{}. Enter your age: ".format(c)))

    if age >= 21:
        aq += 1
    else:
        uq += 1

print("There is {} adult persons".format(aq))
print("There is {} underage persons".format(uq))
