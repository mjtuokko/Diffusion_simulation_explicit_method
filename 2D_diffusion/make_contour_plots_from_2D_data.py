#import used libraries
import numpy as np
from matplotlib import pyplot as plt






'''function for making the 1st z value. Have to make in first time like this
and no matter which is the value, because it will be overwritten immediately''' 
def z_add_to_grid(x,y):
        return 0*x-0*y
    


#Function to make 2d figure(n,X,Y,Z), nth figure and coordinates in parameters
def make_contour_figure(n,X,Y,Z,DT,title_shown,Path_to_save_images):
    T=n*DT #Time
    #make picture and customize layout
    #customize font
    customized_font = {'weight' : 'normal', 'size'   : 19}
    plt.rc('font', **customized_font)
    #Create and customize figure
    fig=plt.figure(figsize=(10,10))
    ax = plt.axes(xlim=(0, 1), ylim=(0, 1))
    ax.set_aspect('equal')
    zlimits = np.linspace(0,1,100)
    colorbar_ticks=np.linspace(0,1,11)
    img=ax.contourf(X, Y, Z, 101,levels=zlimits, cmap='hot')

    cbar=plt.colorbar(img,ticks=colorbar_ticks)
    cbar.set_label('$c$', labelpad=30,rotation=0)
    xaxis=[0,0.2,0.4,0.6,0.8,1]
    plt.xticks(xaxis,xaxis)
    plt.yticks(xaxis,xaxis)
    ax.set_xlabel('X')
    ax.set_ylabel('Y',rotation=0)
    ax.yaxis.set_label_coords(-0.1,0.45)
    #Time shown in title if wanted
    if(title_shown):
        plt.title("$c$($T$=%.5g" %T +")")
    else: 
        plt.title("$c$($X$,$Y$,$T$)")
    #save picture as name by n
    name=Path_to_save_images+"figure"+str(n)+".png"
    plt.savefig(name)
    plt.close()
    #return name of the saved figure
    return name
    
#function for iterating
def make_N_contour_figures(N,DT,Path_to_data,Path_to_save_images,every_nth_save):
    plt.style.use('own_plot_style.mplstyle') #use own style
    
    #make table for image names
    images=[]
    


    #Make n figures
    for n in range(0,N,every_nth_save): #every nth data plotted
        filename=Path_to_data+"2D_data_"+str(n)+".txt"
        #read data
        data = np.loadtxt(filename)
        if(n==0):
            
            size=int(len(data[0]))

        #make x- and y-coordinates to tables
        x = np.linspace(0, 1, size)
        y = np.linspace(0, 1, size)
        #make grid
        X, Y = np.meshgrid(x, y)
        #make variable Z to the z-axis value in the grid
        #Add Z variable to the grid
        Z = z_add_to_grid(X, Y)


        #iterate x (i) and y (j)
        for i in range(size):
            for j in range(size):
                #make new z values
                Z[i][j]=data[i][j]
                #i (x's index) row and j'th element there. #Make n figures
        #make figure
        images.append(make_contour_figure(n,X,Y,Z,DT,True,Path_to_save_images))
    return images
    
    
    
