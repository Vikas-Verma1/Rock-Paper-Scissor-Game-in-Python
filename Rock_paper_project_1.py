import random

# Generate a random number between 1 and 3 

computer = random.randint(1, 3)

your = (input("Enter your choice :"))

reverseDict = {1:"Rock", 2:"Paper", 3:"Ciser"}
yourDict = {"r":1, "p":2, "c":3}

yourstr = yourDict[your]


if(computer == yourstr):
       print("It's a Draw !")
       print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")

else:
    if(computer == 1 and yourstr == 2):
        print("You Win !")
        print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")

    elif(computer == 1 and yourstr == 3):
        print("You Loose !")
        print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")

    elif(computer == 2 and yourstr == 1):
        print("You Loose !")
        print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")

    elif(computer == 2 and yourstr == 3):
        print("You win !")
        print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")

    elif(computer == 3 and yourstr == 1):
        print("You Win !")
        print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")

    elif(computer == 3 and yourstr == 2):
        print("You Loose !")
        print(f"Computer choose :{reverseDict[computer]} \n Your Choice :{reverseDict[yourstr]}")