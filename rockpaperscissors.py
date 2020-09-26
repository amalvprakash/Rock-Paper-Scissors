from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x600")
root.iconbitmap(True, "images/icon.ico")
root.title("Rock Paper Scissors")
root.resizable(False,False)

computerScore = 0
playerScore = 0

# main game function
def game(number):
    global playerScore,computerScore

    computerChoiceList = [1,2,3]
    # 1:rock 2:paper 3:scisors
    
    computerChoice = random.choice(computerChoiceList)
    diff = number-computerChoice
    
    while True:
        if diff in [1,-2]:
            playerScore += 1
            scoreLabel = Label(text=playerScore,font="Segoe 16")
            scoreLabel.place(x=220,y=62)
            result.set("Player wins")
            
        elif diff in [-1,2]:
            computerScore += 1
            scoreLabel = Label(text=computerScore,font="Segoe 16")
            scoreLabel.place(x=350,y=62)
            result.set('Computer wins') 
        
        elif diff == 0:
            result.set('Oops...Tie')
    
        imgDict ={1: rock,2: paper,3: scissors}

        imgName = imgDict.get(computerChoice)

        computerLabel = Label(text="Computer Has Choosen,",font="Segoe 16")
        computerLabel.place(x=70,y=170)
        computerImageLabel = Label(image=imgName)
        computerImageLabel.place(x=250,y=200)
        break


welcomeLabel = Label(root,text="Rock Paper Scissors", font="Segoe 24")
welcomeLabel.place(x=150,y=10)


# Score board frame
scoreFrame = Frame(root)
scoreFrame.place(x=100,y=60)

scoreBoard = Label(scoreFrame,text="Player                 |               Computer",font="Segoe 18")
scoreBoard.grid(row=0,column=0)  

# Images
rock = ImageTk.PhotoImage(Image.open("images/rock.png").resize((100,100)))

paper = ImageTk.PhotoImage(Image.open("images/paper.png").resize((100,100)))

scissors = ImageTk.PhotoImage(Image.open("images/scissors.png").resize((100,100)))

iconFrame = Frame(root)
iconFrame.place(x=150,y=350)

rockButton = Button(iconFrame, image=rock,command=lambda: game(1),borderwidth=0)
rockButton.grid(row=5,column=1)

paperButton = Button(iconFrame, image=paper,command=lambda: game(2),borderwidth=0)
paperButton.grid(row=5,column=3)

scissorsButton = Button(iconFrame, image=scissors,command=lambda: game(3),borderwidth=0)
scissorsButton.grid(row=5,column=5)

result = StringVar()
resultLabel = Label(root,textvariable=result,font="Segoe 18") 
resultLabel.place(x=220,y=500)

root.mainloop()
