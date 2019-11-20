import random
import turtle
import time


wordList = ['advocate', 'austere', 'benevolent', 'clout', 'complacent', 'deficient', 'eminent', 'facilitate',
            'galvanizing', 'incite', 'novel', 'oust', 'retention', 'prohibit', 'undermine', 'tentative', 'vital',
            'fiscal', 'evoke', 'disparage']
secretWord = random.choice(wordList)
wrongLetter = []
correctLetter = []

print(f"The secret word is {secretWord}")

wrongguesses = 0
MAX_GUESSES = 7
screenWord = ""




myLoc = (212,230)

sWidth = 1400
sHeight = 700
turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(sWidth, sHeight)
screen.bgcolor("yellow")

t = turtle.getturtle()
t.hideturtle()
t.shape("turtle")
t.color("blue")
t.width(6)
t.speed(0)
t.penup()

wrong = []

correct = []

#2019/11/11
topfont = 70
topScreenTurtle = turtle.Turtle()
topScreenTurtle.hideturtle()
topScreenTurtle.shape("turtle")
topScreenTurtle.color('blue')
topScreenTurtle.width(700)
topScreenTurtle.speed(0)
topScreenTurtle.penup()
topScreenTurtle.goto(-520, 310)
topScreenTurtle.setheading(0)


bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.hideturtle()
bottomScreenTurtle.shape("turtle")
bottomScreenTurtle.color('red')
bottomScreenTurtle.width(700)
bottomScreenTurtle.speed(0)
bottomScreenTurtle.penup()
bottomScreenTurtle.goto(-600, -300)
bottomScreenTurtle.setheading(0)


def drawgallows():
    t.ht()
    t.forward(int(sWidth * 0.125))
    t.right(90)

    t.forward(int(sHeight * 0.25))
    t.left(90)

    t.pendown()
    t.forward(int(sWidth * 0.3))
    t.backward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * 0.7))
    t.left(90)
    t.forward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * 0.1))


def drawhead():
    t.right(90)
    t.circle(int(sHeight * 0.06))

def drawbody():
    t.left(90)
    t.penup()
    t.forward(int(sHeight * 0.06) * 2)
    t.pendown()
    t.forward(int(sHeight * 0.11) * 2)

def drawrightarm():
    curPos = t.position()
    curHeading = t.heading()
    curHeading = t.heading()
    t.backward(120)
    t.left(45)
    t.forward(100)
    t.penup()
    t.goto(curPos)
    t.setheading(curHeading)
    t.showturtle()
    t.setheading(-90)
    t.backward(120)


def drawrighthand():

    t.pu()
    t.right(90)
    t.pd()
    t.circle(int(sHeight * 0.01))

def drawleftarm():
    curPos = t.position()
    curHeading = t.heading()
    t.right(45)
    #t.right(-90)
    t.pendown()
    #t.backward(100)
   # t.right(90)
    t.forward(100)
    t.goto(curPos)
    t.setheading(curHeading)
    t.showturtle()
    #t.ht()

def drawlefthand():
    t.right(90)
    t.circle(int(sHeight * 0.01))

def drawrightleg():
    t.pu()
    t.right(-43)
    t.backward(130)
    t.pd()
    t.right(-45)
    t.forward(130)



def drawleftleg():
    t.rt(-180)
    t.backward(100)
    t.left(-200)
    t.forward(130)

def drawrighthfoot():
    t.rt(90)

    t.circle(int(sHeight * 0.01))
    t.hideturtle()

def drawleftfoot():
    t.pu()
    t.right(45)
    t.fd(7)
    t.pd()
    t.circle(int(sHeight * 0.01))
    t.hideturtle()

    wrongguesses = 0

def updateDrawing():
    if wrongguesses == 0:
        drawgallows()

    if wrongguesses == 1:
        drawhead()

    if wrongguesses == 2:
        drawbody()

    if wrongguesses == 3:
        drawrightarm()

    if wrongguesses == 4:
        drawleftarm()

    if wrongguesses == 5:
        drawleftleg()
    if wrongguesses == 6:
        drawleftfoot()

    if wrongguesses == 7:

        drawrightleg()

    if wrongguesses == 8:
        drawrighthfoot()




def drawwrongLetter():
    topScreenTurtle.clear()
    letterString = "Wrong Letters: "
    for l in wrongLetter:
        letterString += l + ", "
        letterString = letterString[ : -2]
    topScreenTurtle.write(letterString, move=False, align="left", font=("Arial", topfont, "normal"))






def drawWords():
    global screenWord

    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomScreenTurtle.color('green')
    bottomScreenTurtle.penup()
    bottomScreenTurtle.goto(-600, -250)
    bottomScreenTurtle.showturtle()
    bottomScreenTurtle.setheading(0)

    screenWord = ""

    bottomScreenTurtle.pendown()
    screenWord = ""
    for letter in secretWord:
        if letter in correctLetter:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "

    bottomScreenTurtle.write(screenWord, align="left", font=("Arial", 70, "normal"))
    bottomScreenTurtle.penup()
    #t.goto(currentLoc)
    #t.setheading(currentHead)
    #t.pendown()
    bottomScreenTurtle.showturtle()

gameOn = True



def printWinOrLose(win):

    if win:
        topScreenTurtle.write("You win!!!", move=False, align="left", font=("Arial", topfont, "normal"))

    else:
        topScreenTurtle.write("You Lose!!!", move=False, align="left", font=("Arial", topfont, "normal"))




def getWordGuess():

    playerWordGuess = screen.textinput("Guess it","Enter your guess of word.")


    if playerWordGuess.lower() == secretWord:

        #print("Win!")
        printWinOrLose(True)
        return False
    else:
        #print("Lose!")
        printWinOrLose(False)
        time.sleep(1)
        gameOn = False
        writeErrorMessage("The secret word is " + secretWord)
        return False


def getGuess():
    badLetter = ""
    for letter in wrong:
        badLetter += letter + ", "
    boxTitle = "Letters Used:" + badLetter
    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word.")
    return theGuess
def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align="left", font=("Arial", topfont, "normal"))
    time.sleep(2)
    topScreenTurtle.clear()


t.showturtle()
gameOn = True

updateDrawing()
wrongguesses = 1
updateDrawing()
wrongguesses = 2
updateDrawing()
wrongguesses = 3
updateDrawing()
wrongguesses = 4
updateDrawing()
wrongguesses = 5
updateDrawing()
wrongguesses = 6
updateDrawing()
wrongguesses = 7
updateDrawing()
wrongguesses = 8
updateDrawing()










#t.showturtle()

#Main game loop
while gameOn:

    drawWords()
    guess = getGuess()
    guess = str(guess)
    if guess == "$$":
        gameOn = getWordGuess()
    elif len(guess) != 1:
        writeErrorMessage("I need a single error, guess again!")
        drawwrongLetter()
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        drawwrongLetter()
        writeErrorMessage("I need a letter, Guess again!")
    else:
        if guess.lower() in secretWord.lower():
            correctLetter.append(guess.lower())
            print(guess.lower() + " is in " + secretWord)
            drawWords()
        else:
            #if the letter is bad
            wrongLetter.append(guess.lower())
            wrongguesses += 1
            drawwrongLetter()
            updateDrawing()

        if(wrongguesses >= MAX_GUESSES):
            writeErrorMessage("You are out of guesses. Game Over.")
            gameOn = False
            writeErrorMessage("The secret word is " + secretWord)

        if "_" not in screenWord:
            writeErrorMessage("Excellent!!! You Win")










#guess = getGuess()
#now we play the game
# drawgallows()
# drawhead()
# drawbody()
# drawrightarm()
# drawrighthand()
# drawleftarm()
# drawlefthand()
# drawrightleg()
# drawrighthfoot()
# drawleftleg()
# drawleftfoot()

turtle.mainloop()





