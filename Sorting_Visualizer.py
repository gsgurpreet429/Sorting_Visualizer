from tkinter import *
from tkinter import ttk
import random
import time


root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1000, 1000)
root.config(bg='#1B1725')


selected_alg = StringVar()
data = []


def swap(data, i, j):
    data[i], data[j] = data[j], data[i]
    return data


def draw_bars(data, colorArray):
    canvas.delete('all')
    c_height = 380
    c_width = 600
    x_width = c_width/(len(data) + 1)
    offset = 10
    spacing = 10
    normalize_data = [i / max(data) for i in data]
    for i, height in enumerate(normalize_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

        root.update_idletasks()


def bubble_sort(data, draw_bars, timer):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data = swap(data, j , j+1)
                draw_bars(data, ['#226CE0' if x == j or x == j+1 else '#A499B3' for x in range(len(data))])
                time.sleep(timer)
    draw_bars(data, ['#226CE0' for x in range(len(data))])


def selection_sort(data, draw_bars, timer):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data = swap(data, i, min_idx)
        draw_bars(data, ['#226CE0' if x == i or x == min_idx else '#A499B3' for x in range(len(data))])
        time.sleep(timer)
    draw_bars(data, ['#226CE0' for x in range(len(data))])


def insertion_sort(data, draw_bars, timer):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            draw_bars(data, ['#226CE0' if x == j or x == j+1 else '#A499B3' for x in range(len(data))])
            j -= 1
            time.sleep(timer)
        data[j + 1] = key
        draw_bars(data, ['grey' if x == j+1 else '#A499B3' for x in range(len(data))])
        time.sleep(timer)
    draw_bars(data, ['#226CE0' for x in range(len(data))])


def start_algorithm():

    if algMenu.get() == 'Bubble Sort':
        bubble_sort(data, draw_bars, speedscale.get())
    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, draw_bars, speedscale.get())
    else:
        selection_sort(data, draw_bars, speedscale.get())


def generate():
    global data
    minvalue = int(minEntry.get())
    maxvalue = int(maxEntry.get())
    size = int(SizeEntry.get())
    data = []
    for i in range(size):
       data.append(random.randrange(minvalue, maxvalue+1))
    draw_bars(data, ['#A499B3' for x in range(len(data))])


UI_frame = Frame(root, width=600, height=300, bg='#1B1725')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=400, bg='#D0BCD5')
canvas.grid(row=0, column=1, padx=10, pady=5)


Label(UI_frame, text="Sorting Algorithms:", bg='#534B62', fg='white').grid(row=0, column=0, padx=5, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort'])
algMenu.grid(row=1, column=0,pady=5)
algMenu.current(0)

speedscale = Scale(UI_frame,from_=0.1, to=2.0, digits=3, resolution=0.2, orient=HORIZONTAL, label="Select Speed[s]", bg='#534B62', fg='white')
speedscale.grid(row=2, column=0, padx=1, pady=1)


SizeEntry = Scale(UI_frame,from_=3, to=25, resolution=1, orient=HORIZONTAL, label ="Size", bg='#534B62', fg='white')
SizeEntry.grid(row=3, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame,from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, label = "Minimum Value", bg='#534B62', fg='white')
minEntry.grid(row=4, column=0, padx=5, pady=5)

maxEntry = Scale(UI_frame,from_=10, to=100, resolution=1, orient = HORIZONTAL, label="Maximum Value", bg='#534B62', fg='white')
maxEntry.grid(row = 5, column = 0, padx = 5, pady = 5)

Button(UI_frame, text='Generate', command=generate, bg = '#D0BCD5').grid(row=6, column=0, padx=5, pady=5)
Button(UI_frame, text='Start', command=start_algorithm, bg='red').grid(row=7, column=0, padx=5, pady=5)

root.mainloop()
