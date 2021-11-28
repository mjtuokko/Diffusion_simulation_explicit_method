#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:28:31 2021

@author: mjtuokko
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import main_program_3D as start
#make root window  
root = Tk()
root.geometry("500x700")
root.title("3D Diffusion")

#define variables
Number_of_iterations=10000
Number_of_points=101
Number_of_points_analytical=101
Every_nth_save = 500 #Every nth save means a number which tells, how often results are saved
DT = 0.0000125 # Timestep

#booleans which plots will be made
make_2d_plots=tk.IntVar()
make_3D_plots=tk.IntVar()
make_1d_plots=tk.IntVar()



#Function when button is pressed
def Button_Pressed():
    
    All_parameters_are_good=True    

    Number_of_points=int(Number_of_points_input.get("1.0", "end-1c"))
    Number_of_points_analytical=int(Number_of_points_analytical_input.get("1.0", "end-1c"))
    
    if(Number_of_points%2==0 or Number_of_points_analytical%2==0 or Number_of_points<=0 or Number_of_points_analytical<=0):
        messagebox.showinfo("Warning", "Number of points should be an odd number.")
        All_parameters_are_good=False

    Every_nth_save=int(Every_nth_input.get("1.0", "end-1c"))
    
    if (Every_nth_save<=0):
        messagebox.showinfo("Warning", "N should be > 0.")        
        All_parameters_are_good=False
    Number_of_iterations=int(Number_of_iterations_input.get("1.0", "end-1c"))  
    if(Number_of_iterations<=0):
        All_parameters_are_good=False
        messagebox.showinfo("Warning", "Number of iterations should be > 0.")         
    DT=float(DT_input.get("1.0", "end-1c"))
    if(6*(Number_of_points-1)**2>=1/DT):
        messagebox.showinfo("Warning", "DT should be smaller. For " + str(Number_of_points) + " maximum value for DT is " + str(1/(6*(Number_of_points-1)**2)) )
        All_parameters_are_good=False
    if(All_parameters_are_good):
        messagebox.showinfo("Information", "Parameters are acceptable! Pressing OK, the simulation starts. This may take a while.")
        
        start.start_program(Number_of_iterations,DT,Number_of_points,Number_of_points_analytical,Every_nth_save,make_3D_plots.get(),make_2d_plots.get(),make_1d_plots.get())
        Ready = Label(text = " Ready! \n See results in the result folder.")
        Ready.pack()
        messagebox.showinfo("Information", "Ready! \n See results in the result folder.")
    
l = Label(text = "Define parameters and answer questions.")

#make many textboxes and labels for every parameter
Number_of_points_Label = Label(text = "How many points you want per axis \n in the numerical solution? (Odd number)")
Number_of_points_input = Text(root, height = 1,
                width = 5,
                bg = "white")

Number_of_points_input.insert("end-1c",str(101))


Number_of_points_analytical_Label = Label(text = "How many points you want per axis \n in the analytical solution? (Odd number)")
Number_of_points_analytical_input = Text(root, height = 1,
                width = 5,
                bg = "white")
Number_of_points_analytical_input.insert("end-1c",str(101))

Every_nth_Label = Label(text = "Every Nth result is saved. Define the integer N: \n It is recommended to be at least 1/100 of the number of iterations. \n [Not even recommended to use because not even cool pictures.]")
Every_nth_input = Text(root, height = 1,
                width = 5,
                bg = "white")
Every_nth_input.insert("end-1c",str(100))

DT_Label = Label(text = "Define DT (the size of the time step)  \n (Too high values do not lead to stable results)")
DT_input = Text(root, height = 1,
                width = 10,
                bg = "white")
DT_input.insert("end-1c",str(0.0000125))


Number_of_iterations_Label = Label(text = "How many iterations are performed?")
Number_of_iterations_input = Text(root, height = 1,
                width = 7,
                bg = "white")
Number_of_iterations_input.insert("end-1c",str(1000))

Run_button = Button(root, height = 2,
                 width = 30, 
                 text ="Run",
                 command = lambda:Button_Pressed())

    
#Make Checkbutton to booleans

c1 = tk.Checkbutton(root, text='I want 3D plots. This is a slow process, so it is not \n recommended to create a large number (over ~10) of 3D images. \n [Not even recommended to use because not even cool pictures.]',variable=make_3D_plots, onvalue=1, offvalue=0)
c2 = tk.Checkbutton(root, text='I want 2D cross section plots.',variable=make_2d_plots, onvalue=1, offvalue=0)
c3 = tk.Checkbutton(root, text='I want 1D cross section plots.',variable=make_1d_plots, onvalue=1, offvalue=0)


#pack everything

l.pack()
Number_of_iterations_Label.pack()
Number_of_iterations_input.pack()

DT_Label.pack()
DT_input.pack()

Every_nth_Label.pack()
Every_nth_input.pack()

Number_of_points_Label.pack()

Number_of_points_input.pack()

Number_of_points_analytical_Label.pack()
Number_of_points_analytical_input.pack()


c1.pack()
c2.pack()
c3.pack()


Run_button.pack()


#make visible 

mainloop()


