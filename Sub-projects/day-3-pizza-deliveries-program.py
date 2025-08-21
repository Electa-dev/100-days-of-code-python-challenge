print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
    print("You ordered a small pizza!")
elif size == "M":
    bill = 20
    print("You ordered a medium pizza!")
elif size == "L":
    bill = 25
    print("You ordered a large pizza!")
else: print("Not a valid order!!")

if pepperoni == "Y":
    print("Added pepperoni!")
    if size == "S":
        bill += 2
    else: bill += 3
elif pepperoni == "N":
    print("No pepperoni added!")
else:
    print("Enter the exact values shown.")

if extra_cheese == "Y":
    bill += 1
    print("Added cheese!")
else: print("No added cheese!")

print(f"Your final bill is ${bill}.")
