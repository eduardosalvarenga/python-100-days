# Day 2
# Create a Tip calculator, where you're able to split the bill accordingly with the % tip you wanna pay

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = 1 + (tip / 100)
bill_per_person = round(((bill * bill_with_tip) / people), 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")