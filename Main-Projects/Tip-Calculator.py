# Tip calculator app
print("Welcome to the tip calculator!!")
bill = float(input("What is the total bill? "))
tip = int(input("What percentage tip would you like to giv? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Finding the tip in percentages
tip_amount = tip/100 * bill

# Adding the tip amount to the bill
total_bill = bill + tip_amount

# Spliting the bill
each_person = total_bill/people

# Rounding down to decimal places
final_amount = round(each_person, 2)
print(f"Each person should pay: {final_amount}")
