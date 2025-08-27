import random
print("Welcome to rock, paper, scissors")
choice = int(input("What do you choose, 0 for rock, 1 for paper and 2 for scissors: "))
print(f"You chose: ")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

if choice == 0:
    print(rock_paper_scissors[0])
elif choice == 1:
    print(rock_paper_scissors[1])
elif choice == 2:
    print(rock_paper_scissors[2])



print("The computer chose: ")
computer = random.randint(0,2)
print(rock_paper_scissors[computer])

if computer == 0 and choice == 2:
    print("The computer wins")
elif choice == 0 and computer == 2:
    print("Player wins")
elif computer == 2 and choice == 1:
    print("The computer wins")
elif choice == 2 and computer == 1:
    print("Player wins")
elif computer == 1 and choice == 0:
    print("Computer wins")
elif choice == 1 and computer == 0:
    print("Player wins")
elif choice == computer:
    print("It's a draw")
else: print("The input is incorrect! You Lose!")
