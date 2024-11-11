#Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the priciple amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero ")

while rate <= 0:
    rate = float(input("Enter the intereset rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero ")

while time <=0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equla to zero")

total = principle * pow((1 + rate / 100),time) 

print(f"Balance after {time} year/s: ₹{total:.2f}")