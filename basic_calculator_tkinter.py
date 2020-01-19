from tkinter  import *
expression = ""
#Main Function
def press(num):
    global expression
    num = str(num)
    if num == "=":
        try:
            total = str(eval(expression))
            equation.set(total)
            expression = ""
        except:
            equation.set("Error")
            expression = ""
    elif num == "&":
        expression = ""
        equation.set("")
    else:
        expression += str(num)
        equation.set(expression)
#Driver Program
if __name__ == "__main__":
    main_frame = Tk()
    main_frame.title("Calculator")
    main_frame.configure(background="white")
    main_frame.geometry("305x180")
    equation = StringVar()
    equation.set("Enter your expression")
    #Widgets
    expression_field = Entry(main_frame,textvariable=equation,background="black",foreground="white").grid(columnspan=4,ipadx=70,ipady=1)
    button_num = Button(main_frame,text = "1",width=5,height=1,command=lambda: press(1)).grid(row=2,column=0)
    button_num = Button(main_frame,text = "2",width=5,height=1,command=lambda: press(2)).grid(row=2,column=1)
    button_num = Button(main_frame,text = "3",width=5,height=1,command=lambda: press(3)).grid(row=2,column=2)
    button_num = Button(main_frame,text = "+",width=5,height=1,command=lambda: press("+")).grid(row=2,column=3)
    button_num = Button(main_frame,text = "4",width=5,height=1,command=lambda: press(4)).grid(row=3,column=0)
    button_num = Button(main_frame,text = "5",width=5,height=1,command=lambda: press(5)).grid(row=3,column=1)
    button_num = Button(main_frame,text = "6",width=5,height=1,command=lambda: press(6)).grid(row=3,column=2)
    button_num = Button(main_frame,text = "-",width=5,height=1,command=lambda: press("-")).grid(row=3,column=3)
    button_num = Button(main_frame,text = "7",width=5,height=1,command=lambda: press(7)).grid(row=4,column=0)
    button_num = Button(main_frame,text = "8",width=5,height=1,command=lambda: press(8)).grid(row=4,column=1)
    button_num = Button(main_frame,text = "9",width=5,height=1,command=lambda: press(9)).grid(row=4,column=2)
    button_num = Button(main_frame,text = "*",width=5,height=1,command=lambda: press("*")).grid(row=4,column=3)
    button_num = Button(main_frame,text = "(",width=5,height=1,command=lambda: press("(")).grid(row=5,column=0)
    button_num = Button(main_frame,text = "0",width=5,height=1,command=lambda: press(0)).grid(row=5,column=1)
    button_num = Button(main_frame,text = "^",width=5,height=1,command=lambda: press("**")).grid(row=5,column=2)
    button_num = Button(main_frame,text = ".",width=5,height=1,command=lambda: press(".")).grid(row=5,column=3)
    button_num = Button(main_frame,text = ")",width=5,height=1,command=lambda: press(")")).grid(row=6,column=0)
    button_num = Button(main_frame,text = "Clear",width=5,height=1,command=lambda: press("&")).grid(row=6,column=1)
    button_num = Button(main_frame,text = "=",width=5,height=1,command=lambda: press("=")).grid(row=6,column=2)
    button_num = Button(main_frame,text = "/",width=5,height=1,command=lambda: press("/")).grid(row=6,column=3)
    #Infinte Loop
    main_frame.mainloop()