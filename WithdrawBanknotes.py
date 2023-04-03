tq = int(input("Input quantity of money: \n")) #Total quantity input variable

ohbn = tq / 100 #One hundred banknote variable
fftbn = tq / 50 #Fifty banknote variable
twbn = tq / 20 #Twenty banknote variable
tnbn = tq / 10 #Ten banknote variable
fivbn = tq / 5 #Five banknote variable
twobn = tq / 2 #Two banknote variable

print("One hundred banknotes: {:.0f}".format(ohbn))
print("Fifty banknotes: {:.0f}".format(fftbn))
print("Twenty banknotes: {:.0f}".format(twbn))
print("Ten banknotes: {:.0f}".format(tnbn))
print("Five Banknotes: {:.0f}".format(fivbn))
print("Two banknotes: {:.0f}".format(twobn))