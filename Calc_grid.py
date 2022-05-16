from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

window.columnconfigure(0, weight=5)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=5)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=3)

class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Simple Calculator")
        self.lbl1.grid(row=1, column=0, columnspan=6, sticky=EW)

        self.lbl2 = Label(window, text="Input the 1st Number:")
        self.lbl2.grid(row=2, column=1, columnspan=2, sticky=W)
        self.txt2 = Entry(window, bd=3)
        self.txt2.grid(row=2, column=3, columnspan=2, sticky=EW)

        self.lbl3 = Label(window, text="Input the 2nd Number:")
        self.lbl3.grid(row=3, column=1, columnspan=2, sticky=W)
        self.txt3 = Entry(window, bd=3)
        self.txt3.grid(row=3, column=3, columnspan=2, sticky=EW)

        self.btn1 = Button(window, text="Addition")
        self.btn1.grid(row=4, column=1, sticky=EW, padx=3)
        self.btn1.bind('<Button-1>', self.add)
        self.btn2 = Button(window, text="Subtraction")
        self.btn2.grid(row=4, column=2, sticky=EW, padx=3)
        self.btn2.bind('<Button-1>', self.sub)
        self.btn3 = Button(window, text="Multiplication")
        self.btn3.grid(row=4, column=3, sticky=EW, padx=3)
        self.btn3.bind('<Button-1>', self.mul)
        self.btn4 = Button(window, text="Division")
        self.btn4.grid(row=4, column=4, sticky=EW, padx=3)
        self.btn4.bind('<Button-1>', self.div)

        self.lbl4 = Label(window, text="Result:")
        self.lbl4.grid(row=5, column=1, sticky=W)
        self.txt4 = Entry(window, bd=3)
        self.txt4.grid(row=5, column=2, columnspan=2, sticky=EW)

    def add(self, event):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1+num2
        self.txt4.insert(END,str(answer))
        self.txt4.configure(state="readonly")

    def sub(self, event):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1-num2
        self.txt4.insert(END,str(answer))
        self.txt4.configure(state="readonly")

    def mul(self, event):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1*num2
        self.txt4.insert(END,str(answer))
        self.txt4.configure(state="readonly")

    def div(self, event):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1/num2
        self.txt4.insert(END,str(answer))
        self.txt4.configure(state="readonly")


mywin = MyWindow(window)




window.mainloop()