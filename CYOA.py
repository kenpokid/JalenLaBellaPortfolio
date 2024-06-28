name = input("Tell me your name: ")
print("Greetings,", name,"Join me on this adventure through the rain forest")

Q1 = input("as we you start your adventure you hear a growling sound in the distance. Do you...\n"
           "A) Investigate the sound\n"
           "B) Pretend you didnt hear it and continue along\n"
           "C) Turn back to where you came from never to return again\n"
           "D) Hide and pray it doesn't find you\n")
if Q1.lower() == "a":
    Q2 = input("You slowy approach the sound you heard when you pull back the bushes to find a hurt baby bear. Do you...\n"
               "A) Look for its mother\n"
               "B) See if you can help it\n"
               "C) Leave it to die\n"
               "D) Give it some of your food?\n")
    if Q2.lower() == "a":
        Q3 = input("You find the cubs mother and she tries to attack you when she sees you near her baby. Do you...\n"
                   "A) Run away\n"
                   "B) Fight back\n"
                   "C) Give her your sandwhich\n")
        if Q3.lower() == "a":
            print("You try to run but she catches you. You are her dinner. GAME OVER!")
        elif Q3.lower() == "b":
            print("You try to do the crane kick from the karate kid but she catches your foot with her mouth and swallows you whole. GAME OVER!")
        elif Q3.lower() == "c":
            print("You give her you sandwhich and she thanks you by letting you return home unharmed. GAME OVER!")
        else:
            print("Not a valid answer.")
    elif Q2.lower() == "b":
        Q6 = input("You try to help the bear when a hungry tiger shows up. Do you...\n"
                   "A) Try to fight it\n"
                   "B) Try and run away\n")
        if Q6.lower() == "a":
            print("You go to try to lunge at the tiger when the mama bear shows up. She stops the tiger and takes care of her cub. In the meantime you escape and leave the jungle. GAME OVER!")
        elif Q6.lower() == "b":
            print("You try to run but the tiger catches you. Its game over")
        else:
            print("Not a valid answer.")
    elif Q2.lower() == "c":
        Q7 = input("You leave the bear cub and you come across a stream. Do you...\n"
                   "A) Follow the stream\n"
                   "B) Drink from the stream\n")
        if Q7.lower() == "a":
            Q8 = input("You go down stream until you reach a beautiful waterfall. Do you...\n"
                       "A) Go for a swim\n"
                       "B) Take a picture\n")
            if Q8.lower == "a":
                print("While swimming you are attacked by a water python and it eats you. GAME OVER!")
            elif Q8.lower == "b":
                print("You take a great picture and then return home to show it to your friends. GAME OVER!")
        elif Q7.lower() == "b":
            print("You drink from the stream when your stomach starts feeling funny. You pass away a few minutes later. GAME OVER!")
    elif Q2.lower() == "d":
        print("You feed the bear your sandwich and it becomes your friend. You take it home to be your new pet. GAME OVER!")
    else:
        print("Not a valid answer.")
elif Q1.lower() == "b":
    Q4 = input("You continue along the path when all of sudden you trip and scrape your knee. Do you...\n"
               "A) Walk it off\n"
               "B) try to call for help\n"
               "C) Clean it in the near by river\n"
               "D) Amputate your leg\nj" )
    if Q4.lower() == "a":
        print("You try to shrug off the pain but you begin to limp and when you cant go anymore you succomb to the pain and lay there and evemtually pass away. GAME OVER!")
    elif Q4.lower() == "b":
        Q9 = input("You scream for help until a man aproaches and offers to help. Do you...\n"
                   "A) Trust the man\n"
                   "B) Tell him youll handle it yourself\n")
        if Q9.lower() == "a":
            print("The man bandages your leg and takes you back home to rest. GAME OVER!")
        if Q9.lower() == "b":
            Q10 = input("The man helps you any way by carrying you to his camp where they have a camp doctor. You start feeling better. Do you..."
                        "A) Join the friendly camp\n"
                        "B) Continue on your own\nj")
            if Q10.lower() == "a":
                Q11 = input("You join the camp and the chief wants you to join its hunting unit however the town builder wants you join the house builders. You also notice the daughter of the chief winking at you. Do you...\n"
                            "A) Join the hunters\n"
                            "B) Join the builders\n" 
                            "C) Flirt with the chiefs daughter\n")
                if Q11.lower() == "a":
                    print("You join the hunters but in a freak accident you get mauled by a tiger. GAME OVER!")
                elif Q11.lower() == "b":
                    print("You join the builders and live out your days as the best builder in town. GAME OVER!")
                elif Q11.lower() == "c":
                    print("You marry the Chiefs daughter and have 12 kids with her, you become the next chief. GAME OVER!")
                else:
                    print("Not a valid answer.")
            elif Q10.lower() == "b":
                print("You try to continue on your own but as soon as you leave camp the hunters hunt you down for leaving. GAME OVER!")
            else:
                print("Not a valid answer.")
    elif Q4.lower() == "c":
        print("You try to clean your leg but the river infects it and you pass away. GAME OVER!")
    elif Q4. lower() == "d":
        print ("You amputate your leg and now you cant move. you sit and wait until you starve to death. GAME OVER!")
    else:
        print("Not a valid answer.")
elif Q1.lower() == "c":
    print("You go home and miss out on the adventure of a lifetime. GAME OVER!")
elif Q1.lower() == "d":
    Q5 = input("You hide up a tree where you find a birds nest full of eggs. Do you...\n"
        "A) Try to eat the eggs\n"
        "B) Jump back down\n")
    if Q5.lower() == "a":
        print("You try to eat the eggs but the mama bird returns and pecks you to death. GAME OVER!")
    elif Q5.lower() == "b":
        print("You jump down but on the way down you hit a branch and you break all of your bones and pass away. GAME OVER!")
    else:
        print("Not a valid answer.")
else: 
    print("Not a valid answer.")
     
        