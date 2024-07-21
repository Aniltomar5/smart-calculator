from tkinter import *                                                
import math

def click(value):
    #print(value)
    a =entryField.get()
    answer = ""
    try:
        if value=="C":
            a =a[0:len(a)-1]
            entryField.delete(0,END)
            entryField.insert(0,a)
            return
        elif value == "CE":
            answer =entryField.delete(0,END)
            return
        elif value=="√":
            answer=math.sqrt(eval(a))

        elif value=="π":
            answer = math.pi
            
        elif value == "cosθ":
            answer=math.cos(math.radians(eval(a)))
            
        elif value == "tanθ":
            answer=math.tan(math.radians(eval(a)))
            
        elif value == "sinθ":
            answer=math.sin(math.radians(eval(a)))
            
        elif value == "2π":
            answer = 2*math.pi
            
        elif value == "cosh":
            answer=math.cosh(eval(a))
            
        elif value == "tanh":
            answer=math.tanh(eval(a))
            
        elif value == "sinh":
            answer=math.sinh(eval(a))
            
        elif value == chr(8731):
            answer = eval(a)**(1/3)

        elif value == "x\u02b8":
            entryField.insert(END,"**")
            return
        elif value == "x\u00B3":
            answer = eval(a)**(3)
            
        elif value == "x\u00B2":
            answer = eval(a)**(2)
            
        elif value == "ln":
            answer = math.log2(eval(a))
            
        elif value == "deg":
            answer = math.degrees(eval(a))

        elif value == "rad":
            answer = math.radians(eval(a))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(a))

        elif value == 'x!':
            answer = math.factorial(eval(a))

        elif value == chr(247):  # devision
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(a)
        
        else:
            entryField.insert(END,value)
            return
        entryField.delete(0,END)
        entryField.insert(0,answer)
    except SyntaxError:
        pass

root = Tk()
root.title('smart Calculator')
root.config(bg='cyan')
root.geometry('680x486+400+100')

# logoImage=PhotoImage(file='logoA.png')
# logoLabel=Label(root,image=logoImage)
# logoLabel.grid(row=0,column=0)

entryField = Entry(root,font=('arial',20,'bold'),bg = 'cyan',fg = 'white',bd = 10,relief=SUNKEN,width=30)
entryField.grid(row=0,column=0,columnspan =8)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue=1   
columnvalue=0
for i in button_text_list:

    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='cyan',fg='white',font=('arial',18,'bold'),activebackground='cyan',command=lambda button=i: click(button))
    
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0
        

root.mainloop()