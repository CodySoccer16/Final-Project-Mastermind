
import tkinter as tk
from tkinter import *


root = Tk()
root.title("Mastermind")
root.geometry("700x700")

players = 0
# button Functions
def btn_player_1():
    players = 1
    startScreen.pack_forget()
    GameAmountScreen.pack()
    return players
def btn_player_2():
    players = 2
    startScreen.pack_forget()
    GameAmountScreen.pack()
    return players


def btn_games_2():
    games = 2
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_4():
    games = 4
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_6():
    games = 6
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_8():
    games = 8
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games
def btn_games_10():
    games = 10
    GameAmountScreen.pack_forget()
    GameScreen.pack()
    return games


# Start Screen
startScreen = Frame(root)
title = Label(startScreen, text="Mastermind")
title.pack()
player1Btn = Button(startScreen, text="1 Player", command=btn_player_1)
player2Btn = Button(startScreen, text="2 Player", command=btn_player_2)
player1Btn.pack()
player2Btn.pack()

#Game Amount Screen
GameAmountScreen = Frame(root)
title = Label(GameAmountScreen, text="How Many Games?")
Instructions  = Label(GameAmountScreen, text="Instructions Here")
games2Btn = Button(GameAmountScreen, text="2 Games", command=btn_games_2)
games4Btn = Button(GameAmountScreen, text="4 Games", command=btn_games_4)
games6Btn = Button(GameAmountScreen, text="6 Games", command=btn_games_6)
games8Btn = Button(GameAmountScreen, text="8 Games", command=btn_games_8)
games10Btn = Button(GameAmountScreen, text="10 Games", command=btn_games_10)
title.pack()
Instructions.pack()
games2Btn.pack()
games4Btn.pack()
games6Btn.pack()
games8Btn.pack()
games10Btn.pack()

#Game Screen

#gameboard
GameScreen = Frame(root, width=700, height=700)
gameboard = Label(GameScreen, bg= "Grey", height=42, width=35, borderwidth=8, relief="groove", )
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
for i in range(10):
    for j in range(4):
        guessReturn.append(Label(GameScreen, bg= "Dark Grey", height=1, width=2))
        guessReturn[i*4+j].place(x=200+(25*j),y=40+(55*i))

#cover
cover = Label(GameScreen, bg= "Black", height=4, width=34, borderwidth=8)
#cover.place(x=28,y=590)

playerTurn = 0
currentBox = 0
currentAnswer = 0
minRange = -1
maxRange = 4
#Button Commands
def btn_white():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
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

def btn_blue():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer > minRange and currentAnswer < maxRange:
            answerBoardList[currentAnswer].config(bg="blue")
            currentAnswer += 1
            return currentAnswer
        else:
            print("Out of Range")
    else:
        if currentBox > minRange and currentBox < maxRange:
            gameboardList[currentBox].config(bg="blue")
            currentBox += 1
            return currentBox
        else:
            print("Out of Range")

def btn_purple():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer > minRange and currentAnswer < maxRange:
            answerBoardList[currentAnswer].config(bg="purple")
            currentAnswer += 1
            return currentAnswer
        else:
            print("Out of Range")
    else:
        if currentBox > minRange and currentBox < maxRange:
            gameboardList[currentBox].config(bg="purple")
            currentBox += 1
            return currentBox
        else:
            print("Out of Range")

def btn_pink():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer > minRange and currentAnswer < maxRange:
            answerBoardList[currentAnswer].config(bg="pink")
            currentAnswer += 1
            return currentAnswer
        else:
            print("Out of Range")
    else:
        if currentBox > minRange and currentBox < maxRange:
            gameboardList[currentBox].config(bg="pink")
            currentBox += 1
            return currentBox
        else:
            print("Out of Range")

def btn_orange():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer > minRange and currentAnswer < maxRange:
            answerBoardList[currentAnswer].config(bg="orange")
            currentAnswer += 1
            return currentAnswer
        else:
            print("Out of Range")
    else:
        if currentBox > minRange and currentBox < maxRange:
            gameboardList[currentBox].config(bg="orange")
            currentBox += 1
            return currentBox
        else:
            print("Out of Range")

def btn_black():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer > minRange and currentAnswer < maxRange:
            answerBoardList[currentAnswer].config(bg="black")
            currentAnswer += 1
            return currentAnswer
        else:
            print("Out of Range")
    else:
        if currentBox > minRange and currentBox < maxRange:
            gameboardList[currentBox].config(bg="black")
            currentBox += 1
            return currentBox
        else:
            print("Out of Range")


def btn_delete():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer > 0 and currentAnswer-1 > minRange and currentAnswer-1 < maxRange:
            currentAnswer -= 1
            answerBoardList[currentAnswer].config(bg="Dark Grey")
    else:
        if currentBox > 0 and currentBox-1 > minRange and currentBox-1 < maxRange:
            currentBox -= 1
            gameboardList[currentBox].config(bg="Dark Grey")

answerColors = []
def btn_enter():
    global playerTurn, currentBox, currentAnswer, minRange, maxRange
    if playerTurn % 2 == 0:
        if currentAnswer == 4:
            for i in range(4):
                answerColors.append(answerBoardList[i].cget("bg"))
            #print(answerColors)
            playerTurn += 1
        else:
            print("Not Enough Colors")
        cover.place(x=28,y=590)
    else:
        winCheck()
        minRange += 4
        maxRange += 4

timesChecked = 0     
def winCheck():
    global timesChecked, minRange, maxRange, answerBoardList, gameboardList, answerColors
    totalCorrect = 0
    totalClose = 0
    if timesChecked == 0:
        for i in range(minRange+1, maxRange):
            print(gameboardList[i].cget("bg"), answerBoardList[i].cget("bg"))
            if gameboardList[i].cget("bg") == answerBoardList[i].cget("bg"):
                totalCorrect += 1
            else:
                if gameboardList[i].cget("bg") in answerColors:
                        totalClose += 1
        timesChecked += 1
    else:
        for i in range(minRange+1, maxRange):
            #print(gameboardList[i].cget("bg"), answerBoardList[i - (4 * timesChecked)].cget("bg"))
            if gameboardList[i].cget("bg") == answerBoardList[i - (4 * timesChecked)].cget("bg"):
                totalCorrect += 1
            else:
                if gameboardList[i].cget("bg") in answerColors:
                        totalClose += 1
        timesChecked += 1
    print(totalCorrect, totalClose)




#keypad
keyPad = Label(GameScreen , bg="grey",height=20 , width=40 , borderwidth = 5 , relief="groove")
keyPad.place(x=400 , y=10)
White = Button(GameScreen, bg= "White",height=6 , width=12, command=btn_white)
White.place(x=405 ,y= 15)
Blue = Button(GameScreen, bg= "blue",height=6 , width=12, command=btn_blue)
Blue.place(x=500 ,y= 15)
Purple = Button(GameScreen, bg= "purple",height=6 , width=12, command=btn_purple)
Purple.place(x=595 ,y= 15)
Pink = Button(GameScreen, bg= "pink",height=6 , width=12, command=btn_pink)
Pink.place(x=405 ,y= 115)
Orange = Button(GameScreen, bg= "Orange",height=6 , width=12, command=btn_orange)
Orange.place(x=500 ,y= 115)
Orange = Button(GameScreen, bg= "Black",height=6 , width=12, command=btn_black)
Orange.place(x=595,y= 115)
Enter = Button(GameScreen , bg="Green" , height = 5, width=10,text="Enter", command=btn_enter)
Enter.place(x=460 , y=230)
Delete= Button(GameScreen, bg= "Red",height=5 , width=10 , text="Delete", command=btn_delete)
Delete.place(x=560 ,y= 230)














startScreen.pack()
root.mainloop()
