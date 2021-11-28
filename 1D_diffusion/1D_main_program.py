import os
import make_animation_from_images as animator
import make_1D_figures_from_1D_data as figure_maker

N=3000
DT=0.00005

#funtion to complain and run the fortran file
def complain_and_run_fortran_file():
    #remove old data
    os.system('rm 1D_data_files/*')
 #   os.system('rm 1D_data_files/Analytical_sol_data/*')    
    command='./make_simulation_1D ' + str(DT) + " " + str(N)
    #complain
    os.system('gfortran make_simulation_1D.f90 -o make_simulation_1D')
    #run
    os.system(command)


#function to make visualization images and animation
def make_visualization():
    #number of iterations
    Number_of_pictures=N
    #make images and save imagenames to list
    images=figure_maker.make_N_1d_figures(Number_of_pictures,DT)
    #make animation from images
    animator.make_animation_from_images(images,30, '1D_animation.gif')
    figure_maker.make_several_1d_plots([0,500,1000,1500,2000,2500,3000],0.00005)
    
#make data_file   
complain_and_run_fortran_file()
#make visualization
make_visualization()
