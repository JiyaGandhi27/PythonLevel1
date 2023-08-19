import random
moves = input("Enter Rock.Paper or scissors")
compmoves = [random.choice(moves)]
if moves == compmoves:
    print("Both players selected the",moves,"It's a tie!")
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