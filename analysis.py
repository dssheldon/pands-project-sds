# Sheldon D'Souza
# Programming and Scripting - Project 2020
# This is the code relating to the project. It supplements and is supplemented by the Readme.md file

# importing in the modules which will be needed for this program
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# open the csv file and added header rows # researched how to add headers from https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
 
iris_data = pd.read_csv('iris.csv', names = ["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width","Species"
])

#create variables for later use to generate useful attributes about the data
i_sl = "Sepal_Length"
i_sw = "Sepal_Width"
i_pl = "Petal_Length"
i_pw = "Petal_Width"
i_sp = "Species"
i_vir = "Iris-virginica"
i_seto = "Iris-setosa"
i_vc = "Iris-versicolor"


# Create a text file by using the open function with a+ attribute

# my_textfile = open("VariableOutput.txt","a+")

# print summary of each variable to a single text file - initally printing to screen
# used the pandas tutorial on Real Python for some of the code used below to summarise attributes of the variables

print("The variables within the dataset are as follows:")
[print(x) for x in iris_data.columns.values] # iterated over the of column values using comprehension
print()

print("The number of records for each class of the Iris flowers is as follows:")
f_count_virg = iris_data.loc[iris_data[i_sp] == i_vir,i_sp].value_counts()
print(f_count_virg.to_string()) # used this to remove the printing of "Name and dtype" at the end of the value_counts() function (https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/)

f_count_seto = iris_data.loc[iris_data[i_sp] == i_seto,i_sp].value_counts()
print(f_count_seto.to_string())

f_count_versi = iris_data.loc[iris_data[i_sp] == i_vc,i_sp].value_counts()
print(f_count_versi.to_string())
print()

print("Useful information about the data is as follow:")
print()

l_petalandsepals = [i_sl, i_sw, i_pl,i_pw] #generate a list to loop over to generate mean, median and std
l_species = [i_vir, i_vc, i_seto]
for petalandsepal in l_petalandsepals:
    for specie in l_species:
        print("The mean of the",petalandsepal, "for the", specie, "is:", round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].mean(),2))
        print("The median of the",petalandsepal, "for the", specie, "is:", round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].median(),2))
        print("The standard deviation of the",petalandsepal, "for the", specie, "is:", round(iris_data.loc[iris_data[i_sp] == specie,petalandsepal].std(),2))
        print()


print("The shape of the iris.csv file is ",iris_data.shape)
print()

print("The following summary is generated using the describe function of pandas:")
print()
print(iris_data.describe()) # using pandas to output a summary of the data