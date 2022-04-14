import time
import random

def check():

    if game[0][0]=="X"and game[0][1]== "X" and a [0][2] =="X":
        print ("Player 1 won!")
    if game[1][0]=="X"and game[1][1]== "X" and a [1][2] =="X":
        print ("Player 1 won!")
    if game[2][0]=="X"and game[2][1]== "X" and a [2][2] =="X":
        print ("Player 1 won!")
    if game[0][0]=="X"and game[1][0]== "X" and a [2][0] =="X":
        print ("Player 1 won!")
    if game[0][1]=="X"and game[1][1]== "X" and a [2][1] =="X":
        print ("Player 1 won!")
    if game[0][2]=="X"and game[1][2]== "X" and a [2][2] =="X":
        print ("Player 1 won!")
    if game[0][0]=="O"and game[0][1]== "O" and a [0][2] =="O":
        print ("Player 2 won!")
    if game[1][0]=="O"and game[1][1]== "O" and a [1][2] =="O":
        print ("Player 2 won!")
    if game[2][0]=="O"and game[2][1]== "O" and a [2][2] =="O":
        print ("Player 2 won!")
    if game[0][0]=="O"and game[1][0]== "O" and a [2][0] =="O":
        print ("Player 2 won!")
    if game[0][1]=="O"and game[1][1]== "O" and a [2][1] =="O":
        print ("Player 2 won!")
    if game[0][2]=="O"and game[1][2]== "O" and a [2][2] =="O":
        print ("Player 2 won!")
   


game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

print("Tell me how many you are: ")
players_count = int(input())

start = time.time()

while True:
    print("Player 1")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == " ":
                game[row][col] = "X"
                break
            else:
                print("ghablan por shode")
        else:
            print("beine 0,2 vared she")

    for row in game:
        print(row)
    
    if check():
        break

    print("Player 2")
    if players_count < 2:
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game[row][col] == " ":
                game[row][col] = "O"
                break
    else:
        while True:
            row = int(input())
            col = int(input())
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == " ":
                    game[row][col] = "O"
                    break
                else:
                    print("deghat nakardi bache, try again")
            else:
                print("mese adam vared kon")

    for row in game:
        print(row)
    
    if check():
        break

end = time.time()
running_time = end - start
print(round(running_time), "Seconds")
