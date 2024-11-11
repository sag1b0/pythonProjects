# Python Weight Convertor

weight = float(input("Enter your Weight: "))
unit = input("Kilogram or Pounds (Input K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your Weight is {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your Weight is {round(weight, 2)} {unit}")

else:
    print(f"{unit} is not valid")