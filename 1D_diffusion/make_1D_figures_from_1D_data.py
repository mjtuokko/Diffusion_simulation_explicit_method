#import used libraries
import numpy as np
from matplotlib import pyplot as plt
#function to get data from file
def get_data_from_file(filename):
    data = np.loadtxt(filename)
    return data
#Function to plot figures
def make_1d_figure_compare_to_c_analytical(n,c,c_analytical_sol,DT,title_shown,name_beginning):
    T=n*DT #Time
    #make picture and layout
    fig = plt.figure(figsize=(16, 12), dpi=80)
    ax = plt.axes(xlim=(0, 1), ylim=(-0.1, 1.1))
    line, = ax.plot([], [], lw=2)
    #Time shown in title if wanted
    if(title_shown):
        plt.title("$c$($T$=%.5g" %T +")")
    ax.set_xlabel('$X$')
    ax.set_ylabel("$c$")
    #make x coordinates
    y_analytical=np.linspace(0,1,len(c_analytical_sol))
    y=np.linspace(0,1,len(c))
    #plot numerical solution
    plt.plot(y,c,'-o',label="Numeerinen ratkaisu")
    #plot analytical solution
    plt.plot(y_analytical,c_analytical_sol,'--g',linewidth=3,label="Analyttinen ratkaisu")
    #Customize layout 

    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.grid(True)
    #save figure
    name=name_beginning+"figure_" + str(n)+".png"
    plt.savefig(name)
    #close figure
    plt.close()
    return name

def make_N_1d_figures(N,DT,Path_to_data,Path_to_analytical_data,Path_to_save_images,every_nth_save):
    #customize style
    plt.style.use('own_plot_style.mplstyle')
    #make table for image names
    images=[]
    #make N figures
    for n in range(0,N,every_nth_save):    #every nth time step plotted
        filename=Path_to_data+"1D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        #read analytical solution
        filename_analytical=Path_to_analytical_data+"1D_data_"+str(n)+".txt"
        #read data
        c_analytical = np.loadtxt(filename_analytical)
        images.append(make_1d_figure_compare_to_c_analytical(n,data,c_analytical,DT,True,Path_to_save_images))
    return images


#function to make many plots to same figure, NOTICE that this should be used manually.
def make_several_1d_plots(n_list,DT,Path_to_data,Path_to_analytical_data,Path_to_save_images):
    plt.style.use('own_plot_style.mplstyle')
#    customized_font = {'weight' : 'normal', 'size'   : 19}
#    plt.rc('font', **customized_font)
    #define DT
    #make picture and layout
    fig = plt.figure(figsize=(20, 12), dpi=80)
    ax = plt.axes(xlim=(0, 1), ylim=(-0.1, 1.1))
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    line, = ax.plot([], [], lw=2)
    #make title
    plt.title("$c$($T$)")
    ax.set_ylabel("$c$")
    ax.set_xlabel("$X$")
    #make table for image names
    name=Path_to_save_images+"figure_"
    #make plots

    for number in range(len(n_list)):
        
        
        n=n_list[number]
        
        T=n*DT #Time  $T$=%.5g' %T
        filename=Path_to_data+"1D_data_"+str(n)+".txt"
        #read data
        c = np.loadtxt(filename)
        #make_x_axis
        y=np.linspace(0,1,len(c))
        #read analytical solution
        filename_analytical=Path_to_analytical_data+"1D_data_"+str(n)+".txt"
        #read data
        c_analytical = np.loadtxt(filename_analytical)
        #make x coordinates
        y_analytical=np.linspace(0,1,len(c_analytical))
        if(number==0):
            
            plt.plot(y,c,'o-',color='orange',markersize=16,label='Numeerinen ratkaisu')     
            
            plt.plot(y_analytical,c_analytical,'--g',label='Analyyttinen ratkaisu')
            
        else:
            plt.plot(y,c,'o-',color='orange',markersize=16)   

            
            plt.plot(y_analytical,c_analytical,'--g')       
            #make annotation to time
        ax.annotate('$T$=%.5g' %T, size=30, xy=(y_analytical[-1], c_analytical[-1]), xytext=(1.05, c_analytical[-1]),arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'black'},
            va='center')

        name = name + str(n) + "_"
    


    plt.legend(bbox_to_anchor=(1.15, 1.1))
    plt.grid(True)
    #save figure
    name=name+".png"
    plt.savefig(name)
    #close figure

    plt.close()
