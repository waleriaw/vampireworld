#print("The world is beautiful! Enjoy it!")
#regime = input("Do you prefer day or night?")
#name = input("What is your name?")
#print(f"Your name is {name} and you are awake at {regime}")

print()

name =input("What's your name?")
print(f"Welcome to vampire world {name}")
print("Do you believe in vampires?")

believe = input("Press 1 for  yes, 2 for no. >")

if believe == "1":
    print("Very well, you'll enjoy the game!")
elif believe == "2":
    print("Well, then this game will expand your horizons!")
else:
    print("You better make up your mind")


print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input(">")

if door == "1":
    print("There is a nice vampire asking if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input(">")

    if vampire == "1":
        print("Congratulations, you found a new friend!")
    elif vampire == "2":
        print("Sorry, the vampire is faster. You become a dinner.")
    else:
        print("You are not so good with numbers, are you?")

elif door == "2":
    print("There is a cute green snake asking if you can code in python.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Politely decline")

    vampire = input(">")
    if vampire == "1":
        print("Congratulations, you are now member of python guild")
    elif vampire == "2":
        print("Sssss...Would you like to learn python? Sss...")
        print("What do you do?")
        print("1. Smile and nod")
        print("2. Decline and run")

        vampire = input(">")

        if vampire == "1":
            print("Congratulations, you are now taking part in Beginner for Python workshop")
        elif vampire == "2":
            print("Sorry, the snake is faster. You become dinner.")
        else:
            print("You are not so good with numbers, are you?")

    else:
        print("You are not so good with numbers, are you?")


else:
    print("You are not so good with numbers, are you?")


