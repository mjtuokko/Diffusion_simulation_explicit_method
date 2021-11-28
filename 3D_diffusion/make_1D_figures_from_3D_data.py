#import used libraries
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




'''function for making the 1st z value. Have to make in first time like this
and no matter which is the value, because it will be overwritten immediately''' 
def z_add_to_grid(x,y):
        return 0*x-0*y
    
    
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

    plt.legend(bbox_to_anchor=(1.1, 1.05))
    plt.grid(True)
    #save figure
    name=Path_to_save_images+"1D_figure_from_3d_data_"+str(n)+".png"
    plt.savefig(name)
    #close figure
    plt.close()
    return name


#function for iterating
def make_N_1d_figures_from_3D_data(N,DT,y_value,z_value,Path_to_data,Path_to_analytical_data,Path_to_save_images,every_nth_save):
    plt.style.use('own_plot_style_3d_to_1d.mplstyle') #use own style
    #make table for image names
    images=[]

    
    #make x- and c-coordinate tables

    for n in range(0,N+1,every_nth_save): #every nth data plotted
        c =[]
        filename=Path_to_data+"3D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        if(n==0):
            size=len(data[0])
        #iterate x (i) and y (j) and z (k)
        #calculate z- and y- indexes to match (X,0.4,0.4)
        if(n==0):
            y_index=int(y_value*(size-1))
            z_index=int(z_value*(size-1))
        
        for i in range(len(data[0])):
            c.append(data[y_index*size+i][z_index]) #There is n lines in one y value
                
          
            
        #analytical c to compare:
        c_analytical=[]
        filename=Path_to_analytical_data+"3D_data_"+str(n)+".txt"
        #read data
        data_analytical = np.loadtxt(filename)

        if(n==0):
            size_analytical=len(data_analytical[0])
        #calculate z- and y- indexes to match (X,0.4,0.4)
        if(n==0):
            y_index_analytical=int(y_value*size_analytical)
            z_index_analytical=int(z_value*size_analytical)
        
        #iterate        
        for i in range(size_analytical):
            
            
            c_analytical.append(data_analytical[y_index_analytical*size_analytical+i][z_index_analytical]) #There is n lines in one y value        
        #make figure


        images.append(make_1d_figure_compare_to_c_analytical(n,c,c_analytical,DT,True,Path_to_save_images))
    return images

#function to make many plots to same figure
def make_several_1d_plots_y_and_z_constant(n_list,DT,y_value,z_value,size):
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
    name="1D_Figures_from_3d_data/1D_Figures_from_3d_data_"
    #make plots

    for number in range(len(n_list)):
        
        
        n=n_list[number]
        
        T=n*DT #Time  $T$=%.5g' %T
        c =[]
        filename="3D_data_files/3D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        
        #calculate z- and y- indexes to match (X,0.4,0.4)
        if(n==0):
            y_index=int(y_value*(len(data[0])-1))
            z_index=int(z_value*(len(data[0])-1))
        #iterate x (i) and y (j) and z (k)
        for i in range(len(data[0])):
            c.append(data[y_index*len(data[0])+i][z_index]) #There is n lines in one y value
        y=np.linspace(0,1,len(c))
          
            
        #analytical c to compare:
        c_analytical=[]
        filename="3D_data_files/Analytical_sol_data/3D_data_"+str(n)+".txt"
        #read data
        data_analytical = np.loadtxt(filename)
        
        
        #calculate z- and y- indexes to match (X,0.4,0.4)
        if(n==0):
            y_index_analytical=int(y_value*(len(data_analytical[0])-1))
            z_index_analytical=int(z_value*(len(data_analytical[0])-1))

        #iterate x (i) 
        for i in range(len(data_analytical[0])):
            c_analytical.append(data_analytical[y_index_analytical*len(data_analytical[0])+i][z_index_analytical]) #There is n lines in one y value        
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
