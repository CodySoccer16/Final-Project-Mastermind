
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
# button Functions
def btn_player_2():
    players = 2
    startScreen.pack_forget()
    GameAmountScreen.pack(fill="both", expand=True)
    return players


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

# Start Screen
startScreen = Frame(root,bg="Light Blue")
startScreen.pack(fill="both", expand=True)
title = Label(startScreen, text="𝕸𝖆𝖘𝖙𝖊𝖗𝖒𝖎𝖓𝖉", font=("Gungsuche",100),bg="Light Blue")
title.pack(pady=20)

player2Btn = Button(startScreen, text="𝓢𝓽𝓪𝓻𝓽",font=("Helvetica",50),bg="Lime", command=btn_player_2)
player2Btn.pack(pady=120)

  

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





#Game Screen
#gameboard
GameScreen = Frame(root, width=700, height=700)
gameboard = Label(GameScreen, bg= "Grey", height=42, width=40, borderwidth=8, relief="groove", )
gameboard.place(x=25,y=25)
gameboardList = []
for i in range(10):
    for j in range(4):
        gameboardList.append(Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2))
        gameboardList[i*4+j].place(x=40+(45*j),y=40+(55*i))
#gameboardList[1].config(bg="White")
#special boxes
answerBoardList = []
for i in range(4):
    answerBoardList.append(Label(GameScreen, bg= "Dark Grey", height=3, width=6, borderwidth=2))
    answerBoardList[i].place(x=40+(60*i),y=600)

guessReturn = []
amountPlaced = 0
for i in range(10):
    for j in range(4):
            guessReturn.append(Label(GameScreen, bg= "Dark Grey", height=1, width=2))
            guessReturn[i*4+j].place(x=220+(22*j),y=46+(55*i))



#cover
cover = Label(GameScreen, bg= "Black", height=4, width=39, borderwidth=8)
#cover.place(x=28,y=590)

playerTurn = 0
currentBox = 0
currentAnswer = 0
minRange = -1
maxRange = 4
#Button Commands
def btn_white():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, games
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="White")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="White")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > minRange and currentAnswer < maxRange:
                answerBoardList[currentAnswer].config(bg="White")
                currentAnswer += 1
                return currentAnswer
            else:
                print("Out of Range")
        else:
            if currentBox > minRange and currentBox < maxRange:
                gameboardList[currentBox].config(bg="White")
                currentBox += 1
                return currentBox
            else:
                print("Out of Range")

def btn_blue():
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

def btn_purple():
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

def btn_pink():
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

def btn_orange():
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

def btn_black():
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
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer > 0 and currentAnswer-1 > minRange and currentAnswer-1 < maxRange:
                currentAnswer -= 1
                answerBoardList[currentAnswer].config(bg="Dark Grey")
        else:
            if currentBox > 0 and currentBox-1 > minRange and currentBox-1 < maxRange:
                currentBox -= 1
                gameboardList[currentBox].config(bg="Dark Grey")
    elif currentGame % 2 == 0:
        if playerTurn % 2 == 1:
            if currentAnswer > 0 and currentAnswer-1 > minRange and currentAnswer-1 < maxRange:
                currentAnswer -= 1
                answerBoardList[currentAnswer].config(bg="Dark Grey")
        else:
            if currentBox > 0 and currentBox-1 > minRange and currentBox-1 < maxRange:
                currentBox -= 1
                gameboardList[currentBox].config(bg="Dark Grey")

answerColors = []
def btn_enter():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, player1Score, player2Score, answerColors, timesChecked
    if currentGame % 2 == 1:
        if playerTurn % 2 == 0:
            if currentAnswer == 4:
                for i in range(4):
                    if answerBoardList[i].cget("bg") in answerColors:
                        print("No duplicates")
                    else:
                        answerColors.append(answerBoardList[i].cget("bg"))
                #print(answerColors)
                if len(answerColors) == 4:
                    playerTurn += 1
                    updateInstructLabel()
                    cover.place(x=28,y=590)
            else:
                print("Not Enough Colors")
            
        else:
            if currentBox % 4 == 0 and currentBox != 0 and ((currentBox / 4) > timesChecked):
                winCheck()
                minRange += 4
                maxRange += 4
                player1Score += 1
                updateScore()
            else:
                print("Not Enough Colors")
    elif currentGame % 2 == 0:
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
                winCheck()
                minRange += 4
                maxRange += 4
                player2Score += 1
                updateScore()
            else:
                print("Not Enough Colors")

        
        

timesChecked = 0     
def winCheck():
    global timesChecked, minRange, maxRange, answerBoardList, gameboardList, answerColors, player1Score, player2Score
    totalCorrect = 0
    totalClose = 0
    if timesChecked == 0:
        for i in range(minRange+1, maxRange):
            if gameboardList[i].cget("bg") == answerBoardList[i].cget("bg"):
                totalCorrect += 1
            else:
                if gameboardList[i].cget("bg") in answerColors:
                        totalClose += 1
        timesChecked += 1
    elif timesChecked > 0 and timesChecked < 10:
        for i in range(minRange+1, maxRange):
            #print(gameboardList[i].cget("bg"), answerBoardList[i - (4 * timesChecked)].cget("bg"))
            if gameboardList[i].cget("bg") == answerBoardList[i - (4 * timesChecked)].cget("bg"):
                totalCorrect += 1
            else:
                if gameboardList[i].cget("bg") in answerColors:
                        totalClose += 1
        timesChecked += 1
        
    if totalCorrect == 4:
        guessReturn[((timesChecked-1) * 4) + 0].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 1].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 2].config(bg="Red")
        guessReturn[((timesChecked-1) * 4) + 3].config(bg="Red")
        updateScore()
        resetBoard()

 
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

    if timesChecked == 10:
        if playerTurn % 2 == 0:
            player2Score += 1
            updateScore()
        else:
            player1Score += 1
            updateScore()
        resetBoard()

#keypad
keyPad = Label(GameScreen , bg="grey",height=20 , width=40 , borderwidth = 5 , relief="groove")
keyPad.place(x=400 , y=190)
White = Button(GameScreen, bg= "White",height=6 , width=12, command=btn_white)
White.place(x=405 ,y= 30 + 165)
Blue = Button(GameScreen, bg= "blue",height=6 , width=12, command=btn_blue)
Blue.place(x=500 ,y= 30+ 165)
Purple = Button(GameScreen, bg= "purple",height=6 , width=12, command=btn_purple)
Purple.place(x=595 ,y= 30+ 165)
Pink = Button(GameScreen, bg= "pink",height=6 , width=12, command=btn_pink)
Pink.place(x=405 ,y= 130+ 165)
Orange = Button(GameScreen, bg= "Orange",height=6 , width=12, command=btn_orange)
Orange.place(x=500 ,y= 130+ 165)
Orange = Button(GameScreen, bg= "Black",height=6 , width=12, command=btn_black)
Orange.place(x=595,y= 130+ 165)
Enter = Button(GameScreen , bg="Green" , height = 5, width=10,text="Enter", command=btn_enter)
Enter.place(x=460 , y=245+ 165)
Delete= Button(GameScreen, bg= "Red",height=5 , width=10 , text="Delete", command=btn_delete)
Delete.place(x=560 ,y= 245+ 165)

#score
scoreBoard = Label(GameScreen, bg="grey",height=8 , width=40 , borderwidth = 5 , relief="groove")
scoreBoard.place(x=400 , y=540)
player1Label = Label(GameScreen,text="Player 1 Score:", font=("comic Sans", 25),  bg="grey")
player1Label.place(x=405 , y=465 + 80)
player2Label = Label(GameScreen,text="Player 2 Score:",font=("comic Sans", 25), bg="grey")
player2Label.place(x=405 , y=525 + 80)
player1Scorelbl = Label(GameScreen,text=str(player1Score),font=("comic Sans", 25), bg="grey")
player1Scorelbl.place(x=640 , y=465 + 80)
player2Scorelbl = Label(GameScreen,text=str(player2Score),font=("comic Sans", 25), bg="grey")
player2Scorelbl.place(x=640 , y=525 + 80)

#instructions
inGameinstructions = Label(GameScreen, bg="grey",height=8 , width=40 , borderwidth = 5 , relief="groove")
inGameinstructions.place(x=400 , y=25)
instructText = Label(GameScreen,bg = "grey", text=f"Player 1 make \nyour code",font=("comic Sans", 30))
instructText.place(x=415 , y=35)

def updateScore():
    global player1Score, player2Score
    player1Scorelbl.config(text=str(player1Score))
    player2Scorelbl.config(text=str(player2Score))

def updateInstructLabel(): # fix this to be more accurate
    global playerTurn, currentGame, games
    if currentGame % 2 == 1:
        instructText.config(text=f"Player 2 make \nyour guess")
    elif currentGame % 2 == 0:
        instructText.config(text=f"Player 1 make \nyour guess")

def resetBoard():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange, answerColors, timesChecked, currentGame, games
    if currentGame +1 <= games:
        currentGame += 1
        for i in range(4):
            answerBoardList[i].config(bg="Dark Grey")
        for i in range(40):
            gameboardList[i].config(bg="Dark Grey")
        for i in range(40):
            guessReturn[i].config(bg="Dark Grey")
        answerColors = []
        #playerTurn = 0 # maybe fix this?
        currentBox = 0
        currentAnswer = 0
        minRange = -5
        maxRange = 0
        timesChecked = 0
        #updateInstructLabel()
        cover.place_forget()
        if currentGame % 2 == 1:
            print(currentGame)
            instructText.config(text=f"Player 1 make \nyour code")
        elif currentGame % 2 == 0:
            instructText.config(text=f"Player 2 make \nyour code")

    else:
        print(player1Score, player2Score)
        if int(player1Score) > int(player2Score + 1):
            instructText.config(text=f"Game Over\n Player 1 wins")
        elif int(player2Score) > (player1Score + 1):
            instructText.config(text=f"Game Over\n Player 2 wins")
        elif int(player1Score) == int(player2Score + 1):
            instructText.config(text=f"Game Over\n Its a tie")
        








root.mainloop()
