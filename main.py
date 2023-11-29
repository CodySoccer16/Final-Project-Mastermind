import tkinter as tk
from tkinter import *


root = Tk()
root.title("Mastermind")
root.geometry("500x500")

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



startScreen.pack()
root.mainloop()