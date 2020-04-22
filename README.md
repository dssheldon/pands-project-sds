# Programming and Scripting - Project 2020

## Project Plan

- Download the Iris.csv file from the UC Irvine Machine Learning Repository: Iris data set. http://archive.ics.uci.edu/ml/datasets/Iris as instructed in the project instructions.
- Research plotting via matplotlib and seaborn to supplement knowledge in lecture
- Research the Iris data set and analysis completed by others
- Research making a Markdown Readme file (https://commonmark.org/help/tutorial/)
- Research the use of pandas in order to extract the data as required
- Research and write the code which extracts the information about the variables to a text file
- Research and write the code for the plots
- Sources used for this project included:
  - Lecture videos and notes
  - Real Python's Python Plotting With Matplotlib (Guide) <https://realpython.com/python-matplotlib-guide/>
  - Datacamp.com
  - Youtube videos – Corey Schafer and others
  - Books – Python Crash course (Eric Matthews), A Whirlwind tour of python etc.

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

*Scatter plots*

These are used to plot data points on a horizontal and a vertical axis in order to show how much one variable is affected by another. The relationship between the variables is called their correlation. Correlation between variables gives us the ability to predict the value of one variable when the value of a highly correlated variable is known. Various analyses have shown that a scatter plots between almost all variables of the Iris flower, users are able to separate the Iris-Setosa from the other two species

*Histogram*

A histogram plots the frequency of a certain numerical attribute of the data. It is used to determine the distribution of a dataset.

Some interesting observations from using histograms on the Iris data by others is as follow:

- The overall distribution, petal length and petal width does not have a normal distribution, whereas sepal length and sepal width are uniformly distributed.
- The distribution of Iris-Setosa petal is completely different from the other 2 species
- Using sepal length and sepal width, we can’t separate one species from another as the distribution is overlapping
- Iris-Setosa is not normally distributed by sepal length and petal width
- Petal length can be used as a differentiating factor in terms of the distribution of the 3 flower species.

*Heat map with correlation*

Heat maps are another visual plot to see the correlation between two variables. The conclusions reached will be very similar to the scatter plots above.

*Box Plot*

A box plot is a way of summarizing a set of data measured on an interval scale. The ends of the box are the upper and lower quartiles, so the box spans the interquartile range and the median is marked by a vertical line inside the box. The whiskers provide the information whether the data is positive or negatively skewed by looking at the distribution of the data with respect to its median.  The boxplot provides us with information on outliers. 

Box plot analysis on the Iris dataset show that the Sepal Length for Virginica and Sepal Width of Setosa both have outliers while all the other boxplots looked perfectly balanced, we can see that that petal width for both Setosa and Versicolor are positively skewed as the median lie at the lower end of the boxplot.

*Violin Plots*

Violin plots are similar to Box Plot but with a rotated plot on each side, giving more information about the density estimate on the y-axis. The density is mirrored and flipped over and the resulting shape is filled in, creating an image resembling a violin. The advantage of a violin plot is that it can show nuances in the distribution that aren’t perceptible in a boxplot. On the other hand, the boxplot more clearly shows the outliers in the data