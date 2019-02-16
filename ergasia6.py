#python 3.7

import tkinter, random, os, tkinter.messagebox, tkinter.simpledialog

window = tkinter.Tk()
window.title("Askisi6-Narkalieutis")

#h sunarthsh createMenu dhmiourgei to menou tou neou parathyrou (p.x to koumpi restart)
def createMenu():
    menubar = tkinter.Menu(window)
    menusize = tkinter.Menu(window, tearoff=0)
    menubar.add_cascade(label="Restart", menu=menusize)
    menusize.add_command(label="Restart", command=restartGame)
    menusize.add_separator()
    window.config(menu=menubar)

#h synarthsh preprepareGame zhtaei apo ton xrhsth arithmo sthlwn, seirwn kai narkwn
#kai apothikevei tis times se metavlites, epeita kalei tis sunarthseis createMenu kai prepareGame
#wste na dhmiourgithei to menu tou parathirou kai to meros sto opoio tha vrisketai o pinakas tou narkalieuth
def preprepareGame():
    global customsizes, rows, cols, mines
    rows = tkinter.simpledialog.askinteger(" ", "Αριθμος σειρων")
    cols = tkinter.simpledialog.askinteger(" ", "Αριθμως στηλων")
    mines = tkinter.simpledialog.askinteger(" ", "Αριθμος ναρκων")
    while mines > rows*cols:
        mines = tkinter.simpledialog.askinteger("Custom size", "Maximum mines for this dimension is: " + str(rows*cols) + "\nEnter amount of mines")
    prepareGame()

#h sunarthsh prepare game dhmiourgei th lista buttons kai me vash tis grammes kai tis sthles prosthetei sth lista buttons
#osa stoixeia osa einai kai oi times rows, cols
def prepareGame():
    createMenu()
    global rows, cols, mines, buttons, field
    buttons = []
    for x in range(0, rows):
        buttons.append([])
        for y in range(0, cols):
            b = tkinter.Button(window, text=" ", width=2)
            b.grid(row=x+1, column=y)
            buttons[x].append(b)
    field = []
    for x in range(0, rows):
        field.append([])
        for y in range(0, cols):
            #add button and init value for game
            field[x].append(0)
    for _ in range(0, mines): #vazoume tis narkes ston pinaka tou narkalieuth me thn xrhsh ths randint apo thn vivliothiki random
        x = random.randint(0, rows-1)
        y = random.randint(0, cols-1)
        while field[x][y] == -1: # parakatw elegxoume to kathe stoixeio wste na mhn bei mia narki panw se alli
            x = random.randint(0, rows-1)
            y = random.randint(0, cols-1)
        field[x][y] = -1
        if x != 0:
            if y != 0:
                if field[x-1][y-1] != -1:
                    field[x-1][y-1] = int(field[x-1][y-1]) + 1
            if field[x-1][y] != -1:
                field[x-1][y] = int(field[x-1][y]) + 1
            if y != cols-1:
                if field[x-1][y+1] != -1:
                    field[x-1][y+1] = int(field[x-1][y+1]) + 1
        if y != 0:
            if field[x][y-1] != -1:
                field[x][y-1] = int(field[x][y-1]) + 1
        if y != cols-1:
            if field[x][y+1] != -1:
                field[x][y+1] = int(field[x][y+1]) + 1
        if x != rows-1:
            if y != 0:
                if field[x+1][y-1] != -1:
                    field[x+1][y-1] = int(field[x+1][y-1]) + 1
            if field[x+1][y] != -1:
                field[x+1][y] = int(field[x+1][y]) + 1
            if y != cols-1:
                if field[x+1][y+1] != -1:
                    field[x+1][y+1] = int(field[x+1][y+1]) + 1
    for _x in range(0, rows):
        for _y in range(cols):
            if field[_x][_y] == -1:
                buttons[_x][_y]["text"] = "*"

#h sunarthsh restart diagrafei oti exei ginei ston pinaka panw gia apofygh memory leak kai kalei thn synarthsh
#preprepareGame wste na ksekinisei apo thn arxh to programma kai na zhthsei pali grammes, sthles ktl.
def restartGame():
    for x in window.winfo_children():
        if type(x) != tkinter.Menu:
            x.destroy()
    preprepareGame()

preprepareGame()

window.mainloop()
