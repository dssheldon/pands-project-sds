# Sheldon D'Souza
# Programming and Scripting - Project 2020
# This is the code relating to the project. It supplements and is supplemented by the Readme.md file

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

l_petalandsepals = [i_sl, i_sw, i_pl,i_pw] #generate a list of variables to use for various analysis and operations
l_species = [i_vir, i_vc, i_seto] # generated a list of classes

# Create a text file by using the open function with a+ attribute

# with open("VariableOutput.txt","a") as txt_file:

# print summary of each variable to a single text file - initally printing to screen
# use myfile.write("appended text") to replace the print function
# used the pandas tutorial on Real Python for some of the code used below to summarise attributes of the variables

# APPEND A SUMMARY OF VARIABLES TO THE FILE
print("SUMMARY OF VARIABLES") # File heading
print('\n')

# Extract and append a the names of all variables used in the dataset
# Appended the headers for each of the columns and the species names, by iterating over the two lists created at the start of the program
print("The variables within the dataset are as follows:")
[print(x) for x in iris_data.columns.values] # iterated over the of column values using list comprehension
[print (' ','-',y) for y in l_species]
print('\n')


# Generated and appended to the file, the number of records by each specie
# Obtained the "number of records" by using the .loc method from the pandas library (Reference: Real Python - Pandas Tutorial )

print("The number of records for each class of the Iris flowers is as follows:")

f_count_virg = iris_data.loc[iris_data[i_sp] == i_vir,i_sp].value_counts() # used value_counts() method to generate the "number of records" for the specified data subset
print(f_count_virg.to_string()) # used this to remove the printing of "Name and dtype" at the end of the value_counts() function (https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/)

f_count_seto = iris_data.loc[iris_data[i_sp] == i_seto,i_sp].value_counts()
print(f_count_seto.to_string())

f_count_versi = iris_data.loc[iris_data[i_sp] == i_vc,i_sp].value_counts()
print(f_count_versi.to_string())
print('\n')

# Generated Other Useful information about the data

print("Useful information about the data is as follow:")
print()

# Used for loopsto iterate  through the lists of variables of "petals and sepals" measurements and "Species" 
#    Used the .loc method in Pandas to obtain the specifc data for each class
#       The end result is to generate the mean, median and std for each variable broken down by class of iris flower
#           using the  mean/median/std methods
for petalandsepal in l_petalandsepals:
    for specie in l_species:
        print("The mean of the",petalandsepal, "for the", specie, "is:", round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].mean(),2))
        print("The median of the",petalandsepal, "for the", specie, "is:", round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].median(),2))
        print("The standard deviation of the",petalandsepal, "for the", specie, "is:", round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].std(),2))
        print()

# Generated the shape of the dataset using the shape method within pandas

print("The shape of the iris.csv file is ",iris_data.shape)
print('\n')

# Generated a summary of the data using the describe() method within pandas

print("The following summary is generated using the describe function of pandas:")
print()
print(iris_data.describe()) # using pandas to output a summary of the data