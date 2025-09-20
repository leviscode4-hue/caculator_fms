from tkinter import *
import math
import tkinter.messagebox


root = Tk()
root.title("calculatrice scientifique")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("485x568+0+0")

calculator = Frame(root)
calculator.grid()
#----------------------------_entry_information_-----------------------------------------------------------------
txtDisplay = Entry(calculator, font=('arial',20,'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


#----------------------------------_calculetor_logic_----------------------------------
class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum= False
        self.oper = ''
        self.result = False
    
    def numberEnter(self, num):
        self.result = False 
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value= False
        else:
            if secondnum =='.':
                if secondnum in firstnum:
                    return
            self.current= firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(txtDisplay.get())
        if self.check_sum == True:
            self.valid_function()

        else: 
            self.total= float(txtDisplay.get())
        
    def valid_function(self):
        if self.oper == 'add':
            self.total += self.current
     
        if self.oper == 'sub':
            self.total -= self.current

        if self.oper == 'mul':
            self.total *= self.current
        if self.oper == 'div':
            self.total /= self.current

        if self.oper == 'mod':
            self.total 	%= self.current

        self.input_value= True
        self.check_sum = False
        self.display(self.total)

    def operator(self,oper):
        self.current = float(txtDisplay.get())
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value= True
        self.check_sum = True
        self.oper = oper
        self.result = False


    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
        

    def clear(self):
        self.result= False
        if len(self.current)>0:
            self.current = self.current[0: len(self.current)-1]
            self.display(self.current)
        else:
            self.display(0)
            self.input_value= True
        

    def clearAll(self):
        self.display(0)
        self.input_value = True
        

    def pm(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
           
    def towpi (self):
        self.result = False
        self.current= math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current= math.e
        self.display(self.current)

    def log (self):
        self.result = False
        a = math.log(float(txtDisplay.get()))
        if a < 0:
             self.display("can't log negatif number")
        elif a == 0:
             self.display("can't log zero")
        else:
            self.current= math.log(float(txtDisplay.get()))
            self.display(self.current)

    def log2(self):
            self.result = False
            self.current= math.log2(float(txtDisplay.get()))
            self.display(self.current)

    def log10 (self):
            self.result = False
            self.current= math.log10(float(txtDisplay.get()))
            self.display(self.current)

    def log1p (self):
            self.result = False
            self.current= math.log1p(float(txtDisplay.get()))
            self.display(self.current)

    def lgamma (self):
        self.result = False
        self.current= math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def cos (self):
        self.result = False
        self.current= math.cos(float(txtDisplay.get()))
        self.display(self.current)
        
    def cosh (self):
        self.result = False
        self.current= math.cosh(float(txtDisplay.get()))
        self.display(self.current)
    
    def acosh (self):
        self.result = False
        self.current= math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def tan (self):
        self.result = False
        self.current= math.tan(float(txtDisplay.get()))
        self.display(self.current)
    
    def tanh (self):
        self.result = False
        self.current= math.tanh(float(txtDisplay.get()))
        self.display(self.current)
    
    def atanh (self):
        self.result = False
        self.current= math.atanh(float(txtDisplay.get()))
        self.display(self.current)
        
    
    def sin (self):
        self.result = False
        self.current= math.sin(float(txtDisplay.get()))
        self.display(self.current)
    
    def sinh (self):
        self.result = False
        self.current= math.sinh(float(txtDisplay.get()))
        self.display(self.current)
    
    def asinh (self):
        self.result = False
        self.current= math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def deg (self):
        self.result = False
        self.current= math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def expml (self):
        self.result = False
        self.current= math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def exp (self):
        self.result = False
        self.current= math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def sqrt (self):
        self.result = False
        self.current= math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
        

added_value = Calculator()
    

#------------------------------_buttons_---------------------------------------------------------
numberstd="789456123"
btn=[]
i = 0

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calculator, width=5, height=2, font=('arial',20,'bold'), bd=4, text=numberstd[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x= numberstd[i]: added_value.numberEnter(x)
        i+=1
#----------------------------------_standard---------------------------------------------------------
btnClear = Button(calculator, text=chr(67), width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=  added_value.clear)
btnClear.grid(row=1, column=0, pady=1)

btnAllClear= Button(calculator, text=chr(67)+chr(69), width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= added_value.clearAll)
btnAllClear.grid(row=1, column=1,pady=1)
btnsq = Button(calculator, text=chr(8730), width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= added_value.sqrt)
btnsq.grid(row=1, column=2, pady=1)
btnAdd = Button(calculator, text="+", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= lambda: added_value.operator("add"))
btnAdd.grid(row=1, column=3, pady=1)
btnSub = Button(calculator, text="-", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue",command= lambda: added_value.operator("sub"))
btnSub.grid(row=2, column=3, pady=1)
btnMul = Button(calculator, text="*", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue",command= lambda: added_value.operator("mul"))
btnMul.grid(row=3, column=3, pady=1)
btnDiv = Button(calculator, text=chr(247), width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue",command= lambda: added_value.operator("div"))
btnDiv.grid(row=4, column=3, pady=1)

btnZero = Button(calculator, text="0", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= lambda: added_value.numberEnter(0))
btnZero.grid(row=5, column=0, pady=1)
btnPoint = Button(calculator, text=".", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= lambda: added_value.numberEnter("."))
btnPoint.grid(row=5, column=1, pady=1)
btnPM = Button(calculator, text=chr(177), width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= added_value.pm)
btnPM.grid(row=5, column=2, pady=1)
btnEgual = Button(calculator, text="=", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue",command = added_value.sum_of_total)
btnEgual.grid(row=5, column=3, pady=1)
#---------------------------------------------_scientifique_-----------------------------------------------------------

btnpi = Button(calculator, text="π", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.pi )
btnpi.grid(row=1, column=4, pady=1)
btncos = Button(calculator, text="cos", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.cos)
btncos.grid(row=1, column=5, pady=1)
btntan= Button(calculator, text="tan", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.tan)
btntan.grid(row=1, column=6, pady=1)
btnsin = Button(calculator, text="sin", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.sin)
btnsin.grid(row=1, column=7, pady=1)
#.....nextrow

btn2pi = Button(calculator, text="2π", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= added_value.towpi)
btn2pi.grid(row=2, column=4, pady=1)
btncosh = Button(calculator, text="cosh", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue",command=added_value.cosh)
btncosh.grid(row=2, column=5, pady=1)
btntanh = Button(calculator, text="tanh", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.tanh)
btntanh.grid(row=2, column=6, pady=1)
btnsinh = Button(calculator, text="sinh", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.sinh)
btnsinh.grid(row=2, column=7, pady=1)
#.....nextrow

btnlog = Button(calculator, text="log", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.log)
btnlog.grid(row=3, column=4, pady=1)
btnExp = Button(calculator, text="exp", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.exp)
btnExp.grid(row=3, column=5, pady=1)
btnMod = Button(calculator, text="%", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command= lambda:added_value.operator("mod"))
btnMod.grid(row=3, column=6, pady=1)
btnE = Button(calculator, text="e", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.e)
btnE.grid(row=3, column=7, pady=1)
#............nextrow

btn2log = Button(calculator, text="log2", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.log2)
btn2log.grid(row=4, column=4, pady=1)
btnDeg = Button(calculator, text="deg", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.deg)
btnDeg.grid(row=4, column=5, pady=1)
btncosh = Button(calculator, text="acosh", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.cosh)
btncosh.grid(row=4, column=6, pady=1)
btnsinh = Button(calculator, text="asinh", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.sinh)
btnsinh.grid(row=4, column=7, pady=1)

#.........nextrow
btnlog10 = Button(calculator, text="log10", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.log10)
btnlog10.grid(row=5, column=4, pady=1)
btnlog1p = Button(calculator, text="log1p", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.log1p)
btnlog1p.grid(row=5, column=5, pady=1)
btnExpml = Button(calculator, text="expm1", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.expml)
btnExpml.grid(row=5, column=6, pady=1)
btnGamma = Button(calculator, text="lgamma", width=5,height=2, font=('arial',20,'bold'), bd=4, bg="powder blue", command=added_value.lgamma)
btnGamma.grid(row=5, column=7, pady=1)

TextDisplay = Label(calculator, text="Scientific calculator", font=('arial',30,'bold'), justify=CENTER)
TextDisplay.grid(row=0, column=4, columnspan=4)

#.....................................menu.................................................................
def quitter():
    quitter= tkinter.messagebox.askyesno("calculatrice scientifique", " Etes-vous sure de vouloire quitter ?")
    if quitter > 0:
        root.destroy()
        return

def scientifique():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")

def standard():
    root.resizable(width=False, height=False)
    root.geometry("485x568+0+0")




menubar = Menu(calculator)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Fichier ",menu=filemenu)
filemenu.add_command(label="standard", command=standard)
filemenu.add_command(label="scientific", command=scientifique)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command = quitter)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editer", menu=editmenu)
editmenu.add_command(label="couper")
editmenu.add_command(label="copier")
editmenu.add_separator()
editmenu.add_command(label="coller")

helpmenu= Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide",menu=helpmenu)
helpmenu.add_command(label="Obtenir de l'aide")




root.config(menu=menubar)
root.mainloop()