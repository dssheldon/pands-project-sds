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

import itertools as it # researched itertools as a way to generate comboinations for two sets of variables to use them in a loop in order to automate generating the scatter diagrams
import matplotlib.colors as mcolors
import random

plot_colors = list(mcolors.TABLEAU_COLORS) 


# Researched  https://realpython.com/python-matplotlib-guide/
# Used https://matplotlib.org/3.1.1/gallery/statistics/hist.html as well

# Will try to use the statless rather than stateful interface

# Idea of technique of plotting by species from https://www.datacamp.com/community/tutorials/histograms-matplotlib but generated own code 


for petalandsepal in l_petalandsepals:
    for specie in l_species:
        plt.hist((iris_data.loc[iris_data[i_sp] == specie,petalandsepal]), bins='auto', rwidth=0.95, color=random.choice(plot_colors))
        plt.title(specie.upper()+" "+ petalandsepal.upper())
        plt.xlabel("Size of "+petalandsepal.title())
        plt.ylabel(petalandsepal.title() + " Count")
        plt.grid(axis='y', alpha=0.25)
        plt.tight_layout()
        #plt.savefig(specie.title()+" "+petalandsepal.title()+ "- Histogram")
        #plt.show() #used temporarily and will be replace by savefig above.
        #plt.cla()


#temp = list(it.combinations(l_petalandsepals,2)) # This was the proof of concept to see whether it worked
#print(temp)
#for x in temp:
#    plt.scatter(iris_data[x[0]],iris_data[x[1]])
#    plt.show()
#    #print(x[0],x[1])
#print(temp) - check to be removed


iris_data_combos = list(it.combinations(l_petalandsepals,2)) # used itertools to generate combinations of variables as a list with embeded tuples
# used a for loop to go through each item of the list representing a unique combination (non repeated) of variables to use in the scatter plot
for x in iris_data_combos:
    # used the loc method again to extract data relating to each specie of iris flower seperately, giving it a seperate colour
    # plotted scatter plots for each class/specie assigning a different colour to each specie
    plt.figure(figsize=(8,8))
    plt.scatter((iris_data.loc[iris_data[i_sp] == i_vir,x[0]]), (iris_data.loc[iris_data[i_sp] == i_vir, x[1]]),color='red')
    plt.scatter((iris_data.loc[iris_data[i_sp] == i_vc,x[0]]), (iris_data.loc[iris_data[i_sp] == i_vc, x[1]]),color='blue')
    plt.scatter((iris_data.loc[iris_data[i_sp] == i_seto,x[0]]), (iris_data.loc[iris_data[i_sp] == i_seto, x[1]]),color='green')
    plt.xlabel(x[0].title())
    plt.ylabel(x[1].title())
    plt.title("SCATTER PLOT OF THE PAIRS OF IRIS VARIBLES")
    plt.legend(l_species, loc='upper left', prop={'size': 9})
    plt.tight_layout()
    #plt.show()

# need to add titles etc.

# PLOT OTHER INTERESTING ANALYSIS (Includes heatmap showing correlations, pariplots, box plots and violon plots)    

# Correlation plot done by various
plt.figure(figsize=(8,8))
sns.heatmap(iris_data.corr(),annot=True)
plt.title("CORRELATION BETWEEN IRIS VARIABLES - HEATMAP")
plt.ylim(4.0, 0)
plt.tight_layout()
#plt.show()

sns.pairplot(iris_data, hue=i_sp)
plt.suptitle("PAIRPLOTS OF ALL PAIRS OF VARIABLES USING SEABORN")
plt.subplots_adjust(top=0.95)
#plt.tight_layout()
#plt.show()

# Box plots and violin plots anlysis of data done by various 
#   Idea from https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e but code is my own

plt.figure(figsize=(10,8))
for i,n in zip(list(range(1,5)),l_petalandsepals):
    plt.subplot(2,2,i)
    sns.boxplot(x=i_sp,y=n,data=iris_data)
    plt.suptitle("BOX PLOT OF VARIABLES")
    plt.subplots_adjust(top=0.95,wspace=0.4)
    #plt.tight_layout()
plt.show()

plt.figure(figsize=(10,8))
for i,n in zip(list(range(1,5)),l_petalandsepals):
    plt.subplot(2,2,i)
    sns.violinplot(x=i_sp,y=n,data=iris_data)
    plt.suptitle("VIOLIN PLOT OF VARIABLES")
    plt.subplots_adjust(top=0.90,wspace=0.5)
    #plt.tight_layout()
plt.show()
