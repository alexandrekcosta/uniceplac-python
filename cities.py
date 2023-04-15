co = str(input("Enter city name(4 options:Mumbai,Belagua,Shrasvati,Kishoreganj): "))

if co == "Mumbai":
    print("COUNTRY:INDIA/IN\n"
          "GDP:$3.737 trillion\n"
          "CITY:MUMBAI\n"
          "GDP per capita:$606.625 billion\n")

elif co == "Belagua":
    print("COUNTRY:BRAZIL/BR\n"
          "GDP:$1.810 billion\n"
          "CITY:BELAGUA\n"
          "GDP per capita:R$6.920\n")

elif co == "Shrasvati":
    print("COUNTRY:INDIA/IN\n"
          "GDP:$3.737 trillion\n"
          "CITY:SHRASVATI\n"
          "GDP per capita:R$ 2\n")

elif co == "Kishoreganj":
    print("COUNTRY:BANGLADESH/BD\n"
          "GDP:$421 billion\n"
          "CITY:KISHOREGANJ\n"
          "GDP per capita:R$85\n")

else:
    print("Invalid input")

gdpPCCondition = float(input("Enter GDP per capita value (no float point): \n"))

if gdpPCCondition >= 2000:
    print("Value input is above 2 thousands,so there is bellow a list of cities which DON'T deserve Extra Municipal Auxiliary Fund:\n"
          "MUMBAI\n"
          "BELAGUA\n")

elif gdpPCCondition <= 2000:
    print("Value input is bellow 2 thousands,so there is bellow a list of cities which DESERVE Extra Municipal Auxiliary Fund:\n"
          "SHRASVATI\n"
          "KISHOREGANJ\n")