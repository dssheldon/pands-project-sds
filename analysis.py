# Sheldon D'Souza
# Programming and Scripting - Project 2020
# This is the code relating to the project. It supplements and is supplemented by the Readme.md file


#======================================================================================================================================

#Importing in the modules which will be needed for this program

#======================================================================================================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import itertools as it # researched itertools as a way to generate comboinations for two sets of variables to use them in a loop in order to automate generating the scatter diagrams (below)
import matplotlib.colors as mcolors # imported to generate colours for plots
import random # imported to randomise the colours for plots

#======================================================================================================================================

# GENERAL SECTION OF CODE (FOR BOTH MODULES)

#======================================================================================================================================

# open the Iris csv file and added header rows 

iris_data = pd.read_csv('iris.csv', names = ["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width","Species"])

#create variables for later use to generate useful attributes about the data and writing efficent code
i_sl = "Sepal_Length"
i_sw = "Sepal_Width"
i_pl = "Petal_Length"
i_pw = "Petal_Width"
i_sp = "Species"
i_vir = "Iris-virginica"
i_seto = "Iris-setosa"
i_vc = "Iris-versicolor"

l_petalandsepals = [i_sl, i_sw, i_pl,i_pw] #generate a list of variables to use for various analysis and operations
l_species = [i_vir, i_vc, i_seto] # generated a list of classes

plot_colors = list(mcolors.TABLEAU_COLORS) # generated a list of colours from which random colours will be selected for plots


#=========================================================================================================================================

# WRITING SUMMARY OF VARIABLE TO A TEXT FILE - MODULE

#=========================================================================================================================================


# Answer 3.1 - Output a summary of each variable to a single text file

# Create a text file by using the open function with 'w' attribute

with open("VariableOutput.txt","w") as txt_file:

    # APPEND A SUMMARY OF VARIABLES TO THE FILE
    txt_file.write("\n =======================")
    txt_file.write("\n | SUMMARY OF VARIABLES |") # File heading
    txt_file.write("\n =======================")
    txt_file.write('\n\n\n')

    # Extract and append a the names of all variables used in the dataset
    # Appended the headers for each of the columns and the species names, by iterating over the two lists created at the start of the program
    txt_file.write("\nThe variables within the dataset are as follows:")
    txt_file.write("\n------------------------------------------------")
    [txt_file.write(f"\n{x}") for x in iris_data.columns.values] # iterated over the of column values using list comprehension
    [txt_file.write(f"\n - {y}") for y in l_species]
    txt_file.write('\n\n')


    # Generated and appended to the file, the number of records by each specie
    # Obtained the "number of records" by using the .loc method from the pandas library (Reference: Real Python - Pandas Tutorial )

    txt_file.write("\nThe number of records for each class of the Iris flowers is as follows:")
    txt_file.write("\n-----------------------------------------------------------------------")

    f_count_virg = iris_data.loc[iris_data[i_sp] == i_vir,i_sp].value_counts() # used value_counts() method to generate the "number of records" for the specified data subset
    txt_file.write(f"\n\t {f_count_virg.to_string()}") # used this to remove the printing of "Name and dtype" at the end of the value_counts() function (https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/)

    f_count_seto = iris_data.loc[iris_data[i_sp] == i_seto,i_sp].value_counts()
    txt_file.write(f"\n\t {f_count_seto.to_string()}")

    f_count_versi = iris_data.loc[iris_data[i_sp] == i_vc,i_sp].value_counts()
    txt_file.write(f"\n\t {f_count_versi.to_string()}")
    txt_file.write('\n\n')

    # Generated Other Useful information about the data

    txt_file.write("\nUseful information about the data is as follow:")
    txt_file.write("\n-----------------------------------------------\n")
    
    # Used for loops to iterate  through the lists of variables of "petals and sepals" measurements and "Species" 
    #    Used the .loc method in Pandas to obtain the specifc data for each class
    #       The end result is to generate the mean, median and std for each variable broken down by class of iris flower
    #           using the  mean/median/std methods
    for petalandsepal in l_petalandsepals:
        for specie in l_species:
            txt_file.write(f"\nThe mean of the {petalandsepal} for the {specie} is: ----> {round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].mean(),2)}")
            txt_file.write(f"\nThe median of the {petalandsepal} for the {specie} is: ----> {round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].median(),2)}")
            txt_file.write(f"\nThe standard deviation of the {petalandsepal} for the {specie} is: ---> {round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].std(),2)}")
            txt_file.write("\n")

    # Generated the shape of the dataset using the shape method within pandas

    txt_file.write("\n\nShape of the Dataset")
    txt_file.write("\n--------------------")

    txt_file.write(f"\nThe shape (r,c - number of rows and columns) of the iris.csv file is {iris_data.shape}")
    txt_file.write('\n\n')

    # Generated a summary of the data using the describe() method within pandas

    txt_file.write("\nSummary of Data - Pandas Describe function")
    txt_file.write("\n------------------------------------------\n")

    txt_file.write("\nThe following summary is generated using the describe function of pandas:")
    txt_file.write("\n")
    txt_file.write(f"\n{round(iris_data.describe(),2)}") # using pandas to output a summary of the data

#========================================================================================================================================

# PLOTTING MODULE

#========================================================================================================================================


# Qs. 3.2 - Saving a HISTOGRAM of the variables

# Used the for loop as above (for the text file) to generate the data for the histograms
# Plotted the histograms for each variable by Species type
# Generated a random colour within the matplotlib.colors TABLEAU colour list
# Set the title, labels and set the gridlines for the plot
fig, ax = plt.subplots()
for petalandsepal in l_petalandsepals: 
    for specie in l_species:
        ax.hist((iris_data.loc[iris_data[i_sp] == specie,petalandsepal]), bins='auto', rwidth=0.95, color=random.choice(plot_colors))
        ax.set_title(specie.upper()+" "+ petalandsepal.upper())
        ax.set_xlabel("Size of "+petalandsepal.title())
        ax.set_ylabel(petalandsepal.title() + " Count")
        ax.grid(axis='y', alpha=0.25)
        fig.tight_layout()
        fig.savefig(specie.title()+" "+petalandsepal.title()+ "- Histogram")
        ax.cla() # clear the axes for next plot


# Qs. 3.3 - Saving SCATTER PLOTS of pairs of variables

# Created a list of combinations of each pair of variables using itertools and used a for loop and loc method to generate the required data
# Added labels to each plot

iris_data_combos = list(it.combinations(l_petalandsepals,2)) # used itertools to generate combinations of variables as a list with embeded tuples
# used a for loop to go through each item of the list representing a unique combination (non repeated) of variables to use in the scatter plot

fig1, ax1 = plt.subplots(figsize=(8,8)) #used the stateless approach of matplotlib and added a figure size
for x in iris_data_combos:
    # used the loc method again to extract data relating to each specie of iris flower seperately, giving it a seperate colour
    # plotted scatter plots for each class/specie assigning a different colour to each specie
    ax1.scatter((iris_data.loc[iris_data[i_sp] == i_vir,x[0]]), (iris_data.loc[iris_data[i_sp] == i_vir, x[1]]),color='red')
    ax1.scatter((iris_data.loc[iris_data[i_sp] == i_vc,x[0]]), (iris_data.loc[iris_data[i_sp] == i_vc, x[1]]),color='blue')
    ax1.scatter((iris_data.loc[iris_data[i_sp] == i_seto,x[0]]), (iris_data.loc[iris_data[i_sp] == i_seto, x[1]]),color='green')
    ax1.set_xlabel(x[0].title())
    ax1.set_ylabel(x[1].title())
    ax1.set_title("SCATTER PLOT OF THE PAIRS OF IRIS VARIBLES")
    ax1.legend(l_species, loc='upper left', prop={'size': 12})
    fig1.tight_layout()
    fig1.savefig(specie.title()+" "+x[0].title()+" vs "+x[1].title()+ "- Scatter Plot")
    ax1.cla()

# PLOT OTHER INTERESTING ANALYSIS (Includes heatmap showing correlations, pariplots, box plots and violin plots)
# Used Seaborn to complete these plots   

# Heatmap using SNS
plt.figure(figsize=(8,8))
sns.heatmap(iris_data.corr(),annot=True, cmap="coolwarm")
plt.title("CORRELATION BETWEEN IRIS VARIABLES - HEATMAP")
plt.ylim(4.0, 0) # used to correct the top of the heatmap boxes being cut-off
plt.tight_layout()
plt.savefig("CORRELATION BETWEEN IRIS VARIABLES (HEATMAP) -  SEABORN (Optional Plot)")


# Pairplot using SNS
sns.pairplot(iris_data, hue=i_sp)
plt.suptitle("PAIRPLOTS OF ALL PAIRS OF VARIABLES USING SEABORN")
plt.subplots_adjust(top=0.95)
plt.savefig("PAIRPLOTS OF ALL PAIRS OF VARIABLES - SEABORN (Optional Plot)")


# Box plots using SNS
# Used a for loop to create subplots and then added boxplots for Each variable by Species.
plt.figure(figsize=(10,8))
for i,n in zip(list(range(1,5)),l_petalandsepals): #used "zip" and range to iterate through two variables simultaneously
    plt.subplot(2,2,i) # used 'i' to choose a subplot
    sns.boxplot(x=i_sp,y=n,data=iris_data) # used 'n' to iterate through the list of variables
    plt.suptitle("BOX PLOT OF VARIABLES")  # added a super title for the figure
    plt.subplots_adjust(top=0.95,wspace=0.4) # made adjustments so that the title would fit on the top of the page and set the distance between subplots 
plt.savefig("BOX PLOT OF VARIABLES USING SEABORN (Optional Plot)")

# Violin Plots using SNS
# Used same code as Box plots above
plt.figure(figsize=(10,8))
for i,n in zip(list(range(1,5)),l_petalandsepals):
    plt.subplot(2,2,i)
    sns.violinplot(x=i_sp,y=n,data=iris_data)
    plt.suptitle("VIOLIN PLOT OF VARIABLES")
    plt.subplots_adjust(top=0.90,wspace=0.5)
plt.savefig("VIOLIN PLOT OF VARIABLES USING SEABORN (Optional Plot)")
