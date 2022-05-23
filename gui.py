import turtle
from tkinter import *
from tkinter import Button
import tkinter.font
from tkinter.filedialog import askopenfilename

import parserFile

Code = ""
Error = "No Exception Found"

# main ayarlama
main_screen = Tk()
main_screen.title("Automata Proje ödevi G17")
main_screen.geometry("1000x750")
main_screen.resizable(0, 0)
main_screen.config(bg="#00373d")

# başlık ayarları
title = Label(main_screen, text="Drawing Robot", font=20, background="#00373d", foreground="white")
font = tkinter.font.Font(family="Robot Roc", size=20)
title.configure(font=font)

code_screen = Text(main_screen)
code_screen.insert(END, Code)
code_screen.configure(state="disabled")

exception_screen = Text(main_screen, width=8)
exception_screen.insert(END, Error)
exception_screen.configure(state="disabled")

canvas = Canvas(main_screen, background="white")
screen = turtle.TurtleScreen(canvas)
my_turtle = turtle.RawTurtle(screen, shape="turtle")


def turtle_forward(x):
    my_turtle.forward(x)


def turtle_rotate(x):
    my_turtle.right(x)



def turtle_color(x):
    if x == 'K':
        my_turtle.pencolor("#610000")
    elif x == 'M':
        my_turtle.pencolor("0000061")
    elif x == 'Y':
        my_turtle.pencolor("006100")
    elif x == 'S':
        my_turtle.pencolor("000000")
    else:
        exception_screen.configure(state="normal")
        exception_screen.delete('1.0', END)
        global Error
        Error = "Undefined Color Error"
        exception_screen.insert(END,Error)
        exception_screen.configure(state="disabled")


def turtle_pen(x):
    if x > 3:
        exception_screen.configure(state="normal")
        exception_screen.delete('1.0', END)
        global Error
        Error = "Undefined Pen size Error"
        exception_screen.insert(END,Error)
        exception_screen.configure(state="disabled")
    else:
        my_turtle.pensize(x)

def load_button_on_click_listener():

    filetypes = (('text files', '*.txt'),)
    filename = askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)


    global Code
    code_screen.configure(state="normal")
    Code = open(filename).read()
    Code = Code.replace('\n', " ")
    code_screen.insert(END, Code)
    code_screen.configure(state="disabled")


def clear_button_on_click_listener():
    code_screen.configure(state="normal")
    code_screen.delete('1.0', END)
    global Code
    Code = ""
    code_screen.configure(state="disabled")



def run_button_on_click_listener():

    list = parserFile.parseIt(Code)
    print(list)
    print(len(list))
    try:
        draw(list)
    except:
        exception_screen.configure(state="normal")
        exception_screen.delete('1.0', END)
        global Error
        Error = "Unexpected Syntax Error Please Check Terminal"
        exception_screen.insert(END, Error)
        exception_screen.configure(state="disabled")



#['L', 36, '[', 'L', 4, '[', 'F', 50, 'R', 90, ']', 'R', 10, ']', 'PEN', 2, 'COLOR', 'K']

def draw(list,index_count = -1):


    while index_count < len(list):

        index_count += 1
        print(list[index_count])
        if list[index_count] == 'L':
            count = list[index_count +1]
            print(count)
            index_count += 2

            for i in range(count):
                index_2 = draw(list, index_count)
            index_count = index_2

        elif list[index_count] == 'F':
            index_count += 1
            turtle_forward(list[index_count])
        elif list[index_count] == 'R':
            index_count += 1
            turtle_rotate(list[index_count])
        elif list[index_count] == 'PEN':
            index_count += 1
            turtle_pen(list[index_count])
        elif list[index_count] == 'COLOR':
            index_count += 1
            turtle_color(list[index_count])
        elif list[index_count] == '[':
            continue
        elif list[index_count] == ']':
            break

        else:
            exception_screen.configure(state="normal")
            exception_screen.delete('1.0', END)
            global Error
            Error = "Undefined Instruction Error"
            exception_screen.insert(END,Error)
            exception_screen.configure(state="disabled")

    return index_count






load_button = Button(main_screen, text="Yükle", background="#45494a", foreground="white",
                     command=load_button_on_click_listener)
clear_button = Button(main_screen, text="Temizle", background="#45494a", foreground="white",
                      command=clear_button_on_click_listener)
run_button = Button(main_screen, text="Çiz", background="#45494a", foreground="white",
                    command=run_button_on_click_listener)

title.place(x=40, y=40)
code_screen.place(x=30, y=210, width=460, height=25)
load_button.place(x=40, y=300, width=100, height=25)
clear_button.place(x=180, y=300, width=100, height=25)
exception_screen.place(x=30, y=440, width=460, height=50)
canvas.place(x=550, y=130, width=400, height=400)
run_button.place(x=840, y=660, width=100, height=25)




main_screen.mainloop()
