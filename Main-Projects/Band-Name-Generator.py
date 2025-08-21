# Simple band name generator made using python
# Made using input and print functions, variables and string concatenation

print("Hello, and welcome to the Band Name Generator!")
city = input("What city did you grow up in?\n")
pet_name = input("What is the name of your pet?\n")
Band_Name = city + " " + pet_name
print("Your Band Name could be " + Band_Name)

# Alternatively it could be this 
print("Hello, and welcome to the Band Name Generator!")
city = input("What city did you grow up in?\n")
pet_name = input("What is the name of your pet?\n")
print("Your Band Name could be " + city + " " + pet_name)
