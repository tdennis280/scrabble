from guizero import*
import tkinter as tk
import string

app = App(layout="grid",title="Skrabble",height=680)


boardframe = Box(app,layout="grid",grid=[0,0])
boardframe.bg="turquoise4"

squares = list()
y = 0
x = 0

alphabet = string.ascii_uppercase

for i in range(289):
    if i % 17 == 0 and i!=0:
        y += 1
        x -= 17

    
    if x in [0,16]:
        row = i//17
        squares.append(Text(boardframe,grid=[x,y],text=alphabet[row-1],color="white",width=2,height=1))

    elif y in [0,16]:
        squares.append(Text(boardframe,grid=[x,y],text=x,color="white",width=3))

    else:
        squares.append(PushButton(boardframe,grid=[x,y],text="",width=3,height=1))
        
        squares[-1].tk.configure(borderwidth=1)
        if i in [18,25,32,137,151,256,263,270]:
            squares[-1].tk.configure(bg="red",font="Helvetica 8 bold")
            squares[-1].text="TRIPLE\nWORD\nSCORE"
        elif i in [36,48,54,64,72,80,90,96,144,192,198,208,216,224,234,240,252]:
            squares[-1].tk.configure(bg="pink",font="Helvetica 8 bold")
            squares[-1].text="DOUBLE\nWORD\nSCORE"
        elif i in [40,44,104,108,112,116,172,176,180,184,244,248]:
            squares[-1].tk.configure(bg="dodger blue",font="Helvetica 8 bold")
            squares[-1].text="TRIPLE\nLETTER\nSCORE"
        elif i in [21,29,58,60,69,76,83,122,126,128,132,140,148,156,
                   160,162,166,205,212,219,228,230,259,267]:
            squares[-1].tk.configure(bg="light blue",font="Helvetica 8 bold")
            squares[-1].text="DOUBLE\nLETTER\nSCORE"
        else:
            squares[-1].bg="light sea green"

    if squares[-1].value in ["Z","P"]:
        squares[-1].value=""
    x += 1


    
    


app.display()
