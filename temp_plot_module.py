# Sheldon D'Souza
# This is a temporary module to code in the plots required by the assignment
# It will be merged with the analysis.py

# importing in the modules which will be needed for this program
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Answer 3.1 - Output a summary of each variable to a single text file

# open the Iris csv file and added header rows 
# researched how to add headers https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
 
iris_data = pd.read_csv('iris.csv', names = ["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width","Species"])

#create variables for later use to generate useful attributes about the data
i_sl = "Sepal_Length"
i_sw = "Sepal_Width"
i_pl = "Petal_Length"
i_pw = "Petal_Width"
i_sp = "Species"
i_vir = "Iris-virginica"
i_seto = "Iris-setosa"
i_vc = "Iris-versicolor"

l_petalandsepals = [i_sl, i_sw, i_pl,i_pw] #generate a list of variables to loop over to generate mean, median and std
l_species = [i_vir, i_vc, i_seto] # generated a list of classes
#======================================================================================================================

# Researched  https://realpython.com/python-matplotlib-guide/
# Used https://matplotlib.org/3.1.1/gallery/statistics/hist.html as well

# Will try to use the statless rather than stateful interface

# Idea from https://www.datacamp.com/community/tutorials/histograms-matplotlib but generated own code 

for petalandsepal in l_petalandsepals:
    for specie in l_species:
        plt.hist((iris_data.loc[iris_data[i_sp] == specie,petalandsepal]), bins='auto')
        plt.title(specie+petalandsepal)
        #plt.savefig(specie+petalandsepal)
        plt.show() #used temporarily and will be replace by savefig above.
        plt.cla()