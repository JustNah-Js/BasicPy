print("Welcome to the tempurature Converter Program.")
name = input("\nHello, please type your name : ")
print("\nHi!", name)
print("""\nPlease type in the number of your service Temp. converter:
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celsius
3 - Celsius to Kelvin
4 - Kelvin to Celsius 
and I will give you its equivalent temperature
in your chosen sevice.""")
serv = input("\nEnter your service [1/2/3/4]: ")
if serv == "1":
  print("\nCelsius to Fahrenheit Converter")
  num = input("Temp. in Celsius : ")
  total = float(num) * 9 / 5 + 32
  print("\n" , total ,"Degree fahrenheit")
elif serv == "2":
  print("\nFahrenheit to Celsius Converter")
  num = input("Temp. in Fahrenheit : ")
  total = (float(num) - 32) * 5 / 9
  print("\n",total ,"Degree Celsius")
elif serv == "3":
  print("Celsius to Kelvin Converter")
  num = input("Temp. in Celsius : ")
  total = float(num) + 273.15
  print ("\n" , total ,"Degree Kelvin")
elif serv == "4":
  print("Kelvin to Celsius Converter")
  num = input("Temp. in Kelvin : ")
  total = float(num) - 273.15
  print ("\n" , total ,"Degree Celsius")
else:
  print("\nThere is no service for your request.")
print("\nPress the enter key to exit")