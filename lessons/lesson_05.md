# Lesson 5: Loops and Nesting #

[source](https://swcarpentry.github.io/python-novice-inflammation/05-loop/index.html)

### Learning outcomes ###

* Explain what a `for` loop does.
* Correctly write `for` loops to repeat simple calculations.
* Write a for loop to process multiple files.
## Lesson 5.1: Repeat actions over iterables ##

In the previous lesson, we found that our inflammation data (`inflammation-01.csv`), the maximum value rises and falls linearly, while the minimum seems to be a step function. Neither trend seemed particularly likely, so either there's a mistake in our calculations or something is wrong with our data. We have a dozen data sets right now. We want to create plots for all of our data sets with a single statement. To do that, we’ll have to teach the computer how to repeat things.

An example task that we might want to repeat is accessing numbers in a list, which we will do by printing each number on a line of its own.

```py
odd = [1, 3, 5, 7]
```

As you may remember from [lesson 3](https://sdc-moodle.samf.aau.dk/mod/page/view.php?id=24448), a list is an ordered collection of elements, and every element has a unique number associated with it — its index. This means that we can access elements in a list using their indices. For example, we can get the first number in the list `odds`, by using `odds[0]`. One way to `print` each number is to use four print statements.

```py
def four_prints(lst)
    print(lst[0])
    print(lst[1])
    print(lst[2])
    print(lst[3])

four_prints(odd)
```


This approach is problematic however, because:

* __Not scalable__. Imagine you need to print a list that has hundreds of elements. It might be easier to type them in manually.
* __Difficult to maintain__. If we want to decorate each printed element with an asterisk or any other character, we would have to change four lines of code. While this might not be a problem for small lists, it would definitely be a problem for longer ones.
* __Fragile__. If we use it with a list that has more elements than what we initially envisioned, it will only display part of the list’s elements. A shorter list, on the other hand, will cause an error because it will be trying to display elements of the list that do not exist.

For example, if we modify the input list and call our function

```py
odds = [1, 3, 5]
four_prints(odd)
```

it will get an `IndexError` that is raised when the index of a sequence is out of range.

A better approach will apply a `for` loop:

```py
odds = [1, 3, 5, 7]

for num in odds:
    print(num)
```

or as a function

```py

def n_prints(lst):
    for num in lst:
        print(num)
```

This is shorter — certainly shorter than something that prints every number in a hundred-number list - and more robust as well

```py
odds = [1, 3, 5, 7, 9, 11]
n_prints(odds)
```

Our improved solutino uses a for loop to repeat an operation — in this case, printing — once for each thing in a sequence. The general form of a loop is

```py
for variable in collection:
    # do things using variable, such as print
```

| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/05-loops_image_num.png" alt="for loop" width="400"/> |
|:--:|
| *Using the odds example above, the loop might look like this where each number (num) in the variable odds is looped through and printed one number after another. The other numbers in the diagram denote which loop cycle the number was printed in (1 being the first loop cycle, and 6 being the final loop cycle).* |

We can call the loop variable anything we like, but there must be a colon at the end of the line starting the loop, and we must indent anything we want to run inside the loop. Unlike many other languages, there is no command to signify the end of the loop body (e.g. `end for`); what is indented after the `for` statement belongs to the loop.

 > **_A loop:_** In computer programming, a loop is a sequence of instruction s that is continually repeated until a certain condition is reached. Typically, a certain process is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number.


| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/for-loop.png?raw=true" alt="for loop" width="400"/> |
|:--:|
| *General structure of a standard `for` loop in Python* |



### Naming the loop variable ###

In the example the _loop variable_ was named `num` a mnemonic for 'number'. Just as with variables, you can name loop variables whatever you want.

```py
odds = [1, 3, 5, 7, 9, 11]

for banana in odds:
    print(banana)
```

It is a good idea to choose variable names that are meaningful, otherwise it would be more difficult to understand what the loop is doing.

### Updating a Variable Repeatably ###

```py
length = 0
names = ['Curie', 'Darwin', 'Turing']
for value in names:
    length = length + 1

print(f'There are {length} names in the list.')
```

Note that a loop variable is a variable that is being used to record progress in a loop. It still exists after the loop is over, and we can re-use variables previously defined as loop variables as well

```py
name = 'Rosalind'

for name in ['Curie', 'Darwin', 'Turing']:
    print(name)
print(f'after the loop, name is {name}')
```

Note also that finding the length of an object is such a common operation that Python actually has a built-in function to do it called `len()`

```py
print(len([0, 1, 2, 3]))
```

`len()` is much faster than any function we could write ourselves, and much easier to read than a two-line loop; it will also give us the length of many other things that we haven’t met yet, so we should always use it when we can.

## Lesson 5.2: Visualize Data from Multiple Files ##

As a final piece to processing our inflammation data, we need a way to get a list of all the files in our data directory whose names start with inflammation- and end with .csv. The `glob` library can help here

```py
import glob
```

The `glob` library contains a function, also called `glob`, that finds files and directories whose names match a pattern. We provide those patterns as strings: the character `*` matches zero or more characters, while `?` matches any one character. We can use this to get the names of all the CSV files in the current directory.

```py
print(glob.glob('inflammation*.csv'))
```

As these examples show, `glob.glob`’s result is a list of file and directory paths in arbitrary order. This means we can loop over it to do something with each filename in turn. In our case, the “something” we want to do is generate a set of plots for each file in our inflammation dataset.

If we want to start by analyzing just the first three files in alphabetical order, we can use the `sorted` built-in function to generate a new sorted list from the `glob.glob` output:

```py
import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('inflammation*.csv'))
filenames = filenames[0:3]

for filename in filenames:
    print(filename)

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    plt.show()
```

| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/03-loop_49_1.png" alt="inflammation01" width="600"/> |
|:--:|
| *`inflammation-01.csv`* |


| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/03-loop_49_3.png" alt="inflammation2" width="600"/> |
|:--:|
| *`inflammation-02.csv`* |


| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/03-loop_49_5.png" alt="inflammation" width="600"/> |
|:--:|
| *`inflammation-03.csv`* |

The plots generated for the second file, `inflammation-02.csv`, look very similar to the plots for the first file, `inflammation-01.csv`: their average plots show similar 'noisy' rises and falls; their maxima plots show exactly the same linear rise and fall; and their minima plots show similar staircase structures.

The third dataset, `inflammation-03.csv`, shows much noisier average and maxima plots that are far less suspicious than the first two datasets, however the minima plot shows that the third dataset minima is consistently zero across every day of the trial. If we produce a heat map for the third data file we see the following:

| <img src="https://swcarpentry.github.io/python-novice-inflammation/fig/inflammation-03-imshow.svg" width="600"/> |
|:--:|
| *`inflammation-03.csv`* |

We can see that there are zero values sporadically distributed across all patients and days of the clinical trial, suggesting that there were potential issues with data collection throughout the trial. In addition, we can see that the last patient in the study didn’t have any inflammation flare-ups at all throughout the trial, suggesting that they may not even suffer from arthritis.

The datasets appear to fall into two categories:

1. seemingly 'ideal' datasets that display suspicious maxima and minima (such as inflammation-01.csv and inflammation-02.csv)
2. 'noisy' datasets that show concerning data collection issues such as sporadic missing values and even an unsuitable candidate making it into the clinical trial.