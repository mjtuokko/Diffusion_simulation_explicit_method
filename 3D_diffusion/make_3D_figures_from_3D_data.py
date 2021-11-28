#import used libraries
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




'''function for making the 1st z value. Have to make in first time like this
and no matter which is the value, because it will be overwritten immediately''' 
def z_add_to_grid(x,y):
        return 0*x-0*y
    
    



#Function to make 2d figure(n,X,Y,Z), nth figure and coordinates in parameters
def make_4d_figure(n,data,DT,title_shown,Path_to_save_images,size):
    T=n*DT #Time
    #make picture and customize layout
    #customize font
    customized_font = {'weight' : 'normal', 'size'   : 19}
    plt.rc('font', **customized_font)
    #Create and customize figure
    fig = plt.figure(figsize=(16, 12), dpi=80)
    ax = plt.axes(projection='3d')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.set_xlabel('$X$ (%)',labelpad=40)
    ax.set_ylabel('$Y$ (%)',labelpad=40)
    ax.set_zlabel('$Z$ (%)',labelpad=40)
    ax.tick_params(axis='z', which='major', pad=12)
    mask = data > 0.15
    for i in range(len(data)):
         for j in range(len(data[0])):
             for k in range(len(data[0][0])):
                 if(data[i][j][k]<0.1):
                     data[i][j][k]=0
    idx = np.arange(int(np.prod(data.shape)))
    x, y, z = np.unravel_index(idx, data.shape)
    p=ax.scatter(x, y, z, c=data.flatten(), s=0.7*101**2/size**2, alpha=0.7, marker="o", cmap="Reds", edgecolors=None, vmin=0, vmax=1, linewidth=0)
    plt.tight_layout()
    #Time shown in title if wanted
    if(title_shown):
        plt.title("$C$($T$=%.5g" %T +")")
    else: 
        plt.title("$C$($X$,$Y$,$Z$,$T$)")
    #ax.set_zlim(0,1)
        
    #make colorbar
    colorbar_ticks=np.linspace(0,1,11)
    cbar=plt.colorbar(p,ticks=colorbar_ticks)

    cbar.set_label('$c$', labelpad=30,rotation=0)
    #save picture as name by n
    name=Path_to_save_images+"figure"+str(n)+".png"
    plt.savefig(name)
    plt.close()
    #return name of the saved figure
    return name
    
#function for iterating
def make_N_4d_figures(N,DT,Path_to_data,Path_to_save_images,every_nth_term):
    plt.style.use('own_plot_style_4d.mplstyle') #use own style
    #make table for image names
    images=[]
    

    #Make n figures
    for n in range(0,N+1,every_nth_term): #every 50th data plotted
        
        
        filename=Path_to_data+"3D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        if(n==0):
            size=len(data[0])
        
        #make x- and y and z-coordinates to tables
        X = np.arange(0, size*0.01, 0.01)
        Y = np.arange(0, size*0.01, 0.01)
        Z = np.arange(0, size*0.01, 0.01)
        #make grid
        X, Y, Z = np.meshgrid(X, Y, Z, indexing="ij")
    
        density_matrix = np.sqrt(X**2 + Y**2 + Z**2)
        

        #iterate x (i) and y (j) and z (k)
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    density_matrix[i][j][k]=data[j*size+i][k] #There is "size" -number lines in one y value
                
                
        #make figure
        images.append(make_4d_figure(n,density_matrix,DT,False,Path_to_save_images,size))
    return images
