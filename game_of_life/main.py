import tkinter as tk
import numpy as np
from tkinter import filedialog as fd
win = tk.Tk()

WIDTH = 500
HEIGHT = 500
vs = 10
absvs = vs
cells = np.zeros((WIDTH//vs, HEIGHT//vs), dtype=int)
cells_def = np.zeros((WIDTH//vs, HEIGHT//vs), dtype=int)
cells_new = np.zeros((WIDTH//vs, HEIGHT//vs), dtype=int)

def get_neighbours(x, y):
    total = 0

    if x > 0:
        total += cells[x - 1, y]

    if x > 0 and y > 0:
        total += cells[x - 1, y - 1]

    if y > 0:
        total += cells[x, y - 1]

    if x > 0 and y < (HEIGHT // absvs - 1):
        total += cells[x - 1, y + 1]

    if x < (WIDTH // absvs - 1):
        total += cells[x + 1, y]

    if x < (WIDTH // absvs - 1) and y < (HEIGHT // absvs - 1):
        total += cells[x + 1, y + 1]

    if y < (HEIGHT // absvs - 1):
        total += cells[x, y + 1]

    #chybný kód
    #if x > 0 and y < (HEIGHT // absvs - 1):
    #    total += cells[x - 1, y + 1]
    #chybný kód

    if x < (WIDTH // absvs - 1) and y > 0:
        total += cells[x + 1, y - 1]
    return total

def openfile():
    global cells, cells_new
    load = []
    filename = fd.askopenfilename()
    f = open(filename,"r")
    cells_new = cells_def.copy()
    for i in f:
        for j in i.split():
            load.append(j)
    for i in range(len(load)):
        for j in range(len(load[i])):
            print(load[i][j])
            if load[i][j] == "1":
                cells_new[i, j] = 1
            else:
                cells_new[i, j] = 0
    cells = cells_new.copy()
    canvas.delete("all")
    create_stage()
    redraw_cell()

def recalculate():
    global cells, cells_new
    for y in range(HEIGHT//absvs):
        for x in range(WIDTH//absvs):
            temp = get_neighbours(x, y)
            if (temp == 2 and cells[x, y] == 1) or (temp == 3 and cells[x, y] == 1):
                cells_new[x, y] = 1
            elif temp == 3 and cells[x, y] == 0:
                cells_new[x, y] = 1
            elif temp < 2 or temp > 3:
                cells_new[x, y] = 0
    cells = cells_new.copy()
    canvas.delete("all")
    create_stage()
    redraw_cell()

def slider_changer(e):
    global vs
    canvas.delete("all")
    vs = w.get()
    create_stage()
    redraw_cell()

def create_cell(e):
    global cells
    tx = e.x // vs
    ty = e.y // vs
    x = tx * vs
    y = ty * vs
    canvas.create_rectangle(x, y, x + vs, y + vs, fill="gray")
    cells[tx, ty] = 1
    print(get_neighbours(tx, ty))

def redraw_cell():
    for x in range(WIDTH//vs):
        for y in range(HEIGHT//vs):
            if cells[x, y] == 1:
                canvas.create_rectangle(x * vs, y * vs, x * vs + vs, y * vs + vs, fill="gray")

def create_stage():
    global cells_new, cells_def
    for x in range(WIDTH//vs):
        canvas.create_line(x*vs, 0, x*vs, HEIGHT)
    for y in range(HEIGHT//vs):
        canvas.create_line(0, y*vs, WIDTH, y*vs)
    cells_new = cells_def

canvas = tk.Canvas(width = WIDTH, height = HEIGHT, bg = "white")
canvas.pack()

w = tk.Scale(win, from_=10, to=50, orient="horizontal", command = slider_changer, length = 500)
w.pack()
w2 = tk.Button(win, text = "Press me to progress a generation!", command = recalculate)
w2.pack()
w3 = tk.Button(win, text = "Load an already created game file:", command = openfile)
w3.pack()

create_stage()
canvas.bind("<Button-1>", create_cell)
win.mainloop()

#UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM,UMIERAM
