# -*- coding: utf-8 -*-
"""
Created on Sat May  7 08:38:40 2022

@author: Ace
"""

from tkinter import *

root = Tk()

root.title("Mathmatics")
root.geometry("400x400")
value = Entry(root, font=("Courier",20))
label_series = Label(root, text="Fibonacci Series:  ")
label_sum = Label(root, text = "Fibonacci Sum: ")

def Fibonacci():
    num=int(value.get())
    first_num=0
    sec_num=1
    sum=0
    counter=1
    sum2=0
    while counter <= num:
        label_series["text"] += str(sum) + " "

        sum2=sum2+sum
        counter = counter + 1
        first_num = sec_num
        sec_num= sum
        sum = first_num + sec_num

    
    sum3=sum
    label_sum["text"] += str(sum3) + " "
    
btn = Button(root,text=" Show Fibonacci Series", command= Fibonacci)  
    
btn.pack()
label_series.pack()
label_sum.pack()
value.pack()
root.mainloop()