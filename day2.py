# Tip Calculator Project
# This program calculates how much each person should pay when splitting a bill, including the tip.

# Greet the user
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to an integer
total = int(input("What was the total bill? $"))

# Ask the user how much tip they would like to give (10%, 12%, or 15%) and convert to integer
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))

# Ask how many people will split the bill and convert to integer
people = int(input("How many people to split the bill? "))

# Calculate each person's share
# First calculate the total bill including tip, then divide by number of people
share = (total * (tip / 100) + total) / people

# Format the share to always show 2 decimal places
formatted_share = "{:.2f}".format(share)

# Display the final amount each person should pay
print(f"Each person should pay: ${formatted_share}")

