# Importing algorithms
import random
import time
from tkinter import *
from tkinter import ttk

DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
GREEN = '#0D7377'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
DARK_GREEN = '#38A3A5'
LIGHT_GREEN = '#D4ECDD'
LIGHT_YELLOW = '#FFE194'
ASHY_BLACK = '#2B2B2B'
LIGHTER_GREEN = '#C4FB6D'
PURPLE = '#C490E4'
LIGHT_PINK = '#F6C6EA'
PEACH = '#FFBCBC'
PINKER = '#FF3D68'
PEACHER = '#FF8882'
DARK_PURPLE = '#72147E'
LIGHT_CYAN = '#E4FBFF'
PURPLER = '#583D72'
LAVENDER = '#B088F9'
ORANGE = '#FFBF86'
LIGHT_YELLOW = '#F9F871'
CYANER = '#75CFB8'
YELLOWER = '#F9F871'
BACK_YELLOW = '#FFB319'
PEACH_PINK = '#FF6B6B'


def selection_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        minimum = i
        for k in range(i + 1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, [PEACH_PINK if x == minimum or x == i else CYANER for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [CYANER for x in range(len(data))])


# Main window
window = Tk()
window.title("Insertion Sort Visualizer")
window.maxsize(1000, 700)
window.config(bg=BACK_YELLOW)

algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Insertion Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 3
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, 20):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [CYANER for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.8
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Insertion Sort':
        selection_sort(data, drawData, timeTick)


### User interface ###
UI_frame = Frame(window, width=900, height=300, bg=ORANGE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=LIGHT_YELLOW)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=LIGHT_YELLOW)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=ORANGE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", fg=WHITE, command=sort, bg=ASHY_BLACK)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", fg=WHITE, command=generate, bg=ASHY_BLACK)
b3.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()
