from random import randint
player = False
while player == False:
    moves = input("Enter Rock , Paper or scissors or Enter Quit to exit:")
    compmoves = moves[randint(0, 2)]
    if moves == compmoves:
      print("Both players selected the", moves, "It's a tie!")
    elif moves == "rock":
       if compmoves == "scissors":
        print("Rock smashes scissors! You win!")
       else:
        print("Paper covers rock! You lose.")
    elif moves == "paper":
        if compmoves == "rock":
         print("Paper covers rock! You win!")
        else:
         print("Scissors cuts paper! You lose.")
    elif moves == "scissors":
        if compmoves == "paper":
         print("Scissors cuts paper! You win!")
        else:
         print("Rock smashes scissors! You lose.")
    elif moves == "Quit":
     print("Thanks for playing!")
    player = True
    break
else:
    print("This is not a valid play! Check your spelling")
    moves = input("Enter Rock.Paper or scissors")
    compmoves = moves[randint(0, 2)]
