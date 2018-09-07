# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 16:43:58 2018

@author: kennedy
"""

from AlphabetSoup import AlphabetSoup
import tkinter as tk

        
window = tk.Tk()
window.title('AlphabetSoup')
window.geometry("600x300")


def result():
    msg = textvar.get()
    alph = textvar2.get()
    ASOUP = AlphabetSoup(msg, alph)
    return label2.config(text = str(ASOUP.Alphabet()))
  
#label
label1 = tk.Label(window, text='AlphabetSoup', font=("Helvetica Bold italic", 16), justify='left', fg = "light green", bg = "dark green")
label1.grid(row = 0, column = 0)

label1 = tk.Label(window, text='Message', font=("Helvetica", 12), justify='left', fg="red")
label1.grid(row = 1, column = 0)
#Entries
textvar = tk.StringVar()
entry1 = tk.Entry(window, textvariable = textvar, width = 50)
entry1.grid(row = 1, column = 1)


label1 = tk.Label(window, text='Alphabet', font=("Helvetica", 12), justify='left', fg="red")
label1.grid(row = 2, column = 0)
#Alphabet
textvar2 = tk.StringVar()
entry2 = tk.Entry(window, textvariable = textvar2, width = 50)
entry2.grid(row = 2, column = 1)


but1 = tk.Button(window, text = 'Exexute', command = result)
but1.grid(row = 3, column = 0)


label2 = tk.Label(window, text='', font=("Helvetica", 12), justify='left', fg="red", width = 50)
label2.grid(row = 4, column = 1, rowspan = 5)
window.mainloop()
