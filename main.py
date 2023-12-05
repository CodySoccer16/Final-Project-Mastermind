
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

box11 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box11.place(x=40,y=40)
box12 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box12.place(x=85,y=40)
box13 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box13.place(x=130,y=40)
box14 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box14.place(x=175,y=40)
box21 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box21.place(x=40,y=95)
box22 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box22.place(x=85,y=95)
box23 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box23.place(x=130,y=95)
box24 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box24.place(x=175,y=95)
box31 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box31.place(x=40,y=150)
box32 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box32.place(x=85,y=150)
box33 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box33.place(x=130,y=150)
box34 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box34.place(x=175,y=150)
box41 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box41.place(x=40,y=205)
box42 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box42.place(x=85,y=205)
box43 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box43.place(x=130,y=205)
box44 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box44.place(x=175,y=205)
box51 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box51.place(x=40,y=260)
box52 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box52.place(x=85,y=260)
box53 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box53.place(x=130,y=260)
box54 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box54.place(x=175,y=260)
box61 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box61.place(x=40,y=315)
box62 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box62.place(x=85,y=315)
box63 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box63.place(x=130,y=315)
box64 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box64.place(x=175,y=315)
box71 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box71.place(x=40,y=370)
box72 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box72.place(x=85,y=370)
box73 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box73.place(x=130,y=370)
box74 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box74.place(x=175,y=370)
box81 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box81.place(x=40,y=425)
box82 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box82.place(x=85,y=425)
box83 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box83.place(x=130,y=425)
box84 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box84.place(x=175,y=425)
box91 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box91.place(x=40,y=480)
box92 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box92.place(x=85,y=480)
box93 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box93.place(x=130,y=480)
box94 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box94.place(x=175,y=480)
box101 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box101.place(x=40,y=535)
box102 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box102.place(x=85,y=535)
box103 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box103.place(x=130,y=535)
box104 = Label(GameScreen, bg= "Dark Grey", height=2, width=4, borderwidth=2)
box104.place(x=175,y=535)
#special boxes
box111 = Label(GameScreen, bg= "Dark Grey", height=3, width=6, borderwidth=2)
box111.place(x=40,y=600)
box112 = Label(GameScreen, bg= "Dark Grey", height=3, width=6, borderwidth=2)
box112.place(x=100,y=600)
box113 = Label(GameScreen, bg= "Dark Grey", height=3, width=6, borderwidth=2)
box113.place(x=160,y=600)
box114 = Label(GameScreen, bg= "Dark Grey", height=3, width=6, borderwidth=2)
box114.place(x=220,y=600)
cover = Label(GameScreen, bg= "Black", height=4, width=34, borderwidth=8)
#cover.place(x=28,y=590)




#keypad
keyPad = Label(GameScreen , bg="grey",height=20 , width=40 , borderwidth = 5 , relief="groove")
keyPad.place(x=400 , y=10)
White = Button(GameScreen, bg= "White",height=6 , width=12)
White.place(x=405 ,y= 15)
Blue = Button(GameScreen, bg= "blue",height=6 , width=12)
Blue.place(x=500 ,y= 15)
Purple = Button(GameScreen, bg= "purple",height=6 , width=12)
Purple.place(x=595 ,y= 15)
Green = Button(GameScreen, bg= "pink",height=6 , width=12)
Green.place(x=405 ,y= 115)
Orange = Button(GameScreen, bg= "Orange",height=6 , width=12)
Orange.place(x=500 ,y= 115)
Orange = Button(GameScreen, bg= "Black",height=6 , width=12)
Orange.place(x=595,y= 115)
Enter = Button(GameScreen , bg="Green" , height = 5, width=10,text="Enter")
Enter.place(x=460 , y=230)
Delete= Button(GameScreen, bg= "Red",height=5 , width=10 , text="Delete")
Delete.place(x=560 ,y= 230)














startScreen.pack()
root.mainloop()
