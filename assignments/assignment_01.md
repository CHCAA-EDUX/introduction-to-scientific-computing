# Introduction to Scientific Programming: Assignment 1 #

Assigment 1 tests your understanding of basic python syntax, procedural programming with functions, and use of `numpy` arrays. our answers should consist of the code for solving a problem and a stepwise explanation of how and why you have chosen to implement the solution as you have. We suggest that you use a notebook and a heavily commented script,

## 1. Basic Math ##
__Task__: Write a function `power_of_y()` that takes two integers as input _x_ and _y_, prints and returns the value of x to the power og y

Example of input and output:

```sh
>>> xy = power_of_y(2, 3)
2 to the power of 3 is 8

>>> print(xy)
8
```

## 2. Data types ##

__Task__: The `len()` function returns the number of items in an iterable object. When the object is a string, the len() function returns the number of characters in the string. Write a function `no_char()` that can take simple data types as input (ex. an integer, a float and string) and return the length of the number of characters in the input.

Example of input and output:

```sh
>>> a = '23'
>>> b = 2
>>> c = 3.0
>>> print(no_char(a))
2
>>> print(no_char(b))
1
>>> print(no_char(c))
3
```


## 3. Matrix manipulation with `numpy` ##

__Task__: Solve the following three subtasks with `numpy`

1. Generate a random 1D array of size 15 and find the mean value of the vector

Example of output:

```py
the mean is 0.4792806543234017
```

2. Generate a 100 x 100 array of random values and find the minimum and maximum values of the array

Example of output:

```py
the minimum is 1.4296695441284868e-05 and maximum 0.9998087405374979
```

3. Generate a 2D array with 1s on the border and 0s inside

Example of output:

```py
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
```