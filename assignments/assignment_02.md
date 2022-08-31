# Introduction to Scientific Programming: Assignment 2 #

Assignment 2 tests your understanding of procedural programming with functions, repetitive execution with loops, and plotting with Python. Your answers should consist of the code for solving the problems and a step-wise explanation of how and why you have chosen to implement the solution as you have. We suggest that you use a notebook or a heavily commented script.

## 1. Reverse a list ##

__Task__:  Create a function that takes a list as input and returns the list in reverse order.

Example of input and output:

```py
>>> lst = [1, 1, 2, 3, 5, 8]
>>> res = reverser(lst)
>>> print(res)
[8, 5, 3, 2, 1, 1]
```

## 2. Nested lists ##

__Task__: Take the following nested list (or list of lists) 

```py
>>> enterprise = [['Kirk', 'Spock', 'Uhura'],
     ['Jaeger', 'Kelso', 'McCoy'],
     ['Masters', 'Preston', 'Ross']]
```

and create a function that returns a _flat list_:

```py
['Kirk', 'Spock', 'Uhura', 'Jaeger', 'Kelso', 'McCoy', 'Masters', 'Preston', 'Ross']
```

## 3. Pairplot ##

__Task__ Read the following columns from `world-happiness-report-2021.dat` into a `pandas` dataframe: 

* _Regional indicator_
* _Ladder score_
* _Logged GDP per capita_
* _Healthy life expectancy_
* _Freedom to make life choices_
* _Generosity_
* _Perceptions of corruption_

Extract the data for two regions using the _Regional indicator_  column from the dataframe and create a `pairplot` using `seaborn` that compares the two regions. You can choose any two regions you like, but the resulting plot should look similar to this:

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/figures/assign_02_3.png?raw=true" alt="tabular data" width="800"/> |
|:--:|
| *A `seaborn` `pairplot` for `'Central and Eastern Europe'` and `'Western Europe'` in the `world-happiness-report-2021.dat` data set* |
