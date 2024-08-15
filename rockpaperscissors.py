# Bot will randomly choose one of the options
# Enter one of available commands: 'rock'/'paper'/'scissors' to play
# Enter 'score' to see Wins/Loses in current session, enter 'exit' to leave
import random
wins = int(0)
loses = int(0)
while True:
    botchoice = random.randint(1, 3)
    if botchoice == 1:
        botchoice = "rock"
    elif botchoice == 2:
        botchoice = "paper"
    else:
        botchoice = "scissors"
    playerchoice = input("rock/paper/scissors/score/exit: ").lower()
    if playerchoice == "rock":
        if botchoice == "rock":
            print("Draw")
        if botchoice == "paper":
            print("You lose!")
            loses = loses + 1
        if botchoice == "scissors":
            print("You won!")
            wins = wins + 1
    elif playerchoice == "paper":
        if botchoice == "rock":
            print("You won!")
            wins = wins + 1
        if botchoice == "paper":
            print("Draw")
        if botchoice == "scissors":
            print("You lost!")
            loses = loses + 1
    elif playerchoice == "scissors":
        if botchoice == "rock":
            print("You lost!")
            loses = loses + 1
        if botchoice == "paper":
            print("You won!")
            wins = wins + 1
        if botchoice == "scissors":
            print("Draw")
    elif playerchoice == "exit":
        break
    elif playerchoice == "score":
        print("Wins:", wins, "Loses:", loses)
    else:
        print("Error")
        continue
    print("Bot chose", botchoice)