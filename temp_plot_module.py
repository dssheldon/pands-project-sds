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

import itertools as it # researched itertools as a way to generate comboinations for two sets of variables to use them in a loop in order to automate generating the scatter diagrams

#temp = list(it.combinations(l_petalandsepals,2)) # This was the proof of concept to see whether it worked
#print(temp)
#for x in temp:
#    plt.scatter(iris_data[x[0]],iris_data[x[1]])
#    plt.show()
#    #print(x[0],x[1])

iris_data_combos = list(it.combinations(l_petalandsepals,2)) # used itertools to generate combinations of variables as a list with embeded tuples
#print(temp) - check to be removed
# used a for loop to go through each item of the list representing a unique combination (non repeated) of variables to use in the scatter plot
for x in iris_data_combos:
    # used the loc method again to extract data relating to each specie of iris flower seperately, giving it a seperate colour
    # plotted scatter plots for each class/specie assigning a different colour to each specie
    plt.scatter((iris_data.loc[iris_data[i_sp] == i_vir,x[0]]), (iris_data.loc[iris_data[i_sp] == i_vir, x[1]]),color='red')
    plt.scatter((iris_data.loc[iris_data[i_sp] == i_vc,x[0]]), (iris_data.loc[iris_data[i_sp] == i_vc, x[1]]),color='blue')
    plt.scatter((iris_data.loc[iris_data[i_sp] == i_seto,x[0]]), (iris_data.loc[iris_data[i_sp] == i_seto, x[1]]),color='green')
# need to add titles etc.
    plt.show()

