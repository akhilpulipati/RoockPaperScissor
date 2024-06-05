#written by Akhil Pulipati
#created on 30 November 2022
#This program is about Rock Paper Scissors game.
#In this program we are asking the user to enter his game name and let him play rock paper scissor against the computer.
from tkinter import * # here we are importing all the functions from tkinter module
import random # here we are importing random module
from tkinter import messagebox,ttk
        
class Game:
    def __init__(self):
        self.GN = Tk()# here we are declaring an object to tkinter
        self.GN.title('Rock Paper Scissors Game')# this is the title bar and its title
        self.GN.geometry('400x150')# here we are mentioning the geometry of the window
        self.GN.eval('tk::PlaceWindow . center')
        self.GameNameLabel = Label(self.GN, text='What do you want to be called in this game',font=("Verdana", 10, "bold"))# here we are using the label to ask user ti enter his game name 
        self.GameNameLabel.pack()# here we are positioning the label
        self.GameNameLabel.config(bg="#C0C0C0")
        self.GameNameEntry = Entry(self.GN)#this the entry for user to enter his game name
        self.GameNameEntry.pack()# here we are positioning the entry
        self.GameNameSubmit = Button(self.GN, text='SUBMIT' ,font=("Verdana", 8, "bold"),command=self.submit)#here we are creating the submit button for game name
        self.GameNameSubmit.pack()# here we are positioning the submit button
        self.GN.config(bg="#C0C0C0")
        
    def submit(self):
        global GameName
        GameName = self.GameNameEntry.get()#here we are recievin the gamename value
        if GameName=="":# if user doesnt enter name and press submit this message will popup
            messagebox.showerror("Error", "You should enter the game name to continue..")
            self.GN.mainloop()# again we are calling the game name window 
        else:    
            self.GN.destroy()#here we are destroying the game name window
            self.display(GameName)# here we are calling the display
        
    def display(self, GameName):
        RPS=Tk()# here we are declaring an object to tkinter
        RPS.title("Rock, Paper, Scissor Game")
        width = 550
        height = 450
        screen_width = RPS.winfo_screenwidth()
        screen_height = RPS.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        RPS.geometry("%dx%d+%d+%d" % (width, height, x, y))
        RPS.resizable(0, 0)
        RPS.config(bg="#008080")#here we are mentioning the background color for the window
        global Replay


        BlankImage=PhotoImage(file="F:\Python\systemblank.png").subsample(3, 3)#here we are assigning a picture to blankimage 
        PlayerRockImage=PhotoImage(file="F:\Python\player_rock.png").subsample(3, 3)#here we are assigning a picture to Player Rock image
        PlayerPaperImage=PhotoImage(file="F:\Python\player_paper.png").subsample(3, 3)#here we are assigning a picture to Player paper image
        PlayerScissorImage=PhotoImage(file="F:\Python\player_scissor.png").subsample(3, 3)#here we are assigning a picture to player scissor image
        ComputerRockImage=PhotoImage(file="F:\Python\com_rock.png").subsample(3, 3)#here we are assigning a picture to computer rock image
        ComputerPaperImage=PhotoImage(file="F:\Python\com_paper.png").subsample(3, 3)#here we are assigning a picture to computer paper image
        ComputerScissorImage=PhotoImage(file="F:\Python\com_scissor.png").subsample(3, 3)#here we are assigning a picture to computer scissor image

        PlayerImage = Label(RPS,image=BlankImage)# here we are creating a label for player image
        ComputerImage = Label(RPS,image=BlankImage)# here we are creating a label for computer image
        PlayerLabel = Label(RPS,text=str(GameName),font=("courier", 18, "bold "))#here we are describing the player label
        PlayerLabel.grid(row=1, column=1)# here we are postioning the player label
        PlayerLabel.config(bg="#008080")
        ComputerLabel = Label(RPS,text="COMPUTER",font=("courier", 18, "bold "))#here we are describing the computer label
        ComputerLabel.grid(row=1, column=3)# here we are postioning the computer label
        ComputerLabel.config(bg="#008080")
        GameStatus=Label(RPS, text="SELECT AN OPTION BELOW", font=("Verdana", 10, "bold"))#here we are describing the Status of the gamr
        GameStatus.config(bg="#008080")
        PlayerImage.grid(row=2,column=1, padx=50,pady=20)# here we are postioning the player image
        ComputerImage.grid(row=2,column=3, pady=20)# here we are postioning the computer image
        GameStatus.grid(row=3, column=2,pady=20)# here we are postioning the game status

       

        def Rock():
            global PlayerChoice
            PlayerChoice = 1
            PlayerImage.configure(image=PlayerRockImage)#here we are configuring the player image
            MatchProcess()#here we are calling the Match process
        
        def Paper():
            global PlayerChoice
            PlayerChoice = 2
            PlayerImage.configure(image=PlayerPaperImage)#here we are configuring the player image
            MatchProcess()#here we are calling the Match process
            
        def Scissors():
            global PlayerChoice
            PlayerChoice = 3
            PlayerImage.configure(image=PlayerScissorImage)#here we are configuring the player image
            MatchProcess()#here we are calling the Match process

        def MatchProcess():
            ComputerChoice = random.randint(1,3)#here we are randomnly choosing a number  between 1 2 and 3
            if ComputerChoice == 1:#if choice is 1 this if will activate
                ComputerImage.configure(image=ComputerRockImage)#here we are configuring the computer image
                ComputerRock()#here we are calling the computer rock

            elif ComputerChoice == 2:#if choice is 2 this if will activate
                ComputerImage.configure(image=ComputerPaperImage)#here we are configuring the computer image
                ComputerPaper()#here we are calling the computer paper
                
            elif ComputerChoice == 3:#if choice is 3 this if will activate
                ComputerImage.configure(image=ComputerScissorImage)#here we are configuring the computer image
                CompututerScissor()#here we are calling the computer scissor

        def ComputerRock():
            if PlayerChoice == 1:#if player choice is 1 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()#here we are declaring a object to the tkinter
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text="GAME \n TIED ", font=("courier", 12, "bold"))#here we are displaying the game status 
                GameStatus.pack()#here we are positioning the game status
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            elif PlayerChoice == 2:#if player choice is 2 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text=str(GameName)+" \nWINS ", font=("courier", 12, "bold"))#here we are displaying the game status
                GameStatus.pack()#here we are positioning the game status
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            elif PlayerChoice == 3:#if player choice is 3 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text="COMPUTER \nWINS ", font=("courier", 12, "bold"))#here we are displaying the game status
                GameStatus.pack()
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window
                
        def ComputerPaper():

            if PlayerChoice == 1:#if player choice is 1 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text="COMPUTER \nWINS ", font=("courier", 12, "bold"))#here we are displaying the game status
                GameStatus.pack()
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            elif PlayerChoice == 2:#if player choice is 2 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()#here we are declaring a object to the tkinter
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text="GAME \n TIED ", font=("courier", 12, "bold"))#here we are displaying the game status 
                GameStatus.pack()#here we are positioning the game status
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            elif PlayerChoice == 3:#if player choice is 3 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text=str(GameName)+" \nWINS ", font=("courier", 12, "bold"))#here we are displaying the game status
                GameStatus.pack()#here we are positioning the game status
                GameStatus.config(bg="#C0C0C0")
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window
            
        def CompututerScissor():
            
            if PlayerChoice == 1:#if player choice is 1 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text=str(GameName)+" \nWINS ", font=("courier", 12, "bold"))#here we are displaying the game status
                GameStatus.pack()#here we are positioning the game status
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            elif PlayerChoice == 2:#if player choice is 2 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text="COMPUTER \nWINS ", font=("courier", 12, "bold"))#here we are displaying the game status
                GameStatus.pack()
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                GameStatus.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            elif PlayerChoice == 3:#if player choice is 3 this if will activate
                RPS.after(1000,lambda:RPS.destroy())
                Replay = Tk()#here we are declaring a object to the tkinter
                Replay.title('Rock Paper Scissors Game')
                Replay.geometry('250x150')
                Replay.eval('tk::PlaceWindow . center')
                GameStatus = Label(Replay, text="GAME \n TIED ", font=("courier", 12, "bold"))#here we are displaying the game status 
                GameStatus.pack()#here we are positioning the game status
                GameStatus.config(bg="#C0C0C0")
                GameDecision=Label(Replay, text="\nDo you want another round?", font=("courier", 10, "bold"))#here we are displaying the game status 
                GameDecision.pack()
                GameDecision.config(bg="#C0C0C0")
                ReplayButton=Button(Replay,text="REPLAY",font =('calibri', 10, 'bold', 'underline'),foreground = 'green',command=lambda: [Replay.destroy(), self.display(GameName)])#here we are creating the replay button
                ReplayButton.pack(side=LEFT)#here we are positioning the replay button
                Exit=Button(Replay,text="EXIT",font =('calibri', 10, 'bold', 'underline'),foreground = 'red',command=ExitApp)#here we are creating the exit button
                Exit.pack(side=RIGHT)#here we are positioning the exit button
                Replay.config(bg="#C0C0C0")
                Replay.mainloop()#here we are starting the replay window

            
        def ExitApp():
            exit()#here we are exiting from the program

        R =  IntVar()
        
        RockButton = ttk.Radiobutton(RPS,variable=R, value =1, image=PlayerRockImage, command=Rock)#here we are creating the radio Rock button
        PaperButton = ttk.Radiobutton(RPS, variable=R, value =2,image=PlayerPaperImage, command=Paper)#here we are creating the radio Paper button
        ScissorButton = ttk.Radiobutton(RPS,variable=R, value =3, image=PlayerScissorImage, command=Scissors)#here we are creating the radio  Scissor button
        RockButton.grid(row=4,column=1, pady=30)#here we are positioning the rock button
        PaperButton.grid(row=4,column=2, pady=30)#here we are positioning the paper button
        ScissorButton.grid(row=4,column=3, padx=40,pady=40)#here we are positioning the scissor button


def main():
    G=Game()#here we are creating an object to game class
    G.GN.mainloop()#here we are starting the gamename window

        
if __name__ == "__main__":     
    main()#here we are calling the main function
