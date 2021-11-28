#import used libraries
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D





'''function for making the 1st z value. Have to make in first time like this
and no matter which is the value, because it will be overwritten immediately''' 
def z_add_to_grid(x,y):
        return 0*x-0*y
    
    



#Function to make 2d figure(n,X,Y,Z), nth figure and coordinates in parameters
def make_2d_figure(n,X,Y,Z,DT,title_shown,z_value,Path_to_save_images):
    T=n*DT #Time
    #make picture and customize layout
    #customize font
    customized_font = {'weight' : 'normal', 'size'   : 19}
    plt.rc('font', **customized_font)
    #Create and customize figure
    fig = plt.figure(figsize=(16, 12), dpi=80)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, cmap="binary",vmin=0,vmax=1)
    ax.set_xlabel('X',labelpad=50)
    ax.set_ylabel('Y',labelpad=50)
    ax.set_zlabel('c',labelpad=50)
    ax.tick_params(axis='z', which='major', pad=12)
    #Time shown in title if wanted
    if(title_shown):
        plt.title("$c$($T$=%.5g" %T +"), kun $Z$=" + str(z_value) )
    else: 
        plt.title("$c$($X$,$Y$,$T$)")
    ax.set_zlim(0,1)
    #save picture as name by n
    name=Path_to_save_images+"figure"+str(n)+".png"
    plt.savefig(name)
    plt.close()
    #return name of the saved figure
    return name
    
#function for iterating
def make_N_2d_figures_from_3D_data(N,DT,z_value,Path_to_data,Path_to_save_images,every_nth_term):
    plt.style.use('own_plot_style.mplstyle') #use own style
    #make table for image names
    images=[]
    

    
    #Make n figures
    for n in range(0,N+1,every_nth_term): #every nth data plotted
        filename=Path_to_data+"3D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        size=int(len(data[0]))
        #make x- and y-coordinates to tables
        x = np.linspace(0, 1, size)
        y = np.linspace(0, 1, size)
        #make grid
        X, Y = np.meshgrid(x, y)
        #make variable Z to the z-axis value in the grid
        #Add Z variable to the grid
        Z = z_add_to_grid(X, Y)
        
        #calculate z_index
        z_index=int(z_value*(size-1))
        #iterate x (i) and y (j)
        for i in range(size):
            for j in range(size):
                #make new z values
                Z[i][j]=data[j*size+i][z_index]
                #i (x's index) row and j'th element there.
                
                
        #make figure
        images.append(make_2d_figure(n,X,Y,Z,DT,True,z_value,Path_to_save_images))
    return images
    
