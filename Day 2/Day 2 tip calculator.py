print("Welcome to the tip calculator !")

bill = float(input(("What was the total bill? $")))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

total_bill = bill +(bill*tip/100)

people = int(input("How many people to split the bill? "))

print(f"Each person should pay ${round((total_bill/people),2)}")
