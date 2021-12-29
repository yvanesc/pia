from tkinter import *
import string
import random

global mode
mode = 0

sizex = 700
sizey = 400
posx  = 0
posy  = 0
pia_face = [":-)", ";-)", "8-)", ":-S", ":-D"]
msg_hist = []
pia_hist = []
greetings =["Hello","Hi","Good Morning"]
thanks =["Fine","Thank you","Great"]
window = Tk() 

window.title("ChatBot 0.1 PIA")

window.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

lbl01 = Label(window, text=random.choice(pia_face), font=("Arial Bold", 10), bg="black", fg="green")
lbl01.grid(column=0, row=0)

#value=int(x)
value = int(sizex/50)
for i in range(value):
    pia_hist.append(Label(window,text="..........yes.............."+str(i), bg="black", fg="green"))
    pia_hist[i].grid(column=0, row=i+1)    

#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

for j in range(value):
    msg_hist.append(Entry(window,width=80, state='disabled'))
    msg_hist[j].grid(column=1, row=j+1) 

msg2pia = Entry(window,width=80)
msg2pia.grid(column=1, row=j+1)
msg2pia.focus_set()
def clicked():
    global mode

    # create history msg2pia
    res =  msg2pia.get()
    # last_hist = j
    for jj in range(value):
        msg_hist[jj].configure(state='normal')
        msg_hist[jj].delete(0,'end')
        if jj == j:
            msg_hist[jj].insert(END,msg2pia.get())
        else:
            msg_hist[jj].insert(END,msg_hist[jj+1].get())
            msg_hist[jj].configure(state='disabled')

    # create history pia

    #     #msg_hist.append(Entry(window,width=80, state='normal'))

    #     msg_hist[j].grid(column=1, row=j+1) 

    # txt02.delete(0,'end')
    # txt02.insert(END,res)
    # txt03.delete(0,'end')
    #remove = string.whitespace
    res = res.strip()
    #greetings
    if res.lower() == "hello":
        pia_hist[i].configure(text= random.choice(greetings)) #"Hello")
    # Training mode
    elif res.lower() == "how are you ?":
        pia_hist[i].configure(text= random.choice(thanks)) #"Hello")
    elif res == "!?" or res =="?!":
        if mode == 0:
            pia_hist[i].configure(text= "Training mode")           
            mode = 1
        else:
            pia_hist[i].configure(text= "...")
            mode = 0
    for ii in range(value):
    #pia_hist[ii].delete(0,'end')
    #.cget("text")
        pia_hist[ii].configure(text =  pia_hist[ii + 1].cget("text"))
    # goodbye
    # Thanks
    # noanswer
    
    else:
        pia_hist[i].configure(text= "...")
    #msg2pia.delete(0,'end')
    #clicked02()
def clicked02():
    msg2pia.delete(0,'end')
    #txt02.select_clear()

btn_send = Button(window, text="Send Msg", command=clicked)
btn_send.grid(column=1, row=i+3)

btn_cls = Button(window, text="Clean", command=clicked02)
btn_cls.grid(column=0, row=i+2)

#btn_exit = Button(window, text="Exit", command=clicked02)
#btn_exit.grid(column=2, row=3)
# bind return button
window.bind('<Return>', (lambda e, btn_send=btn_send: btn_send.invoke()))

window.mainloop()