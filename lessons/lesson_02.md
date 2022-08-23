# Lesson 2: Simple data types, variable assignment, functions, and modules #

 In programming language terminology, Python in this case, an "expression" is an instruction that combines values and operators (and functions) and always evaluates down to a new value. An expression is opposed to a "statement" that is just a standalone instruction that the Python interpreter can excute. When you type a statement on the command line, Python executes it and displays the result, if there is one. The result of a print statement is a value.
 
## Lesson 2.1: Simple data types ##

### Data types (simple) ###

| Data Type | Example |
| --- | --- |
| Integer | ... -1, 0, 1 ...|
| Floating-point Number | ... -1.0, 0.0, 1.0 ... |
| String | 'a', 'ab', 'abc' |

#### String manupulation

* `SyntaxError` EOL (end of line), forgot to close the string
```py
>>> 'hello Spock
  File "<stdin>", line 1
    'hello Spock
               ^
SyntaxError: EOL while scanning string literal
```

* Concatenation

```py
>>> 'Kathryn' +  'Janeway'
'KathrynJaneway'
```

* `TypeError` for string concatenation

```py
>>> 'Janeway' + 35
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

* string formatting

```py
>>> 'Janeway %s' % 35
'Janeway 35'

>>> 'Janeway {}'.format(35)

>>> f'Janeway {35}'
'Janeway 35'
```

* f-strings: 'formatted string literals,' f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. The expressions are evaluated at runtime and then formatted using the `__format__` protocol.

```
>>> 'Kathryn'*5
'KathrynKathrynKathrynKathrynKathryn'

>>> 'Kathryn'*'Spock'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'

>>> 'Kathryn'*5.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```

## Lesson 2.2: Variable Assignment ##

* variable: a value assigned a label

```py
>>> spock = 50 # initialize variable
>>> spock
50
>>> janeway = 35
>>> spock + janeway 
85
>>> spock + janeway + janeway
135
>>> spock = spock + 5 # assign new value to variable (old is  overwritten)
>>> spock
55
```

* overwrite string

```py
>>> captain = 'Kirk'
>>> captain
'Kirk'
>>> captain = 'Piccard'
>>> captain
Piccard
```

### Valid variable names

* one word with no spaces
* only use letters, numbers and underscore
* cannot begin with number

| Valid | Invalid |
| :--- | :--- |
| snake_case | snake-case |
| camelBack | camel back |
| wnumber23 | 23wnumber |
| _23 | 23 |
| TOTAL_SUM | TOTAL_$UM |
| hello | 'hello' |

## Lesson 2.3: Functions ##

Create a simple function that takes no input and prints hello (in Klingon)

```py
def hello():
  """
    Print hello in Klingon
    """
    print('nuqneH!')
    print('nuqneH!!!')
    print('Hello there.')

hello()
hello()
hello()
```

* Dependency, install `playsound`

```sh
pip install playsound
```

* say hello


```py
from playsound import playsound
def say_hello():
  """
    Say hello in klingon
    """
    playsound('audio.mp3')

say_hello()
say_hello()
say_hello()
```

* Purpose of a function is to group code in order to re-use it multiple times.
* DRY: _Do not Repeat Yourself_ you should always minimize repetitions, that is, avoid duplicating code. Never use `ctrl+c` or `cmd+c`

### `def` statements with parameters ###

The general form of a function in Python is

```py
def function_name(parameters):
    """docstring"""
    statement(s)
```

A value passed to a function is called an _argument_, e.g., `len(some_list)`. Functions have _parameters_ that you pass arguments to, that is, an argument is stored as a parameter of the function.

```py
def hello(name):
    print(f'Hello {name}')

hello('Spock')
hello('Uhura')
```

Notice that a value stored as a parameter by default only has local score, that is, the variable `name` is forgotten after program execution


```py
def play_file(audiofile):
    """
    Play audio file

    Paramters:
        - audiofile: str, filename (path to)
    """
    playsound(audiofile)

play_file('audio.mp3')
```

#### Define, Call, Pass, Argument, Parameter ####

* _define_ a function is when you create it (a function is just a type of object in Python) (function definition)
  * `def` statements define functions
* you _call_ a function when you use is (function call)
* a value passed to a function call is an _argument_ (function external)
* a value is assigned to function as a _parameter_ (function internal)

### Return values and `return` statements ###

most functions have return values when called

* return values are specified with the return statement that uses the `return` keyword followed by the expression to be returned

Make script `comments.py`

```py
import random

def tweet_comment(state): # define function
    if state == 1:
        comment = 'This. Is concerning.'
    elif state == 2:
        comment = 'TAKE NO MORE'
    elif state == 3:
        comment = 'So gosh darn amazing!'
    elif state == 4:
        comment = "Do you think Ninja's sneak up on their family  members just for fun?"

    return comment

i = random.randint(1,4) # create variable to be passed as argument
tweet = tweet_comment(i) # function call, i is assigned to parameter state
print(tweet) # print return value
```

and in a single liner (don't do this)

```py
print(tweet_comment(random.randint(1,4)))
```

### The `None` value ###

The `None` keyword is used to define the null value in Python. It is not an empty string, False, or a zero, but a instance of the `NoneType` object. `None` can be assigned to a variable to reset it/reset it to an empty state.

* all functions need to evaluate to a return value and `None` is used as return value in cases where there is no return

```py
>>> hello = print('Hello!!!')
Hello!!!
>>> None == hello
True
```

Or with your custom functions

```py
>>> def xequals1():
...     x = 1
...
>>> y = xequals1()
>>> None == y
True
```

### Function arguments ###

* function arguments can be identified by _position_ (positional arguments) or _keyword_ (keyword arguments)
* _Positional arguments_ are arguments that can be called by their position in the function definition
* _Keyword arguments_ are arguments that can be called by their name.
* _Required arguments_ are arguments that must passed to the function.
* _Optional arguments_ are argument that can be not passed to the function. In python optional arguments are arguments that have a default value

```py
def additive(x, y, z = 1):          # a & b required, c optional
    return x + y * z

res = additive(1, 2)                # positional and default
res = additive(1, 2, 3)             # positional
res = additive(z = 5, y = 2, x = 2) # named
res = additive(y = 2, x = 2)        # named and default
res = additive(5, z = 2, y = 1)     # positional and named
res = additive(8, y = 0)            # positional, named, and default
```

Example with `print()`

```py
print('Hello', end='') # positional and named
print('World')
>>> print('1', '2', '3')
1 2 3
>>> print('1', '2', '3', sep='o')
1o2o3
```

BUT

```py
>>> print(sep='o','1', '2', '3')
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

### Local and global variable scope ###

In programming, the scope of the variable is the regions of a program that define the visibility of variable.

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/scope.png?raw=true" alt="variable scope" width="800"/> |
|:--:|
| *The scope of a variable (i.e., a binding between a name such as 'x' and a value such as 'Local Scope') is the part of your program where the variable is valid (i.e., where the name can be used to refer to the value)* |


* _Local variables_ parameters and variables assigned to a called function has _local scope_ in the function by default. 
* _Global variables_ variables that exists outside functions have a global scope
* one global scope (your program), a local scope is created whenever a function is called. When the function reaches its return statement, its scope stops

Impact of scope

* code in global scope cannot use local variables
* code in local scope can access global variables
* code in a function's local scipe cannot use variables in any other local scope
* the same variable name can be used in different scopes for different variables

```py
def hello(name = None):
    print(f'Hello {name}')# name has local scope

name = 'Kathryn'# global scope
hello(name = name)
```

Python has four scopes, built-in (not in example code), global, enclosing (for embedded functions), and local


```py
x = 'Global Scope'
print(x)

def outer_func():
    x = 'Enclosing scope'
    print(x)

    def inner_func():
        x = 'Local scope'
        print(x)

    inner_func()
    print(x)

outer_func()
print(x)
```

#### Local variables are NOT in global scope ####

```py
def hello():
    name = 'Kathryn'
hello()
print(name)
```

will give you a `NameError`, why? Because `name` is only in local scope

### Local variables are only local to one context ###

```py
def hello():
    name = 'Kathryn'
    nuqneH()
    print(name)

def nuqneH():
    name = 'Worf'

hello()
```

### Global variables are in the scope of local variables ###

```py
def hello():
    print(name)

name = 'Kathryn'
hello()
print(name)
```

#### local and global variable can have same name ####

```py
def hello():
    name = 'Kathryn'
    print(f'{name} local')     # local scope

def nuqneH():
    name = 'Worf'
    print(f'{name} local')
    hello()
    print(f'{name} local')

name = 'Picard'
nuqneH()
print(f'{name} global')
```

### `global` statment ###

* allows you to modify a global variable locally

```py
def hello():
    global name
    name = 'Kathryn'

name = 'Worf'
hello()
print(name)
```

Four scope rules

1. a variable used in global scope is always a global variable
2. with a global statement in a function, a variable becomes global
3. if a variable is used in an assignment statement in the function, it is a local variable
4. if not used in an assignment statement, it is a global variable 

### Exception handling ###

To avoid that your program crashes due to an error/exception, you need to detact and handle errors - _exception handling_

`zero_divide.py`

```py
def divide_by(denominator):
    return 23 / denominator

print(divide_by(3))
print(divide_by(5))
print(divide_by(0))
print(divide_by(1))
```

```sh
7.666666666666667
4.6
Traceback (most recent call last):
  File "script.py", line 6, in <module>
    print(divide_by(0))
  File "script.py", line 2, in divide_by
    return 23 / denominator
ZeroDivisionError: division by zero
```

Dividing by zeros results in a program-breaking error

Use `try-except` clauses to catch exceptions

```py
def divide_by(denominator):
    try:
     return 23 / denominator
    except ZeroDivisionError:
        print('[ERROR] Invalid Argument... ')

print(divide_by(3))
print(divide_by(5))
print(divide_by(0))
print(divide_by(1))
```

```sh
7.666666666666667
4.6
[ERROR] Invalid Argument...
None
23.0
```

## Lesson 2.4: Modules ##

* If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.
* A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable \__name\__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:
* Modularization reduces software complexity and facilitates re-usability
* NB: Global variables reduces the modularity and flexibility of the program! You avoid global variable by passing variables to function arguments.

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/modular.png?raw=true" alt="modularization" width="800"/> |
|:--:|
| *Modular programming breaks the code into parts that can be shared across projects and modified independently* |

Create a file called `fibo.py` and add two functions that write and return Fibonacci series up to $n$ respectively.

```py
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Import and execute the two functions from the module `fibo`

```py
>>> import fibo
>>> fibo.fib(1000)
>>> fibo.fib2(100)
```

Modules allow you to import and use other scientists' code

```py
# load modules
import seaborn as sns
import matplotlib.pyplot as plt

# set color and style parameters of the plot
sns.set_palette('rocket')
sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})

# read data
data = sns.load_dataset('iris')

# plot data
plt.figure(figsize=(10,8), dpi= 150)
sns.pairplot(data, kind='reg', hue='species')
plt.show()
```

If the module is not installed you can use `pip` or `conda`

```bash
$ pip install --user seaborn
# or
$ conda install -c anaconda seaborn
```