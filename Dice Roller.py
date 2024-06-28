#!/usr/bin/env python3

import random

def die():
    die = random.randint(1,6)
    return die
def main():
    print("Dice Roller")
    print()
    roll = input("Roll the dice? (y/n): ")
    while roll.lower() == "y":
        roll1 = die()
        print("dice 1 = ", roll1)
        roll2 = die()
        print("dice 2 = ", roll2)
        total = roll1 + roll2
        print("total: ", total)
        print()
        if total == 2:
            print("Snake eyes!\n")
        elif total == 12:
            print ("Boxcars!\n")
        else:
            roll = input("Roll again (y/n): ")
            
if __name__=="__main__":
    main()
