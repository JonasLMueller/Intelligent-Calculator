
from tkinter import *

expression = "" 
  

def press(num): 
    global expression 
    expression = expression + str(num) 
    expressionVar.set(expression)
             
def equalpress(): 
    try: 
        global expression
        
        
        fenster = Toplevel()  
        fenster.configure(background="light blue") 
        fenster.geometry("250x150") 
        labeltext = Label(master=fenster,
                            text='Security Check!!\n\n Please solve the following task to show \nthat you are not a robot. \n'+expression)
        labeltext.place(x=6, y=6, width=230, height=80)
        eingabefeld = Entry(fenster)
        eingabefeld.place(x=60, y = 90, width=100,height= 20)
        buttonOk = Button(master=fenster, text='ok',
                          command = lambda: settotal(fenster) )
        
        buttonOk.place(x=90, y=120, width=30, height=20)
        
        def settotal(fenster):
            
            total = str(eingabefeld.get())
            equation.set(total) 
            fenster.destroy()
    except: 
        
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 


  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="light blue") 
  
    # set the title of GUI window 
    gui.title("Intelligent Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("600x550") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar()
    expressionVar = StringVar()
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=expressionVar)
    equation_field = Entry(gui, textvariable=equation) 
    
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=5, ipadx=30) 
   
    equation_field.grid(columnspan=5, ipadx=30)
    equation.set('') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
                     command=lambda: press(1), height=3, width=21) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='white', 
                     command=lambda: press(2), height=3, width=21) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='white', 
                     command=lambda: press(3), height=3, width=21) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
                     command=lambda: press(4), height=3, width=21) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
                     command=lambda: press(5), height=3, width=21) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
                     command=lambda: press(6), height=3, width=21) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
                     command=lambda: press(7), height=3, width=21) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
                     command=lambda: press(8), height=3, width=21) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
                     command=lambda: press(9), height=3, width=21) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='white', 
                     command=lambda: press(0), height=3, width=21) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='white', 
                  command=lambda: press("+"), height=3, width=21) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='white', 
                   command=lambda: press("-"), height=3, width=21) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='white', 
                      command=lambda: press("*"), height=3, width=21) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='white', 
                    command=lambda: press("/"), height=3, width=21) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='white', 
                   command=equalpress, height=3, width=21) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='white', 
                   command=clear, height=3, width=21) 
    clear.grid(row=5, column='1') 
  
    Decimal= Button(gui, text='.', fg='black', bg='white', 
                    command=lambda: press('.'), height=3, width=21) 
    Decimal.grid(row=6, column=0)

    ausgabe= Button(gui, text='hier', fg='black', bg='white', 
                    command=lambda: print(expression), height=3, width=21) 
    ausgabe.grid(row=6, column=1)  
    # start the GUI 
    gui.mainloop() 

