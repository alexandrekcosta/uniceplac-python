cname = str(input("Enter name of country\n"))
gdp = int(input("Enter GDP of country\n"))
city = str(input("Enter a city name\n"))
gdpPC = int(input("Enter GDP per capita of city\n"))
population = int(input("Enter population of city\n"))
areakm2 = int(input("Enter area per square of city\n"))
PercentValue = int(input("Enter a percentage value\n"))
FundValue = gdp - (gdp * PercentValue / 100)
t = FundValue - gdp

if gdpPC <=2000 and population <= 20000 and areakm2 <= 100000:
    print("This city which is eligible for Extra Money for Municipal Fund!\n"
          "EXTRA-MUNICIPAL FUND VALUE TO RECEIVE:{}\n"
          "DATA OF CITY\n"
          "GDP per capita:{}\n"
          "Population:{}\n"
          "Area per square:{}\n"
          "Country which city is located:{}\n"
          "GDP of {}\n ".format(t,gdpPC,population,areakm2,cname,gdp))
else:
      print("This city is NOT eligible for Extra Money for Municipal Fund!\n"
          "DATA OF CITY\n"
          "GDP per capita:{}\n"
          "Population:{}\n"
          "Area per square:{}\n"
          "Country which city is located:{}\n"
          "GDP of {}\n ".format(gdpPC, population, areakm2, cname, gdp))