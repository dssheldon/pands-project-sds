# Programming and Scripting - Project 2020

## Project Plan

- Download the Iris.csv file from the UC Irvine Machine Learning Repository: Iris data set. http://archive.ics.uci.edu/ml/datasets/Iris as instructed in the project instructions
- Research plotting via matplotlib and seaborn to supplement knowledge in lecture
- Research the Iris data set and analysis completed by others
- Research making a Markdown Readme file (https://commonmark.org/help/tutorial/)
- Research the use of pandas in order to extract the data as required
- Research and write the code which extracts the information about the variables to a text file
- Research and write the code for the plots
- Create separate modules for the text output and the plots and merged them once they work
- Sources used for this project included:
  - Lecture videos and notes
  - Real Python's Python Plotting With Matplotlib (Guide) <https://realpython.com/python-matplotlib-guide/>
  - Matplotlib.org
  - Datacamp.com
  - Youtube videos – Corey Schafer and others
  - Books – Python Crash course (Eric Matthews), A Whirlwind tour of python etc.
  - Stackoverflow.com
  - Geeksforgeeks.org
  - Medium.com

## File List

This repository contains the following core files:

- Analysis.py - main python program
- iris.csv - Iris dataset
- Readme.md - This file
- License - Standard MIT license
- gitignore - created for python

Other files created as outputs from the program:

- VariableOutput.txt - Text file created by the program
- PNG files - outputs of plots saved as images

## Running the program

The program is run by running the analysis.py file. The file is a python program and uses the python libraries mentioned in the 'General' section below.

## Analysis of the Iris Dataset

### The Iris Dataset

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

The dataset contains a set of 150 records under five attributes - petal length, petal width, sepal length, sepal width and species. (https://en.wikipedia.org/wiki/Iris_flower_data_set)

This is perhaps the best-known database to be found in the pattern recognition literature. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. This data in the UCI repository differs from the data presented in Fishers article as the 35th sample and 38th sample have been corrected. (https://archive.ics.uci.edu/ml/datasets/iris)

It is a standard an inbuilt dataset in many languages such as Python (scikit-learn) and R.

### Use of the Dataset

The dataset has been used extensively in the field of machine learning and data analytics. The symmetry of the dataset compounded with the inherent complexity makes it ideal as a starting point for students looking to undertake analysis of the dataset as well as development of code to explore this dataset. The main challenge undertaken by students undertaking machine learning is building a model to classify the flower into the correct species based on the four data attributes and the relationships between them. The main way to do this is to create a decision tree that will sort the flower into its species. However, a major part of doing this is analysing the data visually using various plots. A concise and well thought though exploration of the data is therefore the first step to achieve many data science related objectives.

### Analysis that others have undertaken using the dataset

(Used various sources, however quoted “https://rpubs.com/AjinkyaUC/Iris_DataSet” within this section)

As mentioned above the Iris dataset is one of the most popular datasets currently and various people, ranging from experts to students/beginners have undertaken various degrees and depths of analysis of the data for various purposes. I have summarised some of these analyses here. I have also replicated some of this analysis taking some of the ideas from others but writing my own code for the plots.

#### *Scatter plots*

These are used to plot data points on a horizontal and a vertical axis in order to show how much one variable is affected by another. The relationship between the variables is called their correlation. Correlation between variables gives us the ability to predict the value of one variable when the value of a highly correlated variable is known. Various analyses have shown that a scatter plots between almost all variables of the Iris flower, users are able to separate the Iris-Setosa from the other two species.

#### *Histogram*

A histogram plots the frequency of a certain numerical attribute of the data. It is used to determine the distribution of a dataset.

Some interesting observations from using histograms on the Iris data by others are as follow:

- The overall distribution, petal length and petal width does not have a normal distribution, whereas sepal length and sepal width are uniformly distributed
- The distribution of Iris-Setosa petal is completely different from the other 2 species
- Using sepal length and sepal width, we can’t separate one species from another as the distribution is overlapping
- Iris-Setosa is not normally distributed by sepal length and petal width
- Petal length can be used as a differentiating factor in terms of the distribution of the 3 flower species.

#### *Heat map with correlation*

Heat maps are another visual plot to see the correlation between two variables. The conclusions reached will be very similar to the scatter plots above.

#### *Box Plot*

A box plot is a way of summarizing a set of data measured on an interval scale. The ends of the box are the upper and lower quartiles, so the box spans the interquartile range and the median is marked by a vertical line inside the box. The whiskers provide the information whether the data is positive or negatively skewed by looking at the distribution of the data with respect to its median.  The boxplot provides us with information on outliers. 

Box plot analysis on the Iris dataset show that the Sepal Length for Virginica and Sepal Width of Setosa both have outliers while all the other boxplots looked perfectly balanced, we can see that that petal width for both Setosa and Versicolor are positively skewed as the median lie at the lower end of the boxplot.

#### *Violin Plots*

Violin plots are similar to Box Plot but with a rotated plot on each side, giving more information about the density estimate on the y-axis. The density is mirrored and flipped over and the resulting shape is filled in, creating an image resembling a violin. The advantage of a violin plot is that it can show nuances in the distribution that aren’t perceptible in a boxplot. On the other hand, the boxplot more clearly shows the outliers in the data.

## Downloading the Dataset

Downloaded the dataset from: https://archive.ics.uci.edu/ml/datasets/iris



##  ANALYSIS.PY

### <u>General</u>

#### *Preparing the data for use*

The pandas module within python was used to aggregate the data for tasks. I added headings to the dataset by using the names argument of the pandas read_csv method (researched from stackoverflow.com) as I did not want to modify the dataset permanently. For ease of use I created variables for the abbreviated names for each of the headers and the species. I created two lists; l_petalandsepals and l_species; one for the headers and one for the species of iris flowers. These lists were used to automate the generation of charts and writing efficient code.

#### *Import libraries*

Imported the following libraries to use during the course of the program:

- import matplotlib.pyplot as plt
- import seaborn as sns
- import pandas as pd
- import numpy as np
- import itertools as it
- import matplotlib.colors as mcolors 
- import random

#### *Using the .loc method*

Used the loc method within Pandas to access a group of rows and columns. The main purpose of this was to access the column data of the variables segregated by Species. I used this throughout the program for both writing to the text file and for the plots.

 

### <u>Writing a Summary of variables to a text file</u>

I created a text file by using the “with open” command with the ‘a’ argument to allow data to be appended to the file.

I then generated the following outputs to the text file. I used the print function to generate the output in order to check for correctness before amending the code to append to the file:

#### *Names of variables within the dataset*

The names of the variables were the title of each of the column (header) names. I did this by using a for loop and list comprehension to iterate over list of headers created earlier i.e. l_petalandsepals. I then iterated over the l_species list to get the names of the species (I indented these under the variable ‘Species’).

#### *Number of records for each class*

Used the loc method to return the value data for each species and the value_counts method to generate a count for each species. The count function returned “Name and dtype (data type)” as well and so used the virg.to_string() function to remove this extra data. (Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/)

#### *Others useful information about the dataset*

##### *Mean, median and standard deviation*

The objective of this is to output the mean, median and standard deviation of each of the variable broken down by its respective species.

I achieved through the use of the loc method described above and nested ‘for’ loops. This section took a considerable amount of time and research to pull together. The overall idea is mine, as is the code written. I solved complex aspects of the code and problems by researching various sources, which have been listed in the ‘Project Plan’ section of this Readme.

I used nested for loops to iterate through the l_petalandsepals and l_species lists. Using the loc method I returned the data for each of the variables segregated by species. I then used the mean, median and standard deviation (std) functions to generate this information for the data returned by the for loops. I rounded the data to 2 decimal places and generated narratives (text) to precede the data in order to give it context.

##### *Pandas ‘Shape’*

I used [dataset].shape within Pandas to output the shape of the data.

##### *Pandas ‘Describe’*

Used the [dataset].describe() method to output a standard pandas library summary of the data.



### <u>**Creating Plots**</u>

#### *Histograms*

Used nested for loops to iterate through the l_petalandsepals and l_species lists. Used the loc method to return the data for each of the variables segregated by species. Created a histogram for each variable segregated by species. Selected the bin size as ‘auto’ and adjusted the width of the bins for viewing ease. 

Each histogram plot generated has a separate colour. I achieved this by importing matplotlib.colors library. I then created a list of the ‘Tableau Colors’ from the library and named the list plot_colors. I then used random.choice from the random library to choose a random color from the plot_colors for the historgram being plotted.

The plot title is generated by using the instance returned by the for loops. The species name and the variable name from is generated from the l_specie and l_petalandsepals lists respectively. The x and y axis titles are also generated from these lists.

I added vertical grid lines to the plot and set the ‘alpha’ value to increase the transparency of the grid lines to an appropriate level for ease of viewing.

I applied the tight_layout() method to the plots.

Finally, I used savefig to save the plots as png file. I used the specie name and the variable name followed by the type of plot (as a string) for the file name of each plot (e.g. Iris_Setosa Petal_Length – Histogram). I used the ‘+’ function to concatenate the variable names and the strings to form the file name. This ensured that each iteration of the plot had a unique name and could be saved accordingly.

I cleared the axes using the cla() function so that each historgram saved correctly to file.

#### *Scatter Plots*

The objective was to generate the scatter plots for each pair of variables within the dataset.

I started by importing the ‘itertools’ library. I used the combination method within itertools to generate a list (iris_data_combos) of combinations of each pair of variables (as tuples) within the dataset. I used combinations for this dataset, as the scatterplot of A,B is the same as the scatterplot of B,A.

I set the fig size to adequately size the scatter plots.

I used a ‘for’ loop to iterate through the list of tuples. Using the variables generated from the ‘for’ loop, I plotted a scatterplot. I used the loc method to obtain the data for each species and assigned a colour to each species within the plot. I then plotted the data for each species onto the same scatteplot; for each pair of variables.

I added the x and y labels by generating these from the for loop. I added the legend to be generated from the from the list of species l_species. I also set the location of the legend and the font size of the legend by using the loc and {prop} arguments within the legend method.

I added a title to the plots and also applied the tight_layout() method to the plots.

Finally, I used savefig to save the plots as png file. I used the specie name and the names of the pairs of variables (generated by the for loop), followed by the type of plot (as a string) for the file name of each plot (e.g. Iris_Setosa Sepal_Length vs Petal_Length – Scatter Plot). I used the ‘+’ function to concatenate the variable names and the strings to form the file name. This ensured that each iteration of the plot had a unique name and could be saved accordingly.

The end result is that each pair of variables has been plotted as a scatter plot with the data clearly broken up and colour coded as per species.

####  *Other Interesting Analysis*

As mentioned in the ‘Use of dataset’ section above, there is a lot of other interesting analyses that has been done on the dataset. As an optional exercise I plotted some of these analyses. I have discussed these in the sections below. I imported Seaborn as I used this library for these plots.

##### Heatmap

This is another plot type apart from scatterplots to show the correlation between two variables. I used the heatmap within Seaborn to plot this. I set the annotation argument to True (which displayed the correlation value on the heatmap) and used the colour map (cmap) argument to set the heatmap colour.

I used the ‘ylim’ function to set the vertical limit of the plot as the top boxes of the heatmap were initially being cut-off. This seems to be an issue with the heatmap plot within seaborn, but was corrected using the ylim function.

I applied the tight_layout() method to the plots. I set the title for the plot and used savefig to save the plot as a png file.

##### Pairplots

The pairplot function within seaborn, plots a pairplot for all pairs of variables in the dataset onto one figure. I used this function to draw the plot and used the ‘hue’ argument to set the legend (which was the species column within the dataset). 

I used the subplot_adjust method to adjust the top of the plot, as initially, the title of the plot was not appearing where it should and therefore did not apply the tight_layout() method to this plot.

I added  "super title" for the entire figure using the suptitle() menthod. I used savefig to save the plot as a png file.

##### Box Plots and Violin Plots

As mentioned above, the box plots and violin plots are useful to see the distribution of data within a dataset. I used Seaborn to plot the box and violin plots.

I created a figure, set the figsize and created four axes (subplots) on the figure. I used a ‘for’ loop to create the subplots using the seaborn boxplot and violinplot functions. The ‘for’ loop iterates through two lists simultaneously (using the zip function). The first list contains the range function which outputs numbers from one to four [i.e. range(1,5)]. The iteration through the first list was used to specify the subplot. The iteration through the second list plotted the boxplot or violinplot by passing the values of the second list to the boxplot or violinplot function within Seaborn. Both plots took the species (x-axis), variables from l_petalandsepals (y-axis) and the dataset (data) arguments.

I added a title to the plot. I did not apply the tight_layout() method to the plots as this caused the title on the plot to be misplaced. Instead I used the subplot_adjust method to adjust the top of the plot (as done in the seaborn pairplot above) and wspace argument to increase the space within the subplots.

I used savefig to save the plot as a png file.