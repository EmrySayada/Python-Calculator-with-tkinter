from tkinter import *
from time import sleep
from sympy import solvers
import speech_recognition as sr

root = Tk()
root.geometry("500x324")   
root.resizable(0, 0)  
root.title("Calculator")

rec = sr.Recognizer()

input_text = StringVar()


calculator_frame = Frame(root)
calculator_frame.pack(side = LEFT)


input_frame = Frame(calculator_frame, width=312,height=50)
 
input_frame.pack(side=TOP)
 

 
input_field = Entry(input_frame, font=('arial', 18, 'bold'),textvariable=input_text, width=22, bg="white")
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=11, ipadx=11)

input_field.config(state=DISABLED)

recent_problems = Frame(root)
recent_problems.pack(side=RIGHT, expand=True)


def recent_problem_click():
    global expression 
    input_text.set(expression)


recent_problems_text = Text(recent_problems, height=25, font=('arial', 16))
recent_problems_text.pack(side=RIGHT, expand=True)
recent_problems_text.config(state=DISABLED)


btns_frame = Frame(calculator_frame, width=312, height=272.5, bg="grey")
 
btns_frame.pack(side=LEFT)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)



def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

 
def bt_equal():
    global expression
    result = str(eval(expression))
    recent_problems_text.config(state=NORMAL)
    recent_problems_text.insert(END, f"{str(expression)} = {result}\n")
    recent_problems_text.config(state=DISABLED)
    input_text.set(result)
    expression = ""

def equation_mode():
    global expression
    expression = expression + str("x")
    input_text.set("equation mode enabled")
    sleep(2)
    input_text.set(expression)
    
 
expression = ""
def rec_func():
        try:
            with sr.Microphone() as source:
                root.title("Listening")
                voice = rec.listen(source)
                problem = rec.recognize_google(voice)
                problem_list = problem.split()
                input_text.set(problem)
                if 'to the power of' in problem or '^' in problem:
                    result = int(problem_list[0])**int(problem_list[-1])
                # elif 'x' in problem:
                #     equation_mode()
                else:
                    result = str(eval(problem))
                input_text.set(result)
                recent_problems_text.config(state=NORMAL)
                recent_problems_text.insert(END, f"{str(problem)} = {result}\n")
                recent_problems_text.config(state=DISABLED)
                root.title("Calculator")
                return True
        except:
            return False




rec_button = Button(recent_problems, text="Record", font=('arial', 16), fg = "white", activebackground='red',bg = "#0000FF", width=15, command=rec_func)
rec_button.place(x=0, y=285)


bclear = Button(btns_frame, text = "C", fg = "white", bg = "#0000FF", width = 32, bd = 0,height = 3, command=bt_clear)
bclear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
bdivid = Button(btns_frame, text = "/", fg = "white", bg = "#0000FF", width = 10, bd = 0,height = 3, command=lambda: btn_click("/"))
bdivid.grid(row = 0, column = 3, padx = 1, pady = 1)
 

 
b7 = Button(btns_frame, text = "7", fg = "black",width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("7"))
b7.grid(row = 1, column = 0, padx = 1, pady = 1)
 
b8 = Button(btns_frame, text = "8", fg = "black",width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("8"))
b8.grid(row = 1, column = 1, padx = 1, pady = 1)
 
b9 = Button(btns_frame, text = "9", fg = "black",width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("9"))
b9.grid(row = 1, column = 2, padx = 1, pady = 1)
 
bmul = Button(btns_frame, text = "*", fg = "white",bg = "#0000FF", width = 10, bd = 0,height = 3, command= lambda: btn_click("*"))
bmul.grid(row = 1, column = 3, padx = 1, pady = 1)
 

 
b4 = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("4"))
b4.grid(row = 2, column = 0, padx = 1, pady = 1)
 
b5 = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("5"))
b5.grid(row = 2, column = 1, padx = 1, pady = 1)
 
b6 = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("6"))
b6.grid(row = 2, column = 2, padx = 1, pady = 1)
 
bminus = Button(btns_frame, text = "-", fg = "white",bg = "#0000FF", bd = 0,width = 10, height = 3, command= lambda: btn_click("-"))
bminus.grid(row = 2, column = 3, padx = 1, pady = 1)
 

 
b1 = Button(btns_frame, text = "1", fg = "black",width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("1"))
b1.grid(row = 3, column = 0, padx = 1, pady = 1)
 
b2 = Button(btns_frame, text = "2", fg = "black",width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("2"))
b2.grid(row = 3, column = 1, padx = 1, pady = 1)
 
b3 = Button(btns_frame, text = "3", fg = "black",width = 10, height = 3, bd = 0,bg = "white", command= lambda: btn_click("3"))
b3.grid(row = 3, column = 2, padx = 1, pady = 1)
 
bplus = Button(btns_frame, text = "+", fg = "white", bg = "#0000FF",width = 10, bd = 0,height = 3, command= lambda: btn_click("+"))
bplus.grid(row = 3, column = 3, padx = 1, pady = 1)
 

 
b0 = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0,bg = "white", command= lambda: btn_click("0"))
b0.grid(row = 4, column = 0, padx = 1, pady = 1, columnspan=2)

# bx = Button(btns_frame, text="x", fg="black", width = 10, height = 3, bd = 0,bg = "white")
# bx.grid(row = 4, column = 1, padx = 1, pady = 1)
 
bdot = Button(btns_frame, text = ".", fg = "white", bg ="#0000FF",width = 10,bd = 0, height = 3, command= lambda: btn_click("."))
bdot.grid(row = 4, column = 2, padx = 1, pady = 1)
 
bequal = Button(btns_frame, text = "=", fg = "white", bg = "#0000FF",width = 10,bd = 0, height = 3, command=bt_equal)
bequal.grid(row = 4, column = 3, padx = 1, pady = 1)
 
root.mainloop()