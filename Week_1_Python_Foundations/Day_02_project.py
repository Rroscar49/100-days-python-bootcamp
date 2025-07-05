# Day 2 Project - Code goes here

print("Welcome to the Tip Calculator!")

# Ask the user for the total bill amount
total_bill = float(input("What was the total bill? $"))

# Ask the user how much tip they want to give (as a percentage)
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people to split the bill
num_people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate the total bill including tip
total_with_tip = total_bill + tip_amount

# Calculate how much each person should pay
amount_per_person = total_with_tip / num_people

# Format the amount per person to 2 decimal places
final_amount = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${final_amount}")
