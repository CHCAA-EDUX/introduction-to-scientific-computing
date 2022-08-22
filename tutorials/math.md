# Python math: The Complete Guide #

To use the math in Python, import the module using import math statements in your program. After that, you can call any method of that module. In Python, some mathematical operations can be performed easily in the math module.

## Most Used Python Math Functions ##

1. `fabs()`: It returns the absolute value of x.
2. `ceil()`: It returns the smallest integer value greater than or equal to x.
3. `floor()`: It returns the largest integer less than or equal to x.
4. `factorial()`: It returns the factorial of x.
5. `gcd()`: This function is used to compute the greatest common divisor of 2 numbers mentioned in its arguments.


## Python `math` ##

Python math is a built-in standard module used to work with complex scientific calculations. Mathematical functions like evaluating complex mathematical operations, such as trigonometric operations, logarithmic operations, etc., are under the math module. However, the math module does not support complex data types. For that, you can use the cmath module as the complex counterpart.

Let’s take some examples of the Math module.

```py
import math

data = 21.6
print(f'The floor of 21.6 is: {math.floor(data)}')
```

The `floor()` function returns the __highest integer value smaller than the number__. If the number is already the integer, then the same number is returned.

Let’s see the value of PI.

```py
import math

print(f'The value of PI: {math.pi}')
```

## `math.pow` ##

The math.pow() is a built-in Python library function that returns the value of x to the power of y ($x^y$). To calculate the power in Python, use the math.pow() function. Python offers to compute the power of a number and hence can make calculating the power easier.

### Syntax ###

```py
pow(x,y,z)
```

### Arguments ###

The `pow()` method returns the value of x to the power of y ($x^y$).

| parameter | meaning |
| - | - |
| x | A number, the base |
| y | A number, the exponent |

```py
import math

print(math.pow(2, 3))
```

## `ceil()` ##

The `ceil()` function returns the __smallest integer value greater than the number__. If the number is already an integer, then the same number is returned. 

The method __ceil()__ returns the ceiling value of x -- the smallest integer, which is not less than x.

```py
import math

data = 21.6
print(math.ceil(21.6))
```

More examples

```py
import math

number = -21.19

print(f'The given number is: {number}')
print(f'Floor value is: {math.floor(number)}')# -22
print(f'Ceiling value is: {math.ceil(number)}')# -21
print(f'Absolute value is: {math.fabs(number)}')# 21.19
```

##  `math.log()` ##

The `math.log()` is a built-in Python method that returns the natural logarithm of a number, or the logarithm of a number to base. Let’s see an example of the Python Math exp() and log() functions.

```py
import math

number = 1e-4
print(f'The given number (x) is: {number}')# 0.0001
print(f'e^x (using exp() function) is: {math.exp(number)-1}')#  0.0001000050001667141
print(f'log(fabs(x), base) is: {math.log(math.fabs(number), 10)}')# -3.999999999999999
```

## Python math trigonometric functions ##

All the trigonometric functions are available in python math module, so you can easily calculate them using `sin()`, `cos()`, `tan()`, `acos()`, `asin()`, `atan()` etc functions.

Also, you can convert angles from degree to radian and radian to degree. See the example code.

```py
import math

angleInDegree = 90
angleInRadian = math.radians(angleInDegree)

print(f'The given angle is: {angleInRadian}')
print(f'sin(x) is: {angleInRadian}')
print(f'cos(x) is: {angleInRadian}')
print(f'tan(x) is: {angleInRadian}')
```