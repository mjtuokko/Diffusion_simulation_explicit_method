#import used libraries
import numpy as np
from matplotlib import pyplot as plt
import os

#Not used in main programs. Used manually
def compare_several_datas():
    folder="Results/"
    list_of_results = os.listdir(folder)
    print(list_of_results)
    fig = plt.figure(figsize=(20, 12), dpi=80)
    ax = plt.axes()
    ax.set_yscale('log')
    list_of_results.sort()
    for sub_folder in list_of_results:
        #    print(sub_folder)
        print(sub_folder)
        c=[]
        c_analytical=[]
        T=[]

        Path_to_data_folder=folder + sub_folder + "/1D_data/"
        Path_to_analytical_data_folder=folder + sub_folder + "/1D_analytical_data/" 
        #Find files in one results
    #    list_of_data_files = os.listdir(Path_to_data_folder)
    #    list_of_analytical_data_files = os.listdir(Path_to_analytical_data_folder)
    #    print(list_of_analytical_data_files)
    #    print(list_of_data_files)
        #Both of those has similarly named data files
    #    data=np.loadtxt(new_folder_path + "1D_data.txt")
    #    c=data
        print(Path_to_data_folder + "parameters.txt")
        parameters=np.loadtxt(Path_to_data_folder + "parameters.txt")
        print(parameters)
        DX=parameters[0]
        DT=parameters[1]
        data_files= os.listdir(Path_to_data_folder)
    #    print(DX)
        for n in range(len(data_files)-2):
            #add numerical value to the list
            filename=Path_to_data_folder+"1D_data_"+str(n)+".txt"
            data=np.loadtxt(filename)
            value=data[5]
            c.append(value)
            
            #add analytical value to the list
            filename=Path_to_analytical_data_folder +"1D_data_"+str(n)+".txt"
            data=np.loadtxt(filename)
            value=data[5]
            c_analytical.append(value)
            T.append(DT*n)

            
        zipped = zip( T,c) #zip lists
        tuples = zip(*sorted(zipped)) #make tuplse
        T,c = [ list(tuple) for tuple in  tuples] #divide to two list
        #make_analytical_c_to_calculate_error
        T_analytical = T
        #sort lists logically
        zipped = zip(T_analytical,c_analytical) #zip lists
        tuples = zip(*sorted(zipped)) #make tuplse
        T_analytical,c_analytical = [ list(tuple) for tuple in  tuples] #divide to two list        
        #calculate errorvalues
        c_error=[]
        for i in range(len(T)):
            c_error.append(abs((100*(c_analytical[i]-c[i])/c_analytical[i])))
       #     if(c_analytical[i]-c[i])>0:
       #         print("+")
       #     else:
       #         print("-")
        plt.style.use('own_plot_style2.mplstyle')
        plt.plot(T,c_error,'--', label="$\Delta X$=%.3g" %DX + ", $\Delta T$=%.3g" %DT , linewidth=3, markersize=3)
     #   print(c_error)
       # plt.plot(T,c_analytical,"--", label="Analytical: $\Delta X$=%.3g" %DX + ", $\Delta T$=%.3g" %DT , linewidth=1, markersize=3)
    plt.grid()
    plt.xlim(0, 0.2)
 #   plt.ylim(0,1.5)
    plt.legend(bbox_to_anchor=(1.12, 1.12))
    plt.ylabel(r"$\dfrac{\left|c_{analyyttinen}-c_{numeerinen}\right|}{c_{analyyttinen}} \times 100$ %")
    plt.xlabel("T")
 #   plt.title("Numeerisen ratkaisun virhe")
 #   plt.show()
    plt.savefig("Comparing_4d_v3.png")
  #  plt.show()
    plt.close()
        
    return list_of_results
        

compare_several_datas()
