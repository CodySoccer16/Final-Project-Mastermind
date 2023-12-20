
import tkinter as tk
from tkinter import *


root = Tk()
root.title("Mastermind")
root.geometry("700x700")

players = 0
player1Score = 0
player2Score = 0
games = 0
currentGame = 1
# Start Button
def btn_player_2():
    players = 2
    startScreen.pack_forget()
    GameAmountScreen.pack(fill="both", expand=True)
    return players
# Start Screen
startScreen = Frame(root,bg="Light Blue")
startScreen.pack(fill="both", expand=True)
title = Label(startScreen, text="𝕸𝖆𝖘𝖙𝖊𝖗𝖒𝖎𝖓𝖉", font=("Gungsuche",100),bg="Light Blue")
title.pack(pady=20)

player2Btn = Button(startScreen, text="𝓢𝓽𝓪𝓻𝓽",font=("Helvetica",50),bg="Lime", command=btn_player_2)
player2Btn.pack(pady=120)


#Game amount Screen

#Button Functions
def btn_games_2():
    global games
    games = 2
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_4():
    global games
    games = 4
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_6():
    global games
    games = 6
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_8():
    global games
    games = 8
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games


#Game Amount Screen
GameAmountScreen = Frame(root,bg="light blue")
title = Label(GameAmountScreen,bg="light blue", text="𝕴𝖓𝖘𝖙𝖗𝖚𝖈𝖙𝖎𝖔𝖓𝖘",font=("Helvetica",50))
Instructions  = Label(GameAmountScreen,bg="light blue", text="Have the player 1 select a code. Next , have the player 2 place there\n first guess. After each guess the computer will give them feedback.\nThe feedback the computer gives you is very important. It will\n either show a red , white or grey square for each box . Red meaning \nyou have a correct color in the correct spot. White meaning you\n have the correct color in the wrong box. And grey meaning you\n have the wrong color in the wrong spot. Keep in mind the feedack\n order does not corrilate with the game board order. Repeat with\n the next row.Continue until the code is guessed or there are no \nmore guesses left.Switch places and play again. The code maker recieves \n 1 point for every guess and 1 bonus point if it cant be guessed in the \n10 guesses. Keep in mind there wil be no duplicates in this game.",font=("Helvetica",15))
numOfGames = Label(GameAmountScreen ,bg="light blue", text = "𝕳𝖔𝖜 𝕸𝖆𝖓𝖞 𝕲𝖆𝖒𝖊𝖘?",font=("Helvetica",50),pady=50)
games2Btn = Button(GameAmountScreen, text="2 𝕲𝖆𝖒𝖊𝖘",bg="lime",font=("Helvetica",25), command=btn_games_2)
games4Btn = Button(GameAmountScreen, text="4 𝕲𝖆𝖒𝖊𝖘",bg="lime",font=("Helvetica",25),command=btn_games_4)
games6Btn = Button(GameAmountScreen, text="6 𝕲𝖆𝖒𝖊𝖘",bg="lime",font=("Helvetica",25), command=btn_games_6)
games8Btn = Button(GameAmountScreen, text="8 𝕲𝖆𝖒𝖊𝖘",bg="lime",font=("Helvetica",25), command=btn_games_8)

title.pack()
Instructions.pack()
numOfGames.pack()
games2Btn.pack(side="left",padx=20)
games4Btn.pack(side="left",padx=20)
games6Btn.pack(side="left",padx=20)
games8Btn.pack(side="left",padx=20)


#Starting values for variables
playerTurn = 0
currentBox = 0
currentAnswer = 0
minRange = -1
maxRange = 4
#Button Commands
def btn_white():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1: # if its an odd game
        if playerTurn % 2 == 0: # if its player 1's turn
            if currentAnswer > minRange and currentAnswer < maxRange: # if the current answer is in range
                answerBoardList[currentAnswer].config(bg="White") # change the color of the answer board
                currentAnswer += 1 # move one box to the right
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange: # if the current box is in range
                gameboardList[currentBox].config(bg="White") # change the color of the gameboard
                currentBox += 1 # move one box to the right
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0: # if its an even game
        if playerTurn % 2 == 1: # if its player 2's turn
            if currentAnswer > minRange and currentAnswer < maxRange: # if the current answer is in range
                answerBoardList[currentAnswer].config(bg="White") # change the color of the answer board
                currentAnswer += 1 # move one box to the right
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange: # if the current box is in range
                gameboardList[currentBox].config(bg="White") # change the color of the gameboard
                currentBox += 1 # move one box to the right
                return currentBox
            else:
                print("Out of Range")

def btn_blue(): #This is the same as btn_white but with blue
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Blue")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Blue")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Blue")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Blue")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")

def btn_purple(): #This is the same as btn_white but with purple
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Purple")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Purple")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Purple")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Purple")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")

def btn_pink(): #This is the same as btn_white but with pink
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Pink")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Pink")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Pink")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Pink")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")

def btn_orange(): #This is the same as btn_white but with orange
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Orange")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Orange")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Orange")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Orange")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")

def btn_black(): #This is the same as btn_white but with black
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Black")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Black")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="Black")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="Black")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")


def btn_delete():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if currentGame % 2 == 1: # if its an odd game
        if playerTurn % 2 == 0: # if its player 1's turn
            if currentAnswer > 0 and currentAnswer-1 > minRange and currentAnswer-1 < maxRange: # if the current answer is in range
                currentAnswer -= 1 # move one box to the left
                answerBoardList[currentAnswer].config(bg="Dark Grey") # change the color of the answer board back to grey
        else: # if its player 2's turn
            if currentBox > 0 and currentBox-1 > minRange and currentBox-1 < maxRange: # if the current box is in range
                currentBox -= 1 # move one box to the left
                gameboardList[currentBox].config(bg="Dark Grey") # change the color of the gameboard back to grey
    elif currentGame % 2 == 0: # if its an even game
        if playerTurn % 2 == 1: # if its player 2's turn
            if currentAnswer > 0 and currentAnswer-1 > minRange and currentAnswer-1 < maxRange: # if the current answer is in range
                currentAnswer -= 1 # move one box to the left
                answerBoardList[currentAnswer].config(bg="Dark Grey") # change the color of the answer board back to grey
        else: # if its player 1's turn
            if currentBox > 0 and currentBox-1 > minRange and currentBox-1 < maxRange: # if the current box is in range
                currentBox -= 1 # move one box to the left
                gameboardList[currentBox].config(bg="Dark Grey")  # change the color of the gameboard back to grey

answerColors = []
boxColors = []
def btn_enter():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, player1Score, player2Score, answerColors, timesChecked, boxColors
    if currentGame % 2 == 1: # if its an odd game
        if playerTurn % 2 == 0: # if its player 1's turn
            if currentAnswer == 4: # if the current answer is in range
                for i in range(4): # for each box in the answer board check if color is a duplicate
                    if answerBoardList[i].cget("bg") in answerColors:
                        print("No duplicates")
                    else:
                        answerColors.append(answerBoardList[i].cget("bg"))
                #print(answerColors)
                if len(answerColors) == 4: #if there are no duplicates
                    playerTurn += 1 # move to player 2's turn
                    updateInstructLabel() # update the instructions
                    cover.place(x=28,y=590) # place the cover over the gameboard
            else:
                print("Not Enough Colors")
            
        else:
            if currentBox % 4 == 0 and currentBox != 0 and ((currentBox / 4) > timesChecked): # if the current box is in range
                for i in range(currentBox-4, currentBox): # for each box in the gameboard check if color is a duplicate
                    if gameboardList[i].cget("bg") in boxColors: 
                        print("No duplicates")
                    else:
                        boxColors.append(gameboardList[i].cget("bg"))
                if len(boxColors) == 4: #if there are no duplicates
                    winCheck() # check if the player won
                    minRange += 4 # move the range of the gameboard
                    maxRange += 4 # move the range of the gameboard
                    player1Score += 1 # add a point to player 1
                    updateScore() # update the score
                    boxColors = [] # reset the box colors
            else:
                print("Not Enough Colors")
    elif currentGame % 2 == 0: #same as above but for even games with players 1 and 2 switched
        if playerTurn % 2 == 1:
            if currentAnswer == 4:
                for i in range(4):
                    if answerBoardList[i].cget("bg") in answerColors:
                        print("No duplicates")
                    else:
                        answerColors.append(answerBoardList[i].cget("bg"))
                if len(answerColors) == 4:
                    playerTurn += 1
                    updateInstructLabel()
                    cover.place(x=28,y=590)
            else:
                print("Not Enough Colors")
        else:
            if currentBox % 4 == 0 and currentBox != 0 and ((currentBox / 4) > timesChecked):
                for i in range(currentBox-4, currentBox):
                    if gameboardList[i].cget("bg") in boxColors:
                        print("No duplicates")
                    else:
                        boxColors.append(gameboardList[i].cget("bg"))
                if len(boxColors) == 4:
                    winCheck()
                    minRange += 4
                    maxRange += 4
                    player2Score += 1
                    updateScore()
                    boxColors = []
            else:
                print("Not Enough Colors")



timesChecked = 0     
def winCheck():
    global timesChecked, minRange, maxRange, answerBoardList, gameboardList, answerColors, player1Score, player2Score
    totalCorrect = 0 #set start values
    totalClose = 0 #set start values
    if timesChecked == 0: # if its the first time checking
        for i in range(minRange+1, maxRange):
            if gameboardList[i].cget("bg") == answerBoardList[i].cget("bg"): # if the color is in the correct spot
                totalCorrect += 1 # add one to the total correct
            else:
                if gameboardList[i].cget("bg") in answerColors: # if the color is in the answer but not in the correct spot
                        totalClose += 1 # add one to the total close
        timesChecked += 1 # add one to the times checked
    elif timesChecked > 0 and timesChecked < 10: # if its not the first time checking and its not the last time checking
        for i in range(minRange+1, maxRange): # for each box in the gameboard
            if gameboardList[i].cget("bg") == answerBoardList[i - (4 * timesChecked)].cget("bg"): # had to change to i - 4 * times checked to not go out of range
                totalCorrect += 1 # add one to the total correct
            else: 
                if gameboardList[i].cget("bg") in answerColors: # if the color is in the answer but not in the correct spot
                        totalClose += 1 # add one to the total close
        timesChecked += 1 # add one to the times checked
        

    #These if statements change the color of the feedback boxes based on the total correct and total close
    #Every situation is covered
    if totalCorrect == 4:
        guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 1].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 2].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 3].config(bg="Red")
        updateScore() # add a point to the player
        resetBoard() # reset the board for next game

 
    elif totalCorrect == 3:
        guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 1].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 2].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
    elif totalCorrect == 2:
        if totalClose == 2:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="White")
        elif totalClose == 1:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
        else:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
    elif totalCorrect == 1:
        if totalClose == 3:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="White")
        elif totalClose == 2:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
        elif totalClose == 1:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
        else:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
    elif totalCorrect == 0:
        if totalClose == 4:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="White")
        elif totalClose == 3:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
        elif totalClose == 2:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
        elif totalClose == 1:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="White")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")
        else:
            guessReturn[((timesChecked-1) * 4) + 0].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 1].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 2].config(bg="Dark Grey")
            guessReturn[((timesChecked-1) * 4) + 3].config(bg="Dark Grey")

    if timesChecked == 10: # if its the last time checking and the player didnt win
        #add one bonus point to the code maker
        if playerTurn % 2 == 0: 
            player2Score += 1
            updateScore()
        else:
            player1Score += 1
            updateScore()
        resetBoard() # reset the board for next game




def updateScore():
    global player1Score, player2Score
    player1Scorelbl.config(text=str(player1Score)) # update the score labels
    player2Scorelbl.config(text=str(player2Score)) # update the score labels

def updateInstructLabel(): 
    #This changes the instructions based on the player turn and the game number
    global playerTurn, currentGame, games
    if currentGame % 2 == 1: 
        instructText.config(text=f"Player 2 make \nyour guess")
    elif currentGame % 2 == 0:
        instructText.config(text=f"Player 1 make \nyour guess")

def resetBoard():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, answerColors, timesChecked, currentGame, games
    if currentGame +1 <= games: # if there are still games left
        currentGame += 1 # move to the next game
        #Reset colors on board
        for i in range(4):
            answerBoardList[i].config(bg="Dark Grey")
        for i in range(40):
            gameboardList[i].config(bg="Dark Grey")
        for i in range(40):
            guessReturn[i].config(bg="Dark Grey")
        #Reset variables
        answerColors = []
        currentBox = 0
        currentAnswer = 0
        minRange = -5
        maxRange = 0
        timesChecked = 0
        cover.place_forget() # remove the cover
        #change label accordingly
        if currentGame % 2 == 1:
            instructText.config(text=f"Player 1 make \nyour code")
        elif currentGame % 2 == 0:
            instructText.config(text=f"Player 2 make \nyour code")

    else: # if there are no games left
        #Change Label to display winner or if there is a tie
        if int(player1Score) > int(player2Score + 1):
            instructText.config(text=f"Game Over\n Player 1 wins")
        elif int(player2Score) > (player1Score + 1):
            instructText.config(text=f"Game Over\n Player 2 wins")
        elif int(player1Score) == int(player2Score + 1):
            instructText.config(text=f"Game Over\n Its a tie")
        



#Game Screen

GameScreen = Frame(root, width=700, height=700)
#gameboard background
gameboard = Label(GameScreen, bg= "Grey", height=42, width=40, borderwidth=8, relief="groove", )
gameboard.place(x=25,y=25)
#gameboard boxes
gameboardList = []
for i in range(10):
    for j in range(4):
        gameboardList.append(Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2))
        gameboardList[i*4+j].place(x=40+(45*j),y=40+(55*i))

#code boxes
answerBoardList = []
for i in range(4):
    answerBoardList.append(Label(GameScreen, bg= "Dark Grey", height=3, width=6, borderwidth=2))
    answerBoardList[i].place(x=40+(60*i),y=600)

#guess return boxes
guessReturn = []
amountPlaced = 0
for i in range(10):
    for j in range(4):
            guessReturn.append(Label(GameScreen, bg= "Dark Grey", height=1, width=2))
            guessReturn[i*4+j].place(x=220+(22*j),y=46+(55*i))

#cover
cover = Label(GameScreen, bg= "Black", height=4, width=39, borderwidth=8)


#keypad
keyPad = Label(GameScreen , bg="grey",height=20 , width=40 , borderwidth = 5 , relief="groove") #background
keyPad.place(x=400 , y=190)
White = Button(GameScreen, bg= "White",height=6 , width=12, command=btn_white) #white button
White.place(x=405 ,y= 30 + 165)
Blue = Button(GameScreen, bg= "blue",height=6 , width=12, command=btn_blue) #blue button
Blue.place(x=500 ,y= 30+ 165)
Purple = Button(GameScreen, bg= "purple",height=6 , width=12, command=btn_purple) #purple button
Purple.place(x=595 ,y= 30+ 165)
Pink = Button(GameScreen, bg= "pink",height=6 , width=12, command=btn_pink) #pink button
Pink.place(x=405 ,y= 130+ 165)
Orange = Button(GameScreen, bg= "Orange",height=6 , width=12, command=btn_orange) #orange button
Orange.place(x=500 ,y= 130+ 165)
Orange = Button(GameScreen, bg= "Black",height=6 , width=12, command=btn_black) #black button
Orange.place(x=595,y= 130+ 165)
Enter = Button(GameScreen , bg="Green" , height = 5, width=10,text="Enter", command=btn_enter) #enter button
Enter.place(x=460 , y=245+ 165)
Delete= Button(GameScreen, bg= "Red",height=5 , width=10 , text="Delete", command=btn_delete) #delete button
Delete.place(x=560 ,y= 245+ 165)

#score
scoreBoard = Label(GameScreen, bg="grey",height=8 , width=40 , borderwidth = 5 , relief="groove") #background
scoreBoard.place(x=400 , y=540)
player1Label = Label(GameScreen,text="Player 1 Score:", font=("comic Sans", 25),  bg="grey") #player 1 score label
player1Label.place(x=405 , y=465 + 80)
player2Label = Label(GameScreen,text="Player 2 Score:",font=("comic Sans", 25), bg="grey") #player 2 score label
player2Label.place(x=405 , y=525 + 80)
player1Scorelbl = Label(GameScreen,text=str(player1Score),font=("comic Sans", 25), bg="grey") #player 1 score
player1Scorelbl.place(x=640 , y=465 + 80)
player2Scorelbl = Label(GameScreen,text=str(player2Score),font=("comic Sans", 25), bg="grey") #player 2 score
player2Scorelbl.place(x=640 , y=525 + 80)

#instructions
inGameinstructions = Label(GameScreen, bg="grey",height=8 , width=40 , borderwidth = 5 , relief="groove") #background
inGameinstructions.place(x=400 , y=25)
instructText = Label(GameScreen,bg = "grey", text=f"Player 1 make \nyour code",font=("comic Sans", 30)) #instructions
instructText.place(x=415 , y=35) 



root.mainloop()
