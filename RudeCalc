import tkinter as tk
from sympy import sympify
import re

class Calculator():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("400x775")
        self.root.title("Emotional Calculator")

        self.calcTxt = ""
        self.label = tk.Label(self.root, text=self.calcTxt, font=('Arial', 12))
        self.label.pack()

        self.txt = ""
        self.label = tk.Label(self.root, text=self.txt, font=('Arial', 18))
        self.label.pack()

        self.frameUpper = tk.Frame(self.root)
        self.frameUpper.pack(expand=True, fill="both")

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        self.frameUpper.columnconfigure(0, weight=1)
        self.frameUpper.columnconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.btn1 = tk.Button(self.frame,text="1", bg="light grey", height=3, font=('Arial',24), command=self.pressOne)
        self.btn1.grid(row=4,column=0,sticky="news")

        self.btn2 = tk.Button(self.frame,text="2", bg="light grey", height=3, font=('Arial',24), command=self.pressTwo)
        self.btn2.grid(row=4,column=1,sticky="news")

        self.btn3 = tk.Button(self.frame,text="3", bg="light grey", height=3, font=('Arial',24), command=self.pressThree)
        self.btn3.grid(row=4,column=2,sticky="news")

        self.btn4 = tk.Button(self.frame,text="4", bg="light grey", height=3, font=('Arial',24), command=self.pressFour)
        self.btn4.grid(row=3,column=0,sticky="news")

        self.btn5 = tk.Button(self.frame,text="5", bg="light grey", height=3, font=('Arial',24), command=self.pressFive)
        self.btn5.grid(row=3,column=1,sticky="news")

        self.btn6 = tk.Button(self.frame,text="6", bg="light grey", height=3, font=('Arial',24), command=self.pressSix)
        self.btn6.grid(row=3,column=2,sticky="news")

        self.btn7 = tk.Button(self.frame,text="7", bg="light grey", height=3, font=('Arial',24), command=self.pressSeven)
        self.btn7.grid(row=2,column=0,sticky="news")

        self.btn8 = tk.Button(self.frame,text="8", bg="light grey", height=3, font=('Arial',24), command=self.pressEight)
        self.btn8.grid(row=2,column=1,sticky="news")

        self.btn9 = tk.Button(self.frame,text="9", bg="light grey", height=3, font=('Arial',24), command=self.pressNine)
        self.btn9.grid(row=2,column=2,sticky="news")

        self.btn0 = tk.Button(self.frame,text="0", bg="light grey", height=3, font=('Arial',24), command=self.pressZero)
        self.btn0.grid(row=5,column=1,sticky="news")

        self.btnNegative = tk.Button(self.frame,text="(-)", bg="grey", height=3, font=('Arial',24), command=self.pressNegative)
        self.btnNegative.grid(row=5,column=0,sticky="news")

        self.btnPeriod = tk.Button(self.frame,text=".", bg="grey", height=3, font=('Arial',24), command=self.pressPeriod)
        self.btnPeriod.grid(row=5,column=2,sticky="news")

        self.btnDivide = tk.Button(self.frame,text="÷", bg="grey", height=3, font=('Arial',24), command=self.pressDivide)
        self.btnDivide.grid(row=1,column=3,sticky="news")

        self.btnMultiply = tk.Button(self.frame,text="×", bg="grey", height=3, font=('Arial',24), command=self.pressMultiply)
        self.btnMultiply.grid(row=2,column=3,sticky="news")

        self.btnMinus = tk.Button(self.frame,text="-", bg="grey", height=3, font=('Arial',24), command=self.pressMinus)
        self.btnMinus.grid(row=3,column=3,sticky="news")

        self.btnPlus = tk.Button(self.frame,text="+", bg="grey", height=3, font=('Arial',24), command=self.pressPlus)
        self.btnPlus.grid(row=4,column=3,sticky="news")

        self.btnEquals = tk.Button(self.frame,text="=", bg="dark orange", font=('Arial',24), command=self.pressEquals)
        self.btnEquals.grid(row=5,column=3,sticky="news")

        self.btnClear = tk.Button(self.frameUpper,text="C", bg="grey", font=('Arial',24), command=self.pressClear)
        self.btnClear.grid(row=0,column=0,sticky="news")

        self.btnDelete = tk.Button(self.frameUpper,text="⌫", bg="grey", font=('Arial',24), command=self.pressDelete)
        self.btnDelete.grid(row=0,column=1,sticky="news")

        self.btnFactorial = tk.Button(self.frame,text="()!", bg="grey", font=('Arial',24), command=self.pressFactorial)
        self.btnFactorial.grid(row=1,column=0,sticky="news")

        self.btnExponent = tk.Button(self.frame,text="()ⁿ", bg="grey", font=('Arial',24), command=self.pressExponent)
        self.btnExponent.grid(row=1,column=1,sticky="news")

        self.btnSQRT = tk.Button(self.frame,text="√()", bg="grey", font=('Arial',24), command=self.pressSQRT)
        self.btnSQRT.grid(row=1,column=2,sticky="news")

        self.root.mainloop()

    def pressOne(self):
        self.txt += "1"
        self.label.config(text=self.txt)
    def pressTwo(self):
        self.txt += "2"
        self.label.config(text=self.txt)
    def pressThree(self):
        self.txt += "3"
        self.label.config(text=self.txt)
    def pressFour(self):
        self.txt += "4"
        self.label.config(text=self.txt)
    def pressFive(self):
        self.txt += "5"
        self.label.config(text=self.txt)
    def pressSix(self):
        self.txt += "6"
        self.label.config(text=self.txt)
    def pressSeven(self):
        self.txt += "7"
        self.label.config(text=self.txt)
    def pressEight(self):
        self.txt += "8"
        self.label.config(text=self.txt)
    def pressNine(self):
        self.txt += "9"
        self.label.config(text=self.txt)
    def pressZero(self):
        self.txt += "0"
        self.label.config(text=self.txt)
    def pressNegative(self):
        print(lastNumber(self.txt))
    def pressPlus(self):
        self.txt += "+"
        self.label.config(text=self.txt)
    def pressMinus(self):
        self.txt += "-"
        self.label.config(text=self.txt)
    def pressMultiply(self):
        self.txt += "×"
        self.label.config(text=self.txt)
    def pressDivide(self):
        self.txt += "÷"
        self.label.config(text=self.txt)
    def pressEquals(self):
        self.txt = sympify(re.sub("×","*",re.sub("÷","/",self.txt))).evalf()
        self.txt = str(self.txt)
        if "." in self.txt:
            self.txt = self.txt.rstrip("0").rstrip(".")
        self.label.config(text=self.txt)
    def pressPeriod(self):
        self.txt += "."
        self.label.config(text=self.txt)
    def pressClear(self):
        self.txt = ""
        self.label.config(text=self.txt)
    def pressDelete(self):
        self.txt = self.txt[:-1]
        self.label.config(text=self.txt)
    def pressFactorial(self):
        print(lastNumber(self.txt))
        self.txt += "."
    def pressExponent(self):
        print(lastNumber(self.txt))
    def pressSQRT(self):
        x = lastNumber(self.txt)
        self.txt = self.txt[:-x]
        self.txt += self.txt[:lastNumber(self.txt)]

def lastNumber(expr: str):
    operators = ('+','-','÷','×','!','√')
    for i in range(len(expr)-1,-1,-1):
        if expr[i] in operators:
            return float(expr[i+1:]) #will cause issues later
    return len(expr)

Calculator()