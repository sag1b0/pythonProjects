# Python Temperature Converter

temp = float(input("Enter the temperature: "))
unit1 = input("Enter the unit Celsius(C), Fahrenheit(F) or Kelvin(K): ").upper()
unit2 = input("Enter the unit (C, F, or K) you want to convert to: ").upper()

if unit1 == "C" and unit2 == "F":
    temp = (temp * 1.8) + 32
    unit = "Fahrenheit"
    print(f"Temperature is {round(temp, 2)} degrees {unit}")
elif unit1 == "F" and unit2 == "C":
    temp = (temp - 32) / 1.8
    unit = "Celsius"
    print(f"Temperature is {round(temp, 2)} degrees {unit}")
elif unit1 == "C" and unit2 == "K":
    temp = temp + 273.15
    unit = "Kelvin"
    print(f"Temperature is {round(temp, 2)} degrees {unit}")
elif unit1 == "K" and unit2 == "C":
    temp = temp - 273.15
    unit = "Celsius"
    print(f"Temperature is {round(temp, 2)} degrees {unit}")
elif unit1 == "F" and unit2 == "K":
    temp = (temp - 32) / 1.8 + 273.15
    unit = "Kelvin"
    print(f"Temperature is {round(temp, 2)} degrees {unit}")
elif unit1 == "K" and unit2 == "F":
    temp = ((temp - 273.15) * 1.8) + 32
    unit = "Fahrenheit"
    print(f"Temperature is {round(temp, 2)} degrees {unit}")
else:
    print(f"{unit1} to {unit2} is not a valid conversion.")
