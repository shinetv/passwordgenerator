from random import *
from tkinter import *

num = "0123456789"
alphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Spalphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'#@+() {}"

# passlen = int(input("enter password length \n"))
# randPass = []
#
# print("select the type of password \n1. number\n2.alphanum\n3.special alphanumeric\n")
# Selecttype = int(input())
#
# if Selecttype == 1:
#     for i in range(passlen):
#         randPass.append(choice(num))
# elif Selecttype == 2:
#     for i in range(passlen):
#         randPass.append(choice(alphanum))
# else:
#     for i in range(passlen):
#         randPass.append(choice(Spalphanum))
#
# result = "".join(randPass)
#
# print(" your random password is : "+result)



def Create_pass():

    TheChoice = Tchoice.get()

    if TheChoice =="":
       resultBox.delete(0.0,END)
       resultBox.insert(END,"\n select the type of password you'd like")

    length = int(pass_length.get())
    randPass = []
    for i in range(length):
        randPass.append(choice(TheChoice))

    result = "".join(randPass)

    TheResult = "\n *** Your password is : "+result+" ***\n"

    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)




window = Tk()
window.geometry("800x500")
window.title("shine Password Generator")

ProgName = Label(window,font=('Kristen ITC',15,'bold'),text="Password Generator (^_^)",fg="blue")
ProgName.grid(row=1,column=3,padx=200,pady=30)

chooseType = Label(window,font=('italian ITC',15,'bold'),text="choose a type among the Three")
chooseType.place(relx=.02, rely=.2)

Tchoice = StringVar()
Numchoice = Radiobutton(window,font=('corbel',14,'italic'),text = "Numeric", variable = Tchoice,value=num)
Numchoice.place(relx=.03, rely=.3)
AlphaNumchoice = Radiobutton(window,font=('corbel',14,'italic'),text = "AlphaNumeric", variable = Tchoice,value=alphanum)
AlphaNumchoice.place(relx=.03, rely=.4)
Specialchoice = Radiobutton(window,font=('corbel',14,'italic'),text = "Special", variable = Tchoice,value=Spalphanum)
Specialchoice.place(relx=.03, rely=.5)


size = Label(window,text="size",font=('copperplate Gothic',14,'bold'))
size.place(relx=.66, rely=.4)

pass_length = Spinbox(window,from_=8,to=100)
pass_length.place(relx=.71, rely=.4)
pass_length.config(state="readonly")

GenButton = Button(window,text = "GENERATE",command=Create_pass)
GenButton.place(relx = .35, rely = .57)

resultBox = Text(window, height=4, width = 70)
resultBox.place(relx=.09, rely=.7)





window.mainloop()