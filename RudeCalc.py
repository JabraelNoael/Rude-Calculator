import tkinter as tk
from sympy import sympify
import re
import random as rand
import math

class Calculator():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("400x775")
        self.root.title("Emotional Calculator")

        self.calcTxt = tk.Label(self.root, text="Hello", font=('Arial', 12))
        self.calcTxt.pack()

        self.txt = ""
        self.label = tk.Label(self.root, text=self.txt, font=('Arial', 18))
        self.label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

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

        self.btnLeftP = tk.Button(self.frame,text="(", bg="grey", font=('Arial',24), command=self.pressLParenthesis)
        self.btnLeftP.grid(row=0,column=0,sticky="news")

        self.btnRightP = tk.Button(self.frame,text=")", bg="grey", font=('Arial',24), command=self.pressRParenthesis)
        self.btnRightP.grid(row=0,column=1,sticky="news")

        self.btnClear = tk.Button(self.frame,text="C", bg="grey", font=('Arial',24), command=self.pressClear)
        self.btnClear.grid(row=0,column=2,sticky="news")

        self.btnDelete = tk.Button(self.frame,text="⌫", bg="grey", font=('Arial',24), command=self.pressDelete)
        self.btnDelete.grid(row=0,column=3,sticky="news")

        self.btnFactorial = tk.Button(self.frame,text="()!", bg="grey", font=('Arial',24), command=self.pressFactorial)
        self.btnFactorial.grid(row=1,column=0,sticky="news")

        self.btnExponent = tk.Button(self.frame,text="()²", bg="grey", font=('Arial',24), command=self.pressExponent)
        self.btnExponent.grid(row=1,column=1,sticky="news")

        self.btnSQRT = tk.Button(self.frame,text="√()", bg="grey", font=('Arial',24), command=self.pressSQRT)
        self.btnSQRT.grid(row=1,column=2,sticky="news")

        self.previousRand = 0

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
    def pressLParenthesis(self):
        self.txt += "("
        self.label.config(text=self.txt)
    def pressRParenthesis(self):
        self.txt += ")"
        self.label.config(text=self.txt)
    def pressEquals(self):
        self.txt = sympify(re.sub("×","*",re.sub("÷","/",self.txt))).evalf()
        self.txt = str(self.txt)
        if "." in self.txt:
            self.txt = self.txt.rstrip("0").rstrip(".")
        self.label.config(text=self.txt)
        x = rand.randint(0,5)
        while (x == self.previousRand):
            x = rand.randint(0,5)
        match x:
            case 0:
                self.calcTxt.config(text="You needed a calculator... for that?")
            case 1:
                self.calcTxt.config(text="Better hope Calculators are allowed on the test")
            case 2:
                self.calcTxt.config(text="Calc is short for Calculator chat.")
            case 3:
                self.calcTxt.config(text="Really putting my math degree to work.")
            case 4:
                self.calcTxt.config(text="Just checking 1+1 is still 2 headahh.")
            case 5:
                self.calcTxt.config(text="...")
        self.previousRand = x
    def pressPeriod(self):
        self.txt += "."
        self.label.config(text=self.txt)
    def pressClear(self):
        self.txt = ""
        self.label.config(text=self.txt)
    def pressDelete(self):
        self.txt = self.txt[:-1]
        self.label.config(text=self.txt)
    def pressNegative(self):
        x = lastNumber(self.txt)
        print(x)
        y = (x[0])
        self.txt = self.txt[:-x[1]]
        self.label.config(text=self.txt)
        self.txt += "-("+str(y)+")"
        self.label.config(text=self.txt)
    def pressFactorial(self):
        x = lastNumber(self.txt)
        print(x)
        if (int(x[0])==x[0]):
            y = str(math.factorial(int(x[0])))
            self.txt = self.txt[:-x[1]]
            self.label.config(text=self.txt)
            self.txt += str(y)
            self.label.config(text=self.txt)
        else:
            print("error")
            self.calcTxt.config(text="I'm not doing a Gamma function for you...")
    def pressExponent(self):
        x = lastNumber(self.txt)
        print(x)
        y = str(int(x[0])**2)
        self.txt = self.txt[:-x[1]]
        self.label.config(text=self.txt)
        self.txt += str(y)
        self.label.config(text=self.txt)
    def pressSQRT(self):
        x = lastNumber(self.txt)
        print(x)
        if (x[0] >= 0):
            y = str(math.sqrt(float(x[0])))
            self.txt = self.txt[:-x[1]]
            self.label.config(text=self.txt)
            self.txt += str(y)
            if "." in self.txt:
                self.txt = self.txt.rstrip("0").rstrip(".")
                self.label.config(text=self.txt)
        else:
            print("error")
            self.calcTxt.config(text="You think you're ready for imaginary numbers? You're not even ready for real ones.")
def lastNumber(expr: str):
    operators = ('+','-','÷','×','!','√')
    for i in range(len(expr)-1,-1,-1):
        if expr[i] in operators:
            return (float(expr[i+1:]),len(expr[i+1:]))
    return (float(expr),len(expr))

Calculator()
