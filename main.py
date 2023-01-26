from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='#082A46')

data = []


def StartAlgorithm():
    global data
    if not data:
        return

    if (algo_menu.get() == 'Quick sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedscal.get())

    elif algo_menu.get() == 'Buble sort':

        bubble_sort(data, drawData, speedscal.get())
    elif algo_menu.get() == 'Merge sort':
        merge_sort(data, drawData, speedscal.get())
    drawData(data, ['green'for x in range(len(data))])


def drawData(data, colorArray):
    canvas.delete("all")
    canava_height = 450
    canava_width = 870
    x_width = canava_width / (len(data)+1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i/max(data) for i in data]
    for i, height in enumerate(normalised_data):
        x0 = i*x_width+offset+spacing_bet_rect
        y0 = canava_height-height*400

        x1 = (i+1)*x_width
        y1 = canava_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(
            x0+2, y0, anchor=SW, text=str(data[i]), font=("new roman", 15, "italic bold"), fill="orange")

    root.update_idletasks()


def Generate():
    global data
    print('Selected Algorithm :' + selected_algorithm.get())
    # we will take value from our speed scale now

    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())

    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue+1))
    drawData(data, ['#A90042' for x in range(len(data))])


selected_algorithm = StringVar()

# label  ,  buttons  , speed scale

minlabel = Label(root, text="Algorithm : ", font=(
    "new roman", 16, "italic bold"), bg="#05897A", width=10, fg="black", relief=GROOVE, bd=5)

minlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(root, width=10, font=("new roman", 19, "italic bold"),
                         textvariable=selected_algorithm, values=['Buble sort', "Merge sort", "Quick sort"])
algo_menu.place(x=185, y=0)
algo_menu.current(0)   # by default bubble sort

random_generate = Button(root, text="Generate", bg="#2DAE9A", font=("arial", 12, "italic bold"), relief=SUNKEN,
                         activebackground="#05945B", activeforeground="white", bd=5, width=10, command=Generate)

random_generate.place(x=750, y=60)

sizevaluelabel = Label(root, text="size : ", font=("new roman", 12, "italic bold"),
                       bg="#0E6DA5", width=10, fg="black", height=2, relief=GROOVE, bd=5)
sizevaluelabel.place(x=0, y=60)

sizevalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL, font=(
    "arial", 14, "italic bold"), relief=GROOVE, bd=3, width=10)
sizevalue.place(x=135, y=63)
##########################################
minvaluelabel = Label(root, text="Min Value : ", font=("new roman", 12, "italic bold"),
                      bg="#0E6DA5", width=10, fg="black", height=2, relief=GROOVE, bd=5)
minvaluelabel.place(x=250, y=60)

minvalue = Scale(root, from_=0, to=10, resolution=1, orient=HORIZONTAL, font=(
    "arial", 14, "italic bold"), relief=GROOVE, bd=3, width=10)
minvalue.place(x=390, y=63)

##############################################
maxvaluelabel = Label(root, text="Max value : ", font=("new roman", 12, "italic bold"),
                      bg="#0E6DA5", width=10, fg="black", height=2, relief=GROOVE, bd=5)
maxvaluelabel.place(x=500, y=60)

maxvalue = Scale(root, from_=0, to=100, resolution=1, orient=HORIZONTAL, font=(
    "arial", 14, "italic bold"), relief=GROOVE, bd=3, width=10)
maxvalue.place(x=630, y=63)

start = Button(root, text="Start", bg="#c45809", font=("arial", 12, "italic bold"), relief=SUNKEN,
               activebackground="#05945B", activeforeground="white", bd=5, width=10, command=StartAlgorithm)
start.place(x=750, y=0)

speedlabel = Label(root, text="Speed : ", font=("new roman", 12, "italic bold"),
                   bg="#0E6DA5", width=10, fg="black", relief=GROOVE, bd=5)
speedlabel.place(x=400, y=0)

speedscal = Scale(root, from_=0.1, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL, font=(
    "arial", 14, "italic bold"), relief=GROOVE, bd=3, width=10)
speedscal.place(x=530, y=0)

canvas = Canvas(root, width=870, height=450, bg="black")
canvas.place(x=10, y=130)


root.mainloop()
