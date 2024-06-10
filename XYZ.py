#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from time import sleep
# import time
# import os
import colorama 

from tkinter import * 
from tkinter.ttk import *

losy = ["X" , "Y" , "Z"]
wylosowane = []



start = 0

while start < 3:
    start += 1
    los = random.randrange(0, 3)
    wylosowane.append(losy[los])


root = Tk()
root.title('Gierka')
root.geometry('650x450')
root.resizable(False, False)
root.config(background="black")

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=3)
root.columnconfigure(4, weight=3)
root.columnconfigure(5, weight=3)
root.columnconfigure(6, weight=3)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=1)



class Game:
    def __init__(self):

        self.pkt = 0

        w = Canvas (root, bg="BLACK", width=150)
        w.grid(column=1, row=1)

        x = Canvas (root, bg="BLACK", width=150)
        x.grid(column=3, row=1)

        t = Canvas (root, bg="BLACK", width=150)
        t.grid(column=5, row=1)

        self.litera1 = Label(root, text=wylosowane[0], font=('Arial', 80), background="BLACK", foreground="#cc33ff")
        self.litera1.grid(column=1, row=1)

        self.litera2 = Label(root, text=wylosowane[1], font=('Arial', 80), background="BLACK", foreground="#cc33ff")
        self.litera2.grid(column=3, row=1)

        self.litera3 = Label(root, text=wylosowane[2], font=('Arial', 80), background="BLACK", foreground="#cc33ff")
        self.litera3.grid(column=5, row=1)
    
        self.znak = Label(root, text ="", font=('Arial', 20), background="BLACK", foreground="#33cc33")  
        self.znak.grid(column=5, row=0)

        root.after(5000, self.setings)

    def setings(self):
        self.NowyLos()
        self.Ustawienia()

    def NowyLos(self):
        los = random.randrange(0, 3)
        wylosowane.pop(0)
        wylosowane.insert(2, losy[los])
        
        self.litera1.config(text="")

        self.litera2.config(text="")

        self.litera3.config(text=wylosowane[2])


    def OdpTak(self):
        if(wylosowane[0] != wylosowane[2]):
            self.Wrong()

        if(wylosowane[0] == wylosowane[2]):
            self.Poprawnie()
            self.NowyLos()

    def OdpNie(self):
        if(wylosowane[0] == wylosowane[2]):
            self.Wrong()
        
        if(wylosowane[0] != wylosowane[2]):
            self.Poprawnie()
            self.NowyLos()

    def Ustawienia(self):
        style = Style()
 
        style.configure('TButton', font =
            ('calibri', 10),
            foreground = '#cc33ff', background="BLACK", activebackground='#cc33ff', activeforeground="BLACK")
        

        message = Label(root, text="Czy pierwsza i ostatnia pozycja są takie same?", justify=CENTER, foreground="#cc33ff", font=('Arial', 15), background="BLACK")
        message.grid(column=1, columnspan=4, row=0, sticky=EW)

        b1 = Button (root, style = 'TButton', text ="Tak", command= self.OdpTak)
        b1.grid(column=1, columnspan=3, row=2)

        b2 = Button (root, style = 'TButton', text ="Nie", command= self.OdpNie)
        b2.grid(column=3, columnspan=3, row=2)

    def Poprawnie(self):
        self.pkt += 1
        self.znak.config(text= str(self.pkt) + " pkt")
    
    def Wrong(self):
        for widgets in root.winfo_children():
            widgets.destroy()

        message1 = Label(root, text="Źle", foreground="#cc33ff", font=('Arial', 50), background="BLACK")
        message1.grid(column=0,columnspan=7, row=0)

        message = Label(root, text=str(self.pkt) + " pkt", foreground="#cc33ff", font=('Arial', 50), background="BLACK")
        message.grid(column=0,columnspan=7, row=1)

        # if(self.pkt >= 5):
        #     message1 = Label(root, text="Ktoś coś ma.", foreground="#cc33ff", font=('Arial', 20), background="BLACK")
        #     message1.grid(column=0,columnspan=7, row=3)

        self.litera1k = Label(root, text=wylosowane[0], font=('Arial', 50), background="BLACK", foreground="#cc33ff")
        self.litera1k.grid(column=1, row=2)

        self.litera2k = Label(root, text=wylosowane[1], font=('Arial', 50), background="BLACK", foreground="#cc33ff")
        self.litera2k.grid(column=3, row=2)

        self.litera3k = Label(root, text=wylosowane[2], font=('Arial', 50), background="BLACK", foreground="#cc33ff")
        self.litera3k.grid(column=5, row=2)


gra = Game()


root.mainloop()