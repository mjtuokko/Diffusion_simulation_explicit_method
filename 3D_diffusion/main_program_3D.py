import os
import make_animation_from_images as animator
import make_3D_figures_from_3D_data as figure_maker
import make_2D_figures_from_3D_data as cs_2D_figure_maker
import make_1D_figures_from_3D_data as cs_figure_maker
from datetime import datetime


#funtion to complain and run the fortran file
def complain_and_run_2D_fortran_file():
    
#make directories to save result

    os.system("mkdir Results")
    Time=datetime.now()
    Time_str = Time.strftime("%d.%m.%Y_%H:%M")
    global result_path
    result_path="Results/" +  Time_str +"/"#All subfolders is saved here
    command = "mkdir " + result_path 
    os.system(command)
    
    global Path_to_data
    Path_to_data = result_path + "3D_data/"
    command = "mkdir " + Path_to_data   #Folder for 2D_data
    os.system(command)
    global Path_to_analytical_data
    Path_to_analytical_data = result_path + "3D_analytical_data/"
    command = "mkdir " + Path_to_analytical_data  #Folder for 2D_analytical_data
    os.system(command)        

    
    #complain and run fortran file to get data
    command='./make_simulation_3D ' +str(size) + " " + str(DT) + " " + str(N) + " " + str(every_nth_save) + " " + Path_to_data
    os.system('gfortran make_simulation_3D.f90 -o make_simulation_3D')
    os.system(command)
    #complain and run fortran file to get analytical_data
    command='./make_analytical_solution_3D ' +str(size_of_analytical_solution) + " " + str(DT) + " " + str(N) + " " + str(every_nth_save) + " " + Path_to_analytical_data
    os.system('gfortran make_analytical_solution_3D.f90 -o make_analytical_solution_3D')
    os.system(command)

#function to make visualization images and animation
    
def make_visualization(make_3D_plot,make_2D_plot,make_1D_plot):
    #number of iterations
    Number_of_pictures=N
    #speed of animations
    speed_of_animations=int(N/(every_nth_save*6))
    if(speed_of_animations==0):
        speed_of_animations=1
    
    
    if(make_3D_plot==1):
        #make 2D-images and save imagenames to list
        Path_to_save_images= result_path + "3D_figures/"
        command = "mkdir " + Path_to_save_images #Folder save images
        os.system(command)  
        images=figure_maker.make_N_4d_figures(Number_of_pictures,DT,Path_to_data,Path_to_save_images,every_nth_save)
        #make animation from images
        animator.make_animation_from_images(images,speed_of_animations, result_path + "3D_animation.gif")
    
    if(make_2D_plot==1):
        #make contour images
        Path_to_save_images= result_path + "2D_Figures_from_3D_data/"
        command = "mkdir " + Path_to_save_images #Folder for 2D_analytical_data
        os.system(command)  
        images=cs_2D_figure_maker.make_N_2d_figures_from_3D_data(Number_of_pictures,DT,0.5,Path_to_data,Path_to_save_images,every_nth_save)
        #make animation from contour plots
        animator.make_animation_from_images(images,speed_of_animations, result_path + "2D_animation_from_3D_data.gif")
    
    if(make_1D_plot==1):   
        #make cross section images and save imagenames to list
        Path_to_save_images= result_path + "1D_Figures_from_3D_data/"
        command = "mkdir " + Path_to_save_images #Folder for 2D_analytical_data
        os.system(command)      
        
        
        images=cs_figure_maker.make_N_1d_figures_from_3D_data(Number_of_pictures,DT,0.5,0.5,Path_to_data,Path_to_analytical_data,Path_to_save_images,every_nth_save)
        #make animation from images
        animator.make_animation_from_images(images,speed_of_animations,result_path + '1D_animation_from_3D_data.gif')
    
  
    
def start_program(N_param,DT_param,size_param,size_of_analytical_solution_param,every_nth_save_param,make_3D_plot,make_2D_plot,make_1D_plot):
    global N
 #   N=20000 #Number of iterations
    N=N_param
    global DT
 #   DT=0.0000125 #Time step
    DT=DT_param
    global size
    size=size_param
 #   size=101 #size of matrix
    global size_of_analytical_solution
    size_of_analytical_solution=size_of_analytical_solution_param
 #   size_of_analytical_solution=101
    global every_nth_save
    every_nth_save=every_nth_save_param
 #   every_nth_save = 200 #Every nth save means a number which tells, how often results are saved   
    #make data_file
    complain_and_run_2D_fortran_file()
    #make visualization
    make_visualization(make_3D_plot,make_2D_plot,make_1D_plot)

