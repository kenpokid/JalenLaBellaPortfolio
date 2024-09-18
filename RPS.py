import random

while True:
    choice = input("Choose Rock, Paper, or Scissors\n")
    computerChoice = ["rock", "paper", "scissors"]
    computer = random.choice(computerChoice)
    print("You chose " + choice + " computer chose " + computer)
    if choice.lower() == computer.lower():
        print("Its a tie!")
    elif choice.lower() == "rock":
        if computer.lower() == "paper":
            print("You lose!")
        else:
            print("Congratulations you have won!")
    elif choice.lower() == "paper":
        if computer.lower() == "scissors":
            print("You lose!")
        else:
            print("Congratulations you have won!")
    elif choice.lower() == "scissors":
        if computer.lower() == "rock":
            print("You lose!")
        else:
            print("Congratulations you have won!")
    
    again = input("Would you like to try again(y/n)\n")
    if again.lower() == "n":
        break
