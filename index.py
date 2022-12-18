from tkinter import *
window = Tk()  

window.title("Simple Interest Calculator")
window.geometry("480x500")
window.configure(bg="black")
def caculateSi():
    p = float(princentry.get())
    r = float(ratentry.get())
    t = float(timentry.get())
    si = p*r*t/100
    si = round(si,1)
    name = username.get()
    show_label.destroy()
    outputMessage = Label(show_frame,text = name + " you have to pay " + str(si),fg="lightcyan",bg="blue",font=("century",14),bd=1,width =50)
    outputMessage.place(x=40,y=50)
    outputMessage.pack()

appLabel = Label(window,text = "SIMPLE INTEREST CALCULATOR",fg="lightcyan",bg="blue",font=("century",18),bd=5)
appLabel.place(x=40,y=50)

nameLabel = Label(window,text="Your Name",fg="lightcyan",bg="blue",font=("century",14),bd=1)
nameLabel.place(x=70,y=100)
username = Entry(window,text="",bd=1,width=22)
username.place(x=200,y=100)

p_label = Label(window,text="Principle",fg="lightcyan",bg="blue",font=("century",14),bd=1)
p_label.place(x=70,y=150)
princentry = Entry(window,text="",bd=1,width=22)
princentry.place(x=200,y=150)

r_label = Label(window,text="Rate",fg="lightcyan",bg="blue",font=("century",14),bd=1)
r_label.place(x=70,y=200)
ratentry = Entry(window,text="",bd=1,width=22)
ratentry.place(x=200,y=200)

t_label = Label(window,text="Time",fg="lightcyan",bg="blue",font=("century",14),bd=1)
t_label.place(x=70,y=250)
timentry = Entry(window,text="",bd=1,width=22)
timentry.place(x=200,y=250)

calculate =Button(window,text="CALCULATE",fg="lightcyan",bg="blue",font=("century",14),bd=1,command=caculateSi)
calculate.place(x=230,y=300)

show_frame = LabelFrame(window,text="Result",bg="blue",font=("century",13))
show_frame.pack(padx=10,pady=20)
show_frame.place(x=70,y=350)

show_label = Label(show_frame,text="",bg="blue",font=("century",15),width=25)
show_label.place(x=150,y=450)
show_label.pack()

window.mainloop()