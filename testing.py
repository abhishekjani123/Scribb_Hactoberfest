from doctest import master
import tkinter
from tkinter import *
import customtkinter
from turtle import bgcolor, color
import main2
import whiteboard

def ppt():
    main2.ppt_main()

def whiteBoard():
    whiteboard.whiteboard_main()

# customtkinter Setup
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 

root = customtkinter.CTk()
root.geometry("900x480")
root.title("Scribbler")

root.resizable(False, False) 

# All Label text
lbl_txt_mode = tkinter.StringVar(value="Mode")
lbl_txt_title = tkinter.StringVar(value="Scribbler")
lbl_txt_ac = tkinter.StringVar(value="Air Canvas")

# All Labels are created here.....
label_mode = customtkinter.CTkLabel(master=root,textvariable=lbl_txt_mode,text_font=("Arial",14))
label_mode.place(relx=0.7, rely=0.32, anchor=tkinter.CENTER)

label_title = customtkinter.CTkLabel(master=root,textvariable=lbl_txt_title,text_font=("Arial",40))
label_title.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)

label_ac = customtkinter.CTkLabel(master=root,textvariable=lbl_txt_ac,text_font=("Arial",20))
label_ac.place(relx=0.3, rely=0.55, anchor=tkinter.CENTER)

# All Button created here......
b1_wb = customtkinter.CTkButton(master=root,text="White Board",command=whiteBoard,width=150,height=50,fg_color="dodger blue", text_font=("Arial",14))
b1_wb.place(relx=0.7, rely=0.42, anchor=tkinter.CENTER)

b2_ppt = customtkinter.CTkButton(master=root,text="PPT",command=ppt,width=150,height=50,fg_color="dodger blue", text_font=("Arial",14))
b2_ppt.place(relx=0.7, rely=0.58, anchor=tkinter.CENTER)

root.mainloop()