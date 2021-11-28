import os
import make_animation_from_images as animator
import make_3D_figures_from_3D_data as figure_maker
import make_1D_figures_from_3D_data as cs_figure_maker
import make_2D_figures_from_3D_data as cs_2d_figure_maker
import time

N=3000 #number of timesteps
DT=0.00000125
size=11 #size of matrix
every_nth_save=200 #how often results are wroten (every nth timestep)
name_of_subfolder="" #"DT="+str(DT)+",DX="+str(1/(size-1))  #empty if not wanted to the subfolder, NOTICE THIS IS NOT USED IN VISUALIZATION!
#funtion to complain and run the fortran file
def complain_and_run_3D_fortran_file():
    

    #make direction to result if subfolder is not empty
    if(name_of_subfolder!=""):
        print(name_of_subfolder)
        command="rm -r 3D_data_files/"+name_of_subfolder
        os.system(command)
        command="mkdir 3D_data_files/"+name_of_subfolder
        os.system(command)
        command="mkdir 3D_data_files/"+name_of_subfolder+"/Analytical_sol_data"
        os.system(command)
    
    #delete old results
    os.system('rm 3D_data_files/*')
#    os.system('rm 3D_data_files/Analytical_sol_data/*')
    command='time ./make_simulation_3D ' + str(size) + " "  + str(DT) + " " + str(N) + " " + str(every_nth_save) + " " + name_of_subfolder
    #complain and run
    os.system('gfortran make_simulation_3D.f90 -o make_simulation_3D')
    #save time used to execute file
    start_time = time.time()
    os.system(command)
    end_time = time.time()
    print("time used:", end_time-start_time)
    #write time used to the file
    with open('3D_data_files/'+name_of_subfolder+'/time_used_to_execute.txt', 'w') as f:
        f.write('DT '+str(DT))
        f.write(', DX '+str(1/(size-1)))
        f.write(', Number of timesteps '+str(N))
        f.write(", time "+str(end_time-start_time))


#function to make visualization images and animation
def make_3D_visualization():
    #number of iterations
    Number_of_pictures=N
    #make images and save imagenames to list
    images=figure_maker.make_N_4d_figures(Number_of_pictures,DT,every_nth_save)
    #make animation from images
    animator.make_animation_from_images(images,15, "4D_animation.gif")
def make_1D_visualization():
    #number of iterations
    Number_of_pictures=N
    #make images and save imagenames to list
    images=cs_figure_maker.make_N_1d_figures_from_3D_data(N,DT,0.5,0.5,size,every_nth_save) 
    #make animation from images
    animator.make_animation_from_images(images,2, "1D_animation_from_3d_data.gif")
     
def make_2D_visualization():
    #number of iterations
    Number_of_pictures=N
    #make images and save imagenames to list
    images=cs_2d_figure_maker.make_N_2d_figures_from_3D_data(Number_of_pictures,DT,0.5, every_nth_save)
    #make animation from images
    animator.make_animation_from_images(images,15, "2D_from_3D_animation.gif")
    
#make data_file
complain_and_run_3D_fortran_file()
#make visualization
#make_3D_visualization()
#make_2D_visualization()
#make_1D_visualization()
