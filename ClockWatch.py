ts = int(input("Input total seconds: \n")) #Total seconds input variable

m = (ts / 60) #Minutes
h = (ts / 3600) / 1 #Hours

print("{:.0f} seconds equals {:.0f} hours and {:.0f} minutes".format(ts,h,m))
