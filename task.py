print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_with_tips = bill + (bill * tip/100)
total_per_person= total_with_tips / people
tot = round (total_per_person , 2)

print (f"Each person should pay: {tot}")


