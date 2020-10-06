Evolve Rep

# **IMPORTANT!!**

All the exercise used here is done using Jupyter Notebook installed with Conda. Anaconda can work too, but the reason Conda is used here is to save space since Anaconda will pre-install all the library it has. In conda, only the desired library are installed according to the user's needs. 

Refer to the [conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for further information.

For this exercise, it is assumed that:

* Numpy
* Pandas
* Matplotlib

Are already installed.

## Matplotlib Introduction

1. First install all the necessary packages. For efficiency purposes, the installed packages will be called according to the abbreviation below.

```
import numpy as np    #We will call the funtion with np
import pandas as pd   #We will call the function with pd
import matplotlib.pyplot as plt   #We will call the function with plt
```

1a. Lets test the matplotlib package. Start with defining an example variable to put into the plot. In this case we will use the linspace function from numpy package. Try to use other example to put into the variables for the X-axis and the y-axis.

```
X = np.linspace(0,10,10)
y = np.sqrt(X)
```

1b. Now plot the axes using the matplotlib packages. The result should be a blue plotted line
```
fig = plt.figure()
ax = plt.axes()
ax.plot(X, y)

#You can customize the plot figure size using the figsize function. Moreover, you can also change the Y axis and add more lines in the plot using the code below.

fig = plt.figure(figsize=(6, 6))  #You can change it to be higher for example figsize=(10,10) or other than a square
ax = plt.axes()
ax.plot(X, np.sin(X))
ax.plot(X, np.cos(X))

#Alternatively, you can make the code shorter by directly using the matplotlib package.

plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X))    #Use plt.plot instead of ax.plot since the matplotlib package already contains the plotting function.
plt.plot(X, np.cos(X))

#To add more visual detail in the plot, we can change the color by specifying the color code

plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r')   #This will make the line red
plt.plot(X, np.cos(X), 'b')   #This will make the line blue

#We can also change the line style by adding dash or plus sign.

plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r--') #Red dashed line
plt.plot(X, np.cos(X), 'c+-') #Blue oval

#Sometimes the data might go over or shorter than the plotted figure. To limit the axis visualization, we can set the limits using 'xlim' or 'ylim' with the plt function.

plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r')
plt.plot(X, np.cos(X), 'b')
plt.xlim(0,15)    #This will limit the x axis to 15 points only starting from 0
plt.ylim(-2,2)    #This will limit the y axis to 2 points only starting from -2

#We can add more details such as Title and legends to make it easier to intepret.

plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r', linewidth=3, label="sin(x)")    #The label function will add a legend inside the plot.
plt.plot(X, np.cos(X), 'b', markersize=5, label="cos(x)")
plt.xlim(0,15) 
plt.ylim(-2,2)
plt.title("2 Trigonometric Functions)   #This will add a title on top of the plot
plt.xlabel("X")   #This will add a "X" title on the x axis
plt.ylabel("y")   #This will add a "y" title on the y axis
```

### This is a compilation as to some shortcut for line types usable on matplotlib
```
    'b'    #Blue line, marker default
    'ro'   #Red circle line
    'g-'   #Default color, dashed line
    'k^'   #Black triangle
    'c+-'  #Cyan with plus marked with solid line
```

A comprehensive list on the colors used can be found [here!](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html)

2. Now lets start with scatterplot data visualizations! To do this, import the dataset from the "data" folder.
```
sc = pd.read_csv("data/circle_data.csv", sep=';') #This tells panda that the file is separated by a ; instead of a coma (,). Make sure to adjust according to the data.

#You can see some parts of the data using the head() function.

sc.head()
```

2a. We know that there are 3 columns in the data: "x", "y", and "radius". Lets plot the x and y column using a scatter plot.

```
plt.scatter(sc.x, sc.y)
plt.axis('equal')   # Make sure the figure size is equal in size
```

2b. So it is now plotted, but its all blue! It will be easier (and more aesthetic) if we can add more detail.

```
plt.scatter(sc.x, sc.y, c='r')  #This will add a red color to the plot.
plt.axis('equal')

#We can also add a gradient color to the scatterplot.

plt.scatter(sc.x, sc.y, c=sc.radius, s=30, cmap='seismic') #This color is added based on the radius value and the cmap refers to the gradient color type. You can change this accordingly.
plt.axis('equal')
```

3. Now lets make a histogram. 

```
First lets make some random numbers using numpy

numbers = np.random.rand(10000)   #This will make 10000 random numbers using numpy
plt.hist(numbers, bins=25)     #This is the command to plot the histogram
```
