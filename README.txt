Code for the bachelor's thesis. 

The code can simulate numerical solutions to a 1-, 2-, or 3-dimensional diffusion equation. 
Because the code contains some bash commands, it only works on Linux.
The code contains three separate programs. Each program is in its own folder and contains a simulation of a certain dimensional diffusion of its own program.
The code creates a simulation for diffusion and makes different plots of it if desired.

There are two ways to run the code.

1. To use the graphical operating system built into the program, run the program start_program.py in the folder containing the code.

2. Call the start_program function of the main_program_ (N) D.py in the folder.
The function needs several parameters:
(N_param,DT_param,size_param,size_of_analytical_solution_param,every_nth_save_param,make_3D_plot,make_2D_plot,make_1D_plot)
N_param=Number or iterations done
DT_param = The size of time step
size_param = The size of the matrix on which the diffusion is made.
size_of_analytical_solution_param = The size of the matrix on which the diffusion is made.
every_nth_save_param = How often the results are saved?
All other parameters are true values related to plotting: 1=make plot, 0=don't make.

Recommended parameters would be, for example:
N_param=5000
DT_param = 1.0e-5
size_param = 101
size_of_analytical_solution_param = 101
every_nth_save_param = 100
All other parameters are true values related to plotting: 1=make plot, 0=don't make.


The bachelor's thesis can be found in the pdf file.
