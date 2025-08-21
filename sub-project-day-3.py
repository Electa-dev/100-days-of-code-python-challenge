# Even or Odd checker
print("Hello to the even or odd number checker!!")
random_number = int(input("Enter your number here: "))
decision = random_number % 2
if decision == 0:
    print("Even!")
else:
    print("Odd!")
