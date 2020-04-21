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