cname = str(input("Enter name of country: \n"))
gdp = int(input("Enter GDP of country: \n"))
city = str(input("Enter a city name: \n"))
gdpPC = int("Enter GDP per capita of {}\n".format(city))
population = int(input("Enter population of {}\n".format(city)))
areakm2 = int(input("Enter area per square of {}\n:".format(city)))

if gdpPC <=2000 and population <= 20000 and areakm2 <= 100000:
    print("{} is a city which is eligible for Extra Money for Municipal Fund!\n"
          "DATA OF CITY\n"
          "GDP per capita:{}\n"
          "Population:{}\n"
          "Area per square:{}\n"
          "Country which city is located:{}\n"
          "GDP of {}\n ".format(city,gdpPC,population,areakm2,cname,gdp))
else:
    print("{} is a city which is NOT eligible for Extra Money for Municipal Fund!\n"
          "DATA OF CITY\n"
          "GDP per capita:{}\n"
          "Population:{}\n"
          "Area per square:{}\n"
          "Country which city is located:{}\n"
          "GDP of {}\n ".format(city, gdpPC, population, areakm2, cname, gdp))