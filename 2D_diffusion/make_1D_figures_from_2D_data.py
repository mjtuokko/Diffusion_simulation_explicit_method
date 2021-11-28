#import used libraries
import numpy as np
from matplotlib import pyplot as plt


#Function to plot figures
def make_1d_figure_compare_to_c_analytical(n,c,c_analytical_sol,DT,title_shown,Path_to_save_images):
    T=n*DT #Time
    #make picture and layout
    fig = plt.figure(figsize=(16, 12), dpi=80)
    ax = plt.axes(xlim=(0, 1), ylim=(-0.1, 1.1))
    line, = ax.plot([], [], lw=2)
    #Time shown in title if wanted
    if(title_shown):
        plt.title("$C$($T$=%.5g" %T +") \n")
    else:
        plt.title("$C$($T$)")
    ax.set_xlabel('$X$')
    ax.set_ylabel("$c$")
    #make x coordinates
    y_analytical=np.linspace(0,1,len(c_analytical_sol))
    y=np.linspace(0,1,len(c))
    #plot numerical solution
    plt.plot(y,c,'-o',label="Numeerinen ratkaisu")
    #plot analytical solution
    plt.plot(y_analytical,c_analytical_sol,'--g',linewidth=3,label="Analyyttinen ratkaisu")
    #Customize layout 

    plt.legend(bbox_to_anchor=(1.1, 0.05))
    plt.grid(True)
    #save figure
    name=Path_to_save_images+"figure_"+str(n)+".png"
    plt.savefig(name)
    #close figure
    plt.close()
    return name
    
    
def make_N_1d_figures_y_constant(N,DT,y_value,Path_to_data,Path_to_analytical_data,Path_to_save_images,every_nth_save):
    plt.style.use('own_plot_style_legend_right_down.mplstyle') #use own style
    #define DT
    #make table for image names
    images=[]
    #make N figures
    for n in range(0,N,every_nth_save):
        filename=Path_to_data+"2D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        if(n==0):
            size=len(data[0])
            y_index=int((size-1)*y_value)
        #read analytical solution
        filename_analytical=Path_to_analytical_data+"2D_data_"+str(n)+".txt"
        #read data
        c_analytical = np.loadtxt(filename_analytical)
        if(n==0):
            size_analytical=len(c_analytical[0])
            y_index_analytical=int((size_analytical-1)*y_value)
        #read analytical solution
        images.append(make_1d_figure_compare_to_c_analytical(n,data[y_index],c_analytical[y_index_analytical],DT,False,Path_to_save_images))
    return images


#function to make many plots to same figure, not used in main program, should use manually
def make_several_1d_plots_y_constant(n_list,DT,x_value,Path_to_data,Path_to_analytical_data,Path_to_save_images):
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
    images=[]
    name=Path_to_save_images+"1D_figure_"
    #make plots

    for number in range(len(n_list)):
        
        
        n=n_list[number]
        
        T=n*DT #Time  $T$=%.5g' %T
        filename=Path_to_data+"2D_data_"+str(n)+".txt"
        #read data
        data_numerical = np.loadtxt(filename)
        x_index=int(x_value*(len(data_numerical[0])-1))
        c = data_numerical[x_index]      
        #make_x_axis
        y=np.linspace(0,1,len(c))
        #read analytical solution
        filename_analytical=Path_to_analytical_data+"2D_data_"+str(n)+".txt"
        #read data
        data_analytical = np.loadtxt(filename_analytical)
        x_index=int(x_value*(len(data_analytical[0])-1))
        c_analytical = data_analytical[x_index]
        #make x coordinates
        y_analytical=np.linspace(0,1,len(c_analytical))
        if(number==0):
            
            plt.plot(y,c,'o-',color='orange',markersize=9,label='Numeerinen ratkaisu')     
            
            plt.plot(y_analytical,c_analytical,'--g',label='Analyyttinen ratkaisu')

        else:
            plt.plot(y,c,'o-',color='orange',markersize=9)   

            
            plt.plot(y_analytical,c_analytical,'--g')       
            #make annotation to time
        ax.annotate('$T$=%.5g' %T, size=30, xy=(y_analytical[int(len(y_analytical)*0.7)], c_analytical[int(len(y_analytical)*0.7)]), xytext=(1.1, 1-0.2-number/len(n_list)),arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'black'},
            va='center')

        name = name + str(n) + "_"
    

    plt.legend(bbox_to_anchor=(0.55, 0.2))
    plt.grid(True)
    #save figure
    name=name+".png"
    plt.savefig(name)
    #close figure

    plt.close()