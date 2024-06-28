#!/url/bin/env python3
print ("Prime Number Checker\n")

def factors(Guess):
    factorlist = []
    for i in range(1,Guess+1):
        if (Guess%i == 0):
            factorlist.append(i)
    return factorlist
def main ():
    repeat = "y"
    while repeat.lower() == "y":
        Guess = int(input("Please Enter an Integer Between 1 and 5000:"))
        if Guess >= 1 and Guess <= 5000:
            factorlist = factors(Guess)
            if len(factorlist) > 2:
                print("\nThis is NOT a prime number!\n")
                print("There are ",len(factorlist), "factors:" ,factorlist)
                print()
                repeat = input("try again (y/n)?")
            else:
                print("\nThis is a prime number!\n")
                repeat = input("try again (y/n)?")

    print("Bye!")

if __name__=="__main__":
    main()
