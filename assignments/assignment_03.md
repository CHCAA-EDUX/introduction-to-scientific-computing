# Introduction to Scientific Programming: Assignment 3 #

## 1. Temperature measurement ##

__Task__: create a function, `temp_tranform()`, that transforms temperature measured in Celsius to Fahrenheit and Fahrenheit to Celcius depending on an argument. The relationship between Fahrenheit to Celcius is  

$$ F^{\circ} = \frac{9}{5} C^{\circ} + 32$$

## 2. The sigmoid function ##

__Task__: The sigmoid (or logistic) function is an S-shaped function that is normalized between 0 and 1. It is defined as

$$s(x) = \frac{1}{1+e^{-x}}$$

Implement the function and visualize the output in range -10 to 10 in steps of 0.1.

You can confirm that your function works on the following example:

Input and output example:

```py
>>> print(s(0))
0.5
>>> print(s(2))
0.88079
>>> print(s(100))
1.0
```

## 3.  Non-linear Polynomial Fit ##

__Task__: Plot the following `x` and `y` variables in a 2d plot

```py
x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
```

Use the `polyfit()` function from `numpy` to create and plot a linear and a non-linear polynomial fit in the same figure, but with different colors. If you are adventurous, you _can_ (but you do not have to) use `curve_fit()` from the `scipy.optimize` module. 