# Lesson 4: Visualization \# 1 #

### Learning outcomes ###

* Data visulization with Python.
* Plot simple and multiple graphs in a single figure.
3. Use `seaborn` to make publication-ready graphs

While tabular data formats (see Lesson 3) are good for storing and manipulating heterogenous 2d data, they do not facilitate deep understanding of data. Data visualization is a powerful tool to better understand the properties of our data, it allows us to expose patterns, correlations, and trends that cannot be obtained when data is in a table or dataframe, or, as the mathematician Richard Hamming once said, 'the purpose of computing is insight, not numbers,' and data visualization is one of the best ways to develop that insight. With Python we can use several data visualization modules (ex. `matplotlib`, `seaborn`, `plotly`, `bokeh`) to create complex visualizations both for data understanding and communication.

## Lesson 4.1: Data visulization with Python and `matplotlib` ##

[source](https://swcarpentry.github.io/python-novice-inflammation/03-matplotlib/index.html)

In this lesson we will use `numpy` arrays, in case you need a refresher see [lesson 3.2](link-here).

Python does not have an official plotting library, but if there was one, it would be `matplotlib`. `matplotlib` is a comprehensive library for creating static, animated, and interactive visualizations in Python. [Here](https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png) is an excellent cheat sheet for `matplotlib` in case your rote learning resources are getting depleted.

### Visualizing data

Start by reading data

```py
import numpy
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
```

Let us start by visualizing the matrix as a 'heatmap' with `imshow()` from `matplotlib.pyplot`. `imshow()`  is used to display data as an image, i.e,. on a 2D regular raster.


```py
import matplotlib.pyplot
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
```

| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/inflammation-01-imshow.svg" alt="heatmap" width="800"/> |
|:--:|
| *Each row in the heat map corresponds to a patient in the clinical trial dataset, and each column corresponds to a day in the dataset. Blue pixels in this heat map represent low values, while yellow pixels represent high values. As we can see, the general number of inflammation flare-ups for the patients rises and falls over a 40-day period.* |

* the patients take their medication once their inflammation flare-ups begin
* it takes around 3 weeks for the medication to take effect and begin reducing flare-ups
* and flare-ups appear to drop to zero by the end of the clinical trial.

Plot the average inflammation rate over time

```py
ave_inflammation = numpy.mean(data, axis = 0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()
```

We generated a plot of the average inflammation pr. day across all patients in the variable `ave_inflammation`, then used `matplotlib.pyplot` to create a line graph of those values. The result shows a linear rise and fall. We should however check other statistics than the average of a dataset.

Plot the maximum inflammation rate over time

```py
max_plot = matplotlib.pyplot.plot(numpy.max(data, axis=0))
matplotlib.pyplot.show()
```

and the minimum

```py
min_plot = matplotlib.pyplot.plot(numpy.min(data, axis=0))
matplotlib.pyplot.show()
```

The maximum value rises and falls linearly, while the minimum seems to be a step function. Neither trend seems particularly likely, so either there’s a mistake in our calculations or something is wrong with our data. This insight would have been difficult to reach by examining the numbers themselves without visualization tools.

#### Grouping plots ####

You can group similar plots in a single figure using subplots. This script below uses a number of new commands. The function `matplotlib.pyplot.figure()` creates a space into which we will place all of our plots. The parameter `figsize` tells Python how big to make this space. Each subplot is placed into the figure using its `add_subplot` method. The `add_subplot` method takes 3 parameters. The first denotes how many total rows of subplots there are, the second parameter refers to the total number of subplot columns, and the final parameter denotes which subplot your variable is referencing (left-to-right, top-to-bottom). Each subplot is stored in a different variable (`axes1`, `axes2`, `axes3`). Once a subplot is created, the axes can be titled using the `set_xlabel()` command (or `set_ylabel()`). Here are our three plots side by side:

```py
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname = 'inflammation-01.csv', delimiter = ',')

fig = matplotlib.pyplot.figure(figsize = (10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis = 0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis = 0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis = 0))

fig.tight_layout()

matplotlib.pyplot.savefig('inflammation.png')
matplotlib.pyplot.show()
```

The call to `loadtxt` reads our data, and the rest of the program tells the plotting library how large we want the figure to be, that we’re creating three subplots, what to draw for each one, and that we want a tight layout. (If we leave out that call to `fig.tight_layout()`, the graphs will actually be squeezed together more closely.)

The call to `savefig` stores the plot as a graphics file. This can be a convenient way to store your plots for use in other documents, web pages etc. The graphics format is automatically determined by Matplotlib from the file name ending we specify; here PNG from 'inflammation.png'. Matplotlib supports many different graphics formats, including SVG, PDF, and JPEG.

> **_Importing libraries with shortcuts:_** In this lesson we use the `import matplotlib.pyplot` syntax to import the pyplot module of `matplotlib`. However, shortcuts such as `import matplotlib.pyplot as plt` are frequently used. Importing pyplot this way means that after the initial import, rather than writing `matplotlib.pyplot.plot(...)`, you can now write `plt.plot(...)`. Another common convention is to use the shortcut `import numpy as np` when importing the NumPy library. We then can write `np.loadtxt(...)` instead of `numpy.loadtxt(...)`, for example. Some people prefer these shortcuts as it is quicker to type and results in shorter lines of code - especially for libraries with long names! You will frequently see Python code online using a pyplot function with plt, or a NumPy function with np, and it's because they've used this shortcut. It makes no difference which approach you choose to take, but you must be consistent as if you use `import matplotlib.pyplot as plt` then `matplotlib.pyplot.plot(...)` will not work, and you must use `plt.plot(...)` instead. Because of this, when working with other people it is important you agree on how libraries are imported.

## Lesson 4.2: Data Visualiation with `seaborn` ##
[source](https://www.kaggle.com/code/xinyiye123/data-visualization-with-matplotlib-and-seaborn)

In this lesson, we explore the Spotify data set from [lesson 3](link-here).

Start by reading the data into a dataframe with `pandas`

```py
import pandas as pd

df = pd.read_csv('spotify_2017.dat')
print(df.head())
```

Notice that the first column is irrelevant to our task, let us delete (`drop`) it.

```py
df.drop(df.columns[0], axis=1, inplace=True)
```

Create a _histogram_ with four attributes from Spotify: Danceability, Energy, Liveness and Acousticness. 

> **_Historgram:_** A histogram is an approximate representation of the distribution of numerical data. It is used to summarize discrete or continuous data that are measured on an interval scale. It is often used to illustrate the major features of the distribution of the data in a convenient form. The term was first introduced by Karl Pearson. To construct a histogram, the first step is to 'bin' the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent and are often (but not required to be) of equal size.


First, we create a figure 'canvas' with four subplots corresponding to our four attributes, and add labels to global axis with `text`.

```py
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 1, figsize=(9, 9), sharex=True, dpi=150)
fig.text(0.5, 0.04, 'Score', ha='center',size=20)
fig.text(0.04, 0.5, 'Number', va='center', rotation='vertical',size=20)
```

Notice that our `axs` (axis) object is actually a `numpy` 1d array with four columns 

Second, add the histograms and subplot titles

```py
axs[0].hist(df['danceability'])
axs[0].set_title('Danceability')
axs[1].hist(df['energy'])
axs[1].set_title('Energy')
axs[2].hist(df['liveness'])
axs[2].set_title('Liveness')
axs[3].hist(df['acousticness'])
axs[3].set_title('Acousticness')
```

Lastly, we add a centered global title, show and save the figure

```py
fig.suptitle('What Makes Good Music Good?',size=20)
plt.savefig('spotify_histogram.png')
plt.show()
```

It turns out people are looking for danceability and energy, and the less acoustics and live the song is, the more popular it might be.

We tend to think that high tempo (> BMPs) is more upbeat, but is that actually the case. Use a scatter plot to inspect correctaions between `tempo` and upbeat attributes: `Danceability`, `Energy`, `Liveness` and `Acousticness`.

> **_Scatter Plot:_** A scatter plot is a type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data.

```py
fig, axs = plt.subplots(4, 1, figsize=(9, 9), sharex=True, dpi=150)
fig.text(0.5, 0.04, 'Tempo(BPM)', ha='center',size=20)   
```

Notice that we specify the _Dots per inch_ this time, which specifies the number of individual dots that can be placed in a line within the span of 1 inch. More dots means more better resolution. In academic papers, 150-300 DPIs are typically considered publication standard.

Add the scatter plot

```py
axs[0].scatter(df['tempo'], df['danceability'])
axs[0].set_title('Danceability')
axs[1].scatter(df['tempo'], df['energy'])
axs[1].set_title('Energy')
axs[2].scatter(df['tempo'], df['liveness'])
axs[2].set_title('Liveness')
axs[3].scatter(df['tempo'], df['acousticness'])
axs[3].set_title('Acousticness')
```

And show and save the scatter plot

```py
fig.suptitle('Higher BPM = More Upbeat?',size=20)
plt.savefig('bmp_correlations.png')
plt.show()
```

Suprisingly there is no correlation between those `tempo` and the upbeat attributess

Finally, we can use high-level libraries that build on `matplotlib` to create publication-ready graphs. `seaborn` is a Python data visualization library based on `matplotlib` that provides a high-level interface for drawing attractive and informative statistical graphics. In other words, `seaborn` makes it easier to create fancy graphs with `matplotlib`.

Create a heatmap of the correlations between all attributes in our dataframe

```py
import seaborn as sns
corr = df.corr()
ax = plt.figure(figsize=(12,10), dpi=300)
sns.heatmap(corr,annot=True,xticklabels=corr.columns.values,yticklabels=corr.columns.values)
plt.title("Correlation of Song Attributes",size=15)
plt.tight_layout()
plt.savefig('attributes_heatmap.png')
plt.show()
```

Notice that we use `tight_layout()` to adjust the padding between and around plots.


We end by building a scatter plot matrix that plots the pairwise relationships for nine attributes

```py
df_9attrib = df[['danceability','energy','liveness',
             'acousticness','loudness','speechiness',
             'valence','tempo','duration_ms']]
ax1 = plt.figure(dpi = 300)
sns.pairplot(df_9attrib, kind = 'reg', plot_kws={'line_kws':{'color':'red'}})
plt.title("Pairplot of Song Attributes",size=15)
plt.tight_layout()
plt.savefig('attributes_splom.png')
plt.show()
```

Here we add a regression line using the `reg` parameter and color it red with the keyword argument `plot_kws`.