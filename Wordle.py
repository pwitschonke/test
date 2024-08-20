#Libraries
import turtle as t
import random as r
import time

#Functions
def Message(x,y,color,message,font,size,alignment):
    PEN.goto(x,y)
    PEN.color(color)
    PEN.write(message,font=(font,size),align=alignment)

def Draw_Square(x,y,fc):
    DRAW.goto(x,y)
    DRAW.pencolor('white')
    DRAW.pd()
    DRAW.fillcolor(fc)
    DRAW.begin_fill()
    for i in range(4):
        DRAW.fd(50)
        DRAW.rt(90)
    DRAW.end_fill()
    DRAW.pu()

def Write_Words(num):
    for j in range(5):
        Message(GUESSX[j],GUESSY[num],'blue',GUESS.GUESS[j],"times",30,"center")

def Delete():
    if len(GUESS.GUESS)>0:
        Draw_Square(XCORS[len(GUESS.GUESS)-1],YCORS[GUESS.GUESSNUM],'lightgray')
        GUESS.GUESS = GUESS.GUESS[:-1]

def Enter():
    if len(GUESS.GUESS) == 5:
        GUESS.ENTER = True

def A():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'A'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"A","times",30,"center")
def B():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'B'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"B","times",30,"center")
def C():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'C'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"C","times",30,"center")
def D():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'D'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"D","times",30,"center")
def E():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'E'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"E","times",30,"center")
def F():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'F'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"F","times",30,"center")
def G():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'G'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"G","times",30,"center")
def H():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'H'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"H","times",30,"center")
def I():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'I'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"I","times",30,"center")
def J():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'J'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"J","times",30,"center")
def K():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'K'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"K","times",30,"center")
def L():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'L'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"L","times",30,"center")
def M():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'M'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"M","times",30,"center")
def N():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'N'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"N","times",30,"center")
def O():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'O'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"O","times",30,"center")
def P():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'P'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"P","times",30,"center")
def Q():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'Q'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"Q","times",30,"center")
def R():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'R'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"R","times",30,"center")
def S():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'S'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"S","times",30,"center")
def T():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'T'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"T","times",30,"center")
def U():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'U'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"U","times",30,"center")
def V():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'V'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"V","times",30,"center")
def W():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'W'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"W","times",30,"center")
def X():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'X'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"X","times",30,"center")
def Y():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'Y'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"Y","times",30,"center")
def Z():
    if len(GUESS.GUESS) < 5:
        GUESS.GUESS += 'Z'
        Message(GUESSX[len(GUESS.GUESS)-1],GUESSY[GUESS.GUESSNUM],'blue',"Z","times",30,"center")

def Make_Guess():
    while GUESS.ENTER == False:
        WIN.listen()
        WIN.onkey(Delete,'BackSpace')
        WIN.onkey(Enter,'Return')
        WIN.onkey(A,'a')
        WIN.onkey(B,'b')
        WIN.onkey(C,'c')
        WIN.onkey(D,'d')
        WIN.onkey(E,'e')
        WIN.onkey(F,'f')
        WIN.onkey(G,'g')
        WIN.onkey(H,'h')
        WIN.onkey(I,'i')
        WIN.onkey(J,'j')
        WIN.onkey(K,'k')
        WIN.onkey(L,'l')
        WIN.onkey(M,'m')
        WIN.onkey(N,'n')
        WIN.onkey(O,'o')
        WIN.onkey(P,'p')
        WIN.onkey(Q,'q')
        WIN.onkey(R,'r')
        WIN.onkey(S,'s')
        WIN.onkey(T,'t')
        WIN.onkey(U,'u')
        WIN.onkey(V,'v')
        WIN.onkey(W,'w')
        WIN.onkey(X,'x')
        WIN.onkey(Y,'y')
        WIN.onkey(Z,'z')
        WIN.update()
        time.sleep(.1)

def Guess_Analysis():
    word = list(WORD)
    guess = list(GUESS.GUESS)

    #Check For 'Perfect' Letters
    for i in range(len(guess)):
        if guess[i] == word[i]:
            PERFECT_LETTER_INDEXES.append(i)
            word[i] = ' '

    #Check For 'Close' Letters
    for i in range(len(guess)):
        if guess[i] in word:
            CLOSE_LETTER_INDEXES.append(i)
            remove = word.index(guess[i])
            word[remove] = " "

TK_SILENCE_DEPRECATION=1

#Variables
WORD_LIST = ["TAXES","CRANE","HELPS","FORMS","SHAME",
             "SHAPE","APPLE","HEAVE","SHEEN","ARENA",
             "AREAS","BOING","BAKED","BAKES","STUMP",
             "MUSTY","LAYER","ONION","PLEAD","CROSS",
             "BAKED","COOKS","JUMPS","GROSS","FLIES"]
WORD = r.choice(WORD_LIST)
print(WORD)
XCORS = [-135,-80,-25,30,85]
YCORS = [195,140,85,30,-25,-80]
GUESSX = [-110,-55,0,55,110]
GUESSY = [145,90,35,-20,-75,-130]
CORRECT = False
PERFECT_LETTER_INDEXES = []
CLOSE_LETTER_INDEXES = []

#Screen Set Up
WIN = t.Screen()
WIN.setup(450,450)
WIN.bgcolor('black')
WIN.title("Wordle")
WIN.tracer(0)

#Pen Set Up
PEN = t.Turtle()
PEN.ht()
PEN.pu()
#PEN.speed(0)

#Marker Set Up
DRAW = t.Turtle()
DRAW.ht()
DRAW.pu()
#DRAW.speed(0)

#Making A Guessing Turtle
GUESS = t.Turtle()
GUESS.ht()
GUESS.GUESS = ''
GUESS.GUESSNUM = 0
GUESS.ENTER = False

#Draw Blank Board
for rows in range(6):
    for columns in range(5):
        Draw_Square(XCORS[columns],YCORS[rows],'lightgray')

#Update The Board For The User
WIN.update()

#User Taking A Turn
for i in range(6):
    Make_Guess()

    Guess_Analysis()

    #Drawing Green, Yellow, and Grey Squares Based On User's Guess
    for j in range(5):
        if j in PERFECT_LETTER_INDEXES:
            Draw_Square(XCORS[j],YCORS[i],'green')
        elif j in CLOSE_LETTER_INDEXES:
            Draw_Square(XCORS[j],YCORS[i],'yellow')
        else:
            Draw_Square(XCORS[j],YCORS[i],'grey')
    
    #Write The Word Guessed By The User
    Write_Words(i)

    #Update The Screen, Showing The Word And Results
    WIN.update()

    #Check For A Correct Guess
    if GUESS.GUESS == WORD:
        CORRECT = True
        break

    #Reset Variables, Preparing For The Next User Guess
    GUESS.ENTER = False
    GUESS.GUESSNUM += 1
    GUESS.GUESS = ''
    PERFECT_LETTER_INDEXES = []
    CLOSE_LETTER_INDEXES = []

#Check If The User Won Or Lost
if CORRECT == True:
    Message(0,-200,"white","Congratulations","times",25,"center")
else:
    Message(0,-200,'white',f"The Word Was {WORD}",'times',25,'center')

#Update the Screen, Last Time
WIN.update()


t.mainloop()

