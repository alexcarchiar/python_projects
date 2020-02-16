# -*- coding: utf-8 -*-

'''
+--------------------------------------------------------------------------------+
|                                    ver 1.0                                     |
|   This is a simple bot to send emails created by alexcarchiar                  |
|   Created just to get a first glance of the smtplib and tkinter modules        |
+--------------------------------------------------------------------------------+
'''

import smtplib
import tkinter as tk

def email_bot():
    #we start by getting all of the input parameters from the window
    fromaddr = txt_0.get()
    username = fromaddr
    password = txt_1.get()
    toaddrs = txt_2.get()
    from_str = "From : " + fromaddr
    to_str = "To: " + toaddrs
    subj = txt_3.get()
    subj_str = "Subject: " + subj
    port = txt_4.get()
    text  = txt_5.get()
    msg = "\r\n".join([
            from_str,
            to_str,
            subj_str,
            "",
            text,
        ])
    '''
    the try -- exception is used to in case there is an error with sending the emails so we can tell the user
    I didn't specify any exception since there could be multiple ones and frankly I don't really care to find
    out which one is which
    '''
    try:
        server = smtplib.SMTP(port)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        #i = int(input("How many emails? "))
        i = int(txt_6.get())
        for i in range(0,i):
            server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        change_label()
    except:
        print("Error: couldn't send emails")
        lbl.configure(text= "Couldn't send emails, sorry! Close the program and check your parameters!")

def change_label():
    res = "Made it! Check out your inbox to make sure! Bye Bye!"
    lbl.configure(text = res)
    window.mainloop()

def byebye():
    window.destroy()

#building window
window = tk.Tk()
window.title("Email bot by alexcarchiar")
lbl_0 = tk.Label(window, text ="Fill up someone's email address with this lovely bot")
lbl_0.grid(column=0, row=0)
lbl_1 = tk.Label(window, text="Insert sender's email address")
lbl_1.grid(column=0,row=1)
txt_0 = tk.Entry(window, width = 25)
txt_0.grid(column=0,row=2)
lbl_2 = tk.Label(window, text="Insert password")
lbl_2.grid(column=0,row=3)
txt_1 = tk.Entry(window, width = 25,show='*')
txt_1.grid(column = 0, row = 4)
lbl_3 = tk.Label(window, text="Insert receiver's address")
lbl_3.grid(column= 0, row=5)
txt_2 = tk.Entry(window, width = 25)
txt_2.grid(column=0,row=6)
lbl_4 = tk.Label(window, text = "Insert subject")
lbl_4.grid(column= 0,row=7)
txt_3 = tk.Entry(window,width = 25)
txt_3.grid(column=0,row=8)
lbl_5 = tk.Label(window, text="Insert the host and the port in this format: smtp.gmail.com:587")
lbl_5.grid(column=0,row=9)
txt_4 = tk.Entry(window,width = 25)
txt_4.grid(column=0,row= 10)
lbl_6 =tk.Label(window, text="Insert the text you want to send")
lbl_6.grid(column=0,row=11)
txt_5 = tk.Entry(window, width=25)
txt_5.grid(column=0,row=12)
lbl_7 = tk.Label(window, text="How many emails?")
lbl_7.grid(column=0,row=13)
txt_6 = tk.Entry(window, width = 4)
txt_6.grid(column=0,row=14)
btn1 = tk.Button(window, text = "Click me when done", command=email_bot)
btn1.grid(column=0,row=15)
lbl = tk.Label(window, text="")
lbl.grid(column=0,row=16)
btn2 = tk.Button(window, text = "Click me to exit the program", command=byebye)
btn2.grid(column=0,row=17)
window.mainloop()
