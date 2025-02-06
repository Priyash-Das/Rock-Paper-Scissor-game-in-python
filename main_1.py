import random

'''
1 = Rock
-1 = Paper
0 = Scissors
'''

youDict = {"r" : 1, "p" : -1, "s" : 0, "rock" : 1, "paper" : -1, "scissors" : 0, "R" : 1, "P" : -1, "S" : 0, "ROCK" : 1, "PAPER" : -1, "SCISSORS" : 0, "Rock" : 1, "Paper" : -1, "Scissors" : 0}
reverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}

while True:
    computer = random.choice([-1,0,1])
    you_chose = input("Enter your choice (Rock/Paper/Scissors): ")
    you = youDict[you_chose]

    print(f"\nYou chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    print("----------------------------------------------------------------")
    if(computer == you):
        print("It's a draw!\n")
        continue  # Restart the loop if it's a draw
    else:
        if(computer == -1 and you == 0):
            print("You win!")
        elif(computer == -1 and you == 1):
            print("You lose!")
        elif(computer == 0 and you == -1):
            print("You Lose!")
        elif(computer == 0 and you == 1):
            print("You win!")
        elif(computer == 1 and you == -1):
            print("You win!")
        elif(computer == 1 and you == 0):
            print("You lose!")
        else:
            print("Somthin went wrong!")
    print("----------------------------------------------------------------")
    break  # Exit loop if it's not a draw