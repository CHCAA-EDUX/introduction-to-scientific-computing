# Leeson 8: Strings, Dictionaries, and more about Functions #

[source](https://swcarpentry.github.io/python-novice-inflammation/08-func/index.html)


## Working with Strings ##

Remember the string data type `str` from [lesson 2]()? IN Python, strings is a (iterable) sequence of Unicode characters. Python uses unicode today to include every character in all languages and bring uniformity in encoding. Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string. Because strings are arrays, they are iterable and we can loop through the characters in a string, with a `for` loop (see [lesson 5]()).

> **_String Encoding:_** Since Python 3.0, strings are stored as Unicode, i.e. each character in the string is represented by a code point. So, each string is just a sequence of Unicode code points. For efficient storage of these strings, the sequence of code points is converted into a set of bytes. The process is known as encoding. There are various encodings present which treat a string differently. The popular encodings being utf-8, ascii, etc. Using the string `encode()` method, you can convert unicode strings into any encodings supported by Python. By default, Python uses utf-8 encoding.

#### Single or double quotes? ####

Valid string assignment
```py
kirk = 'To boldly go where no man has gone before.'
```

Invalid
```py
picard = 'Things are only impossible until they're not.'
```

Valid
```py
spock = "It is the lot of 'man' to strive no matter how content he is."
```

##### Escape characters #####

Valid
```py
picard = 'Things are only impossible until they\'re not.'

spock = 'It is the lot of \'man\' to strive no matter how content he is.'
```

| Escape character | Result |
| :-: | :-: |
| `\'` | `'`|
| `\"` | `"` |
| `\t` | _Tab_ |
| `\n` | _Newline_ |
| `\\` | `\` |

```py
>>> print("There is a way out of every box, a solution to every puzzle; \n it's just a matter of finding it. \n (Picard)" )
There is a way out of every box, a solution to every puzzle;
it's just a matter of finding it.
(Picard)
```

##### Raw strings #####
* ignores escape characters
```py
>>> print(r'Things are only impossible until they\'re not.')
Things are only impossible until they\'re not.
```
* useful for Win paths and regular expressions

##### Multiline strings #####
* escape characters are optional, BUT may impact your IDE
* docstrings use multiline strings


#### Indexing and Slicing ####
* string is sequence data
* zero indexing again

```py
>>> spock = "Highly illogical."
>>> spock[0]
'H'
>>> spock[5]
'y'
>>> spock[-1]
'.'
>>> spock[0:4]
'High'
>>> spock[:4]
'High'
>>> spock[7:]
'illogical.'
```

#### `in` and `not in` operators for strings ####

* as sequence data, `in` and `no in` work similarly to lists

### String concatenation and interpolation ###

```py
>>> name = 'Janeway'
>>> age = 27
>>> print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
Hello, my name is Janeway. I am 27 years old
>>> print('Hello, my name is %s. I am %d years old.' % (name, age))
Hello, my name is Janeway. I am 27 years old
>>> print('Hello, my name is {}. I am {} years old'.format(name, age))
Hello, my name is Janeway. I am 27 years old
>>> print(f'Hello, my name is {name}. I am {age} years old')
Hello, my name is Janeway. I am 27 years old
```
* f-string string interpolation is easy to read and manipulate
```py
print(f'Hello, my name is {"Kathryn " + name}. I am {age + 8} years old')
```

### String methods ###

```
>>> name = 'Janeway'
>>> print(dir(name))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
#### Casefolding alphabetic characters ####

* casefolding with `upper()` and `lower()`
  * return new string/does not modify existing string var
  * `islower()` and `isupper()` for testing the case of the full string

#### `ìs<feature>()` methods ####

| method | True | False |
| --- | --- | --- |
| `isalpha()` | 'janeway' | 'janeway27' |
| `isalnum()` | 'janeway', '27', 'janeway27' | 'janeway!'|
| `isdecimal()` | '27' | 'janeway' |
| `isspace()` | '  ' | 'janeway'|
| `istitle()` | 'Captain Kathryn Janeway' | 'Janeway is captain' |

Input validation
```py
While True:
  print('Select a new password (letters and numbers only):')
  password = input()
  if password.isalnum():
    break
  print('Passwords can only have letters and numbers.')
```

#### `startswith()` and `endswith()` ####

```py
>>> 'Captain Kathryn Janeway'.startswith('Captain')
True
>>> 'Captain Kathryn Janeway'.endswith('way')
True
>>> 'Janeway'.startswith('Janeway') == 'Janeway'.endswith('Janeway')
True
```

#### `join()` and `split()` ####

* tokenization with `split()`
```py
>>> text = 'Hello my name is Captain James Kirk'
>>> text.split()
['Hello', 'my', 'name', 'is', 'Captain', 'James', 'Kirk']
```

* generate string from list of tokens with `join()`
```py
>>> tokens = ['Hello', 'my', 'name', 'is', 'Captain', 'James', 'Kirk']
>>> " ".join(tokens)
'Hello my name is Captain James Kirk'
```

* interpolation with `split()` and `join()`
```py
>>> name = 'Jean-Luc Piccard'
>>> text = 'Hello my name is Captain James Kirk'
>>> f"{' '.join(text.split()[:-2])} {name}"
```

* sentence tokenization with `split()`
```py
>>> mccoy = "Compassion: that's the one things no machine ever had. Maybe it's the one thing that keeps men ahead of them."
>>> mccoy.split('.')
["Compassion: that's the one things no machine ever had", " Maybe it's the one thing that keeps men ahead of them", '']
```

#### `partition()` ####

* pre-post separator, return substrings in tuple, separator inclusive
* partitioning is not recursive/splits on first occurrence only

```py

before, sep, after = 'James T Kirk'.partition('T')
```

#### `rjust()`, `ljust()`, `center()` ####

* padded string with spaces to justify text

```py
>>> name = 'spock'
>>> name.rjust(10)
'     spock'
>>> name_padded_5 = name.rjust(5)
>>> name_padded_10 = name.rjust(10)
>>> (len(name), len(name_padded_5), len(name_padded_10))
(5, 5, 10)
```

```py
>>> '[Validation Start]'.center(50, '=')
```

* usefull for tables

```py
def print_performance(metrics, leftwidth, rightwidth):
  print('Performance'.center(leftwidth + rightwidth, '-'))
    for (metric, score) in metrics.items():
        print(metric.ljust(leftwidth, '.') + str(score).rjust(rightwidth))

performance_metrics = {'precision': 0.75, 'recall': 0.76, 'f1-score': 0.75 , 'support': 254}
print_performance(performance_metrics, 12, 5)
print()
print_performance(performance_metrics, 20, 6)

---Performance---
precision... 0.75
recall...... 0.76
f1-score.... 0.75
support.....  254

-------Performance--------
precision...........  0.75
recall..............  0.76
f1-score............  0.75
support.............   254
```

#### `strip()`, `rstrip()`, `lstrip()` ####

* strip whitespaces (space, tab, newline)

```py
>>> spock = '     Logic is the beginning of wisdom, not the end.     '
>>> spock.strip()
'Logic is the beginning of wisdom, not the end.'
>>> spock.lstrip()
'Logic is the beginning of wisdom, not the end.     '
>>> print('Highly illogical.\n')
Highly illogical.

>>> print('Highly illogical.\n'.rstrip())
Highly illogical.
```


#### On the safe side ####

The control character (sequence of) that indicates newline (aka. End Of Line, Next Line or line break) depend on your operating system (or the operating system used to generate the file, you are processing). Most systems use or combune Carriage Return (CR) and Line Feed. In typewriters change line requires two axes of motion, _down_ and _across_ respectively, but in software these can be combined into one action CR and LF. Unix and Unix-like operating systems only uses LF for newline with the `\n` escape character, while Windows maintain the full CR LF sequence with the escape sequence `\r\n`. When removing trailing newlines from strings in Python `rstrip('\n')` is normally sufficient, but to be on the safe side you can use the `os.linesep` variable:
```
>>> import os
>>> newline_text = 'Highly illogical.\n'
>>> newline_text.rstrip(os.linesep)
'Highly illogical.'
```

### Numeric values of characters ###
* all information is stored as strings of binary numbers (bytes). Every text character can therefore be converted to a number, a so-called _Unicode code point_
```py
>>> for char in "abc": print(ord(char))
97
98
99
>>> for num in [97, 98, 99]: print(chr(num))
a
b
c
>>> ord('a') < ord('b')
True
>>> chr(ord('a') + 1)
'b'
```

## Dictionaries ##

The dictionary data type `dict` is a mutable collection of values, stored as key-value pairs. Like the list, dictionaries are used to store _collections_ of data and both can be used to store multi-dimensional data.

```py
book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}
```

Unlike lists and `numpy` arrays, dictionaries are unordered

```py
book = {'title': 'Neuromancer', 'author': "Gibson, William" , 'genre': 'Science fiction'}

permuatation = {'genre': 'Science fiction', 'author': "Gibson, William", 'title': 'Neuromancer'}

book == permutation
True
```

But insertion order is remembered since Python 3.7

```py

list(book)
['title', 'author', 'genre']

list(permutation)
['genre', 'author', 'title']
```

Dictionaries is Python's builtin implementation of hash tables, that is, an unordered collection of key-value pairs, where each key is unique. 

* used to implement map and set data structures in most common programming languages.
* offer a combination of efficient lookup, insert and delete operations.
* neither arrays nor linked lists can achieve this

Entering and ordering data with dictionaries (building a simple book-author database)

```py
books = {'Neuromancer': 'Gibson, William', 'VALIS': 'Dick, Phillip K.'}

while True:
    print('Enter a book: (black to quit)')
    title = input()
    if title == '':
        break
    
    if title in books:
        print(f'{title} is written by {books[title]}')
    else:
        print(f'We do not have author information for {title}')
        print(f'Please enter the author of {titile}':)
        author = input()
        books[title] = author
        print('Thank you, the book database is now updated.')
```

NB. you still need to save the database to re-use new entries

Multiple assignment with `items()` method

```py
for (title, author) in books.items():
    print(f'{author} is the author of {title}')

Gibson, William is the author of Neuromancer
Dick, Phillip K is the author of VALIS
```


`setdefault()` method to ensure that a key exists

```py
import pprint
text = 'Cyberspace. A consensual hallucination experienced daily by billions of legitimate operators, in every nation.'

counter = dict()
for char in text:
    counter.setdefault(char, 0)
    counter[char] = counter[char] + 1

pprint.pprint(counter)
```

Nested dictionaries

```py
all_books = {
    'Neuromancer':{'author': 'Gibson, William', 'year': 1984 , 'genre': 'Science fiction' },
    'VALIS': {'author': 'Dick, Phillip K.' , 'year': 1981, 'genre': 'Science fiction' },
    'Schrödingers Cat Trilogy': {'author': 'Wilson, Robert A.' , 'year': 1979, 'genre': 'Science fiction' }
    }

```
## More on Functions: Modularity, Testing and Documenting ##

Once we start putting things in functions in order to re-use them, we need to start testing that those functions are working correctly. Start by writing a function to offset a dataset so that it’s mean value shifts to a user-defined value

Import dependencies

```py
import numpy as np
```

Define the offset function

```py
def offset_mean(data, target_mean_value):
    return (data - np.mean(data)) + target_mean_value
```

We could test this on our actual data, but since we don't know what the values ought to be, it will be hard to tell if the result was correct. Instead, let’s use `numpy` to create a matrix of $0$’s and then offset its values to have a mean value of $3$:

```py
z = np.zeros((2, 2))

print(offset_mean(z, 3))
```

Does the output look right? Now apply it to real-world data

```py
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

print(offset_mean(data, 0))
```

It's hard to tell from the default output whether the result is correct, but there are a few tests that we can run

```py
print(f'original min, mean, and max are: {np.min(data)}, {np.mean(data)}, {np.max(data)}')

offset_data = offset_mean(data, 0)

print(f'min, mean, and max of offset data are:,
      {np.min(offset_data)},
      {np.mean(offset_data)},
      {np.max(offset_data)}')
```

That seems almost right: the original mean was about 6.1, so the lower bound from zero is now about -6.1. The mean of the offset data isn't quite zero, but it’s pretty close. We can even go further and check that the standard deviation hasn’t changed

```py
print(f'std dev before and after: {np.std(data)}, {np.std(offset_data})')
```

Those values look the same, but we probably wouldn’t notice if they were different in the sixth decimal place. Let’s do this instead

```py
print(f'difference in standard deviations before and after: {np.std(data) - np.std(offset_data)}')
```

Again, the difference is very small. It’s still possible that our function is wrong, but it seems unlikely enough that we should probably get back to doing our analysis. We have one more task first: we should write some documentation for our function to remind ourselves later what it’s for and how to use it.

The usual way to put documentation in software is to add comments like this

```py
# offset_mean(data, target_mean_value):
# return a new array containing the original data with its mean offset to match the desired value.
def offset_mean(data, target_mean_value):
    return (data - numpy.mean(data)) + target_mean_value
```

There’s a better way, though. If the first thing in a function is a string that isn’t assigned to a variable, that string is attached to the function as its documentation

```py
def offset_mean(data, target_mean_value):
    """Return a new array containing the original data
       with its mean offset to match the desired value."""
    return (data - np.mean(data)) + target_mean_value
```

This is better because we can now ask Python’s built-in help system to show us the documentation for the function

```py
help(offset_mean)
```

A string like this is called a docstring. We don't need to use triple quotes when we write one, but if we do, we can break the string across multiple lines

```py
def offset_mean(data, target_mean_value):
    """Return a new array containing the original data
       with its mean offset to match the desired value.

    Examples
    --------
    >>> offset_mean([1, 2, 3], 0)
    array([-1.,  0.,  1.])
    """
    return (data - numpy.mean(data)) + target_mean_value

help(offset_mean)
```

### Defining Defaults ###

Remember from from [lesson 2]() when we looked at function arguments? Now we have passed parameters to functions in two ways: directly, as in `type(data)`, and by name, as in `np.loadtxt(fname='something.csv', delimiter=',')`. In fact, we can pass the filename to loadtxt without the `fname=`

```py
np.loadtxt('inflammation-01.csv', delimiter=',')
```

but we still need to say `delimiter=`

```py
np.loadtxt('inflammation-01.csv', ',')
```

To understand what's going on, and make our own functions easier to use, let’s re-define our `offset_mean()` function like this

```py
def offset_mean(data, target_mean_value=0.0):
    """Return a new array containing the original data
       with its mean offset to match the desired value, (0 by default).

    Examples
    --------
    >>> offset_mean([1, 2, 3])
    array([-1.,  0.,  1.])
    """
    return (data - np.mean(data)) + target_mean_value
```

The key change is that the second parameter is now written `target_mean_value = 0.0` instead of just `target_mean_value`. If we call the function with two arguments, it works as it did before

```py
test_data = np.zeros((2, 2))
print(offset_mean(test_data, 3))
```

But we can also now call it with just one parameter, in which case `target_mean_value` is automatically assigned the default value of $0.0$:

```py
more_data = 5 + np.zeros((2, 2))
print('data before mean offset:')
print(more_data)
print('offset data:')
print(offset_mean(more_data))
```

This is handy: if we usually want a function to work one way, but occasionally need it to do something else, we can allow people to pass a parameter when they need to but provide a default to make the normal case easier. The example below shows how Python matches values to parameters

```py
def display(a=1, b=2, c=3):
    print(f'a: {a}', 'b: {b}', 'c: {c}')

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)
```

As this example shows, parameters are matched up from left to right, and any that haven’t been given a value explicitly get their default value. We can override this behavior by naming the value as we pass it in

```py
print('only setting the value of c')

display(c=77)
```

With that in hand, let’s look at the help for `np.loadtxt`

```py
help(np.loadtxt)
```

This tells us that `loadtxt` has one parameter called `fname` that doesn't have a default value, and eight others that do. If we call the function like `np.loadtxt('inflammation-01.csv', ',')`, he filename is assigned to `fname` (which is what we want), but the `delimiter` string `','` is assigned to `dtype` rather than `delimiter`, because `dtype` is the second parameter in the list. However `','` isn't a known `dtype` so our code produced an error message when we tried to run it. When we call `loadtxt` we don't have to provide `fname=` for the filename because it's the first item in the list, but if we want the `','` to be assigned to the variable delimiter, we do have to provide `delimiter=` for the second parameter since `delimiter` is not the second parameter in the list.

More general (from [lesson 2]()),

* function arguments can be identified by _position_ (positional arguments) or _keyword_ (keyword arguments)
* _Positional arguments_ are arguments that can be called by their position in the function definition
* _Keyword arguments_ are arguments that can be called by their name.
* _Required arguments_ are arguments that must passed to the function.
* _Optional arguments_ are argument that can be not passed to the function. In python optional arguments are arguments that have a default value

### Readable functions ###

Consider the following functions

```py
def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return np.sqrt(d / (len(p) - 1))

def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return np.sqrt(sum_squared_devs / (len(sample) - 1))
```

The functions `s` and `std_dev` are computationally equivalent (they both calculate the sample standard deviation), but to a human reader, they look very different. Which one is the easiest to read?

As this example illustrates, both documentation and a programmer's coding style combine to determine how easy it is for others to read and understand the programmer's code. Choosing meaningful variable names and using blank spaces to break the code into logical 'chunks' are helpful techniques for producing readable code. This is useful not only for sharing code with others, but also for the original programmer. If you need to revisit code that you wrote months ago and haven’t thought about since then, you will appreciate the value of readable code!