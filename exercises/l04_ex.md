# Exercises 4 #

## Pair programming ##

This execise focuses on 2D visualization of tabular data. We will use the World Happiness report data from 2021, which contains the rankings of national happiness, based on respondent ratings of their own lives, which the report also correlates with various life factors. The report uses the Cantril ladder instrument to measure happiness, that is, it asks respondents to think of a ladder, with the best possible life for them being a 10 and the worst possible life being a 0. They are then asked to rate their own current lives on that 0 to 10 scale. The rankings are from nationally representative samples for the years 2019-2021.

Extract the following columns from `world-happiness-report-2021.dat`: 

* _Ladder score_
* _Logged GDP per capita_
* _Healthy life expectancy_
* _Freedom to make life choices_
* _Generosity_
* _Perceptions of corruption_

Create a pair plot of six variables and set the font to "Times New Roman", the color cycle/palette to use `matplotlib`'s colormap "bone", and save the figure 300 dots per inch. Make sure that the font size is readable.

Dataframes provide a method called `dataframe.corr()` for computing its correlation matrix. Create a heatmap using the same data and plotting parameters as the pair plot above.

Try to fill the diagonal with zeros in the collelation matrix.

## Check your understanding ##

<br /> 

</details>

<details>
  <summary>1. Modify the following code to display the three plots on top of one another instead of side by side.

```py
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

fig.tight_layout()

plt.pyplot.show()
```
</summary>

```py
fig = plt.figure(figsize=(3.0, 10.0))

axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)
```

</details>

&nbsp;

<br /> 

</details>

<details>
  <summary>2. In the above `inflammation-01.csv` code example, modify the code to include standard deviation (`np.std`) of the inflammation data for each day across all patients - you will need four `axes` objects
</summary>

```py
data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

fig = plt.figure(figsize=(13.0, 3.0))

axes1 = fig.add_subplot(1, 4, 1)
axes2 = fig.add_subplot(1, 4, 2)
axes3 = fig.add_subplot(1, 4, 3)
axes4 = fig.add_subplot(1, 4, 4)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

axes4.set_ylabel('sd')
axes4.plot(np.std(data, axis=0))

fig.tight_layout()

plt.show()
```

</details>

&nbsp;

</details>

<br /> 

<details>
<summary>3. `+` usually means addition, but when used on strings or lists, it means 'concatenate'. Given that, what do you think the multiplication operator `*` does on lists? In particular, what will be the output of the following code? 
  
```py
counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
```

* `[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]`
* `[4, 8, 12, 16, 20]`
* `[[2, 4, 6, 8, 10],[2, 4, 6, 8, 10]]`
* `[2, 4, 6, 8, 10, 4, 8, 12, 16, 20]`

</summary>

* `[2, 4, 6, 8, 10, 2, 4, 6, 8, 10]`

</details>

&nbsp;

## Practice Questions ##

<br /> 

</details>

<details>
  <summary> 1. What does the parameter `figsize=(3.0, 10.0)` in `plt.figure(figsize=(3.0, 10.0))` do?</summary>

Sets the figure's width and height in inches.

</details>
&nbsp;

<br /> 

</details>

<details>
  <summary> 2. What elements do `df.iloc[3, :]` extract from the dataframe `df`?</summary>

The fourth row and all columns

</details>
&nbsp;

<br /> 

</details>

<details>
  <summary> 3. What is the difference between `df.dropna()` and `df.dropna(axis=1)` for dataframe `df`?</summary>

Default drop rows that contains nan values, axis=1 drops all columns with NaN values.

</details>
&nbsp;

<br /> 

</details>

<details>
  <summary> 4. How does `set_palette('magma')` modify a `seaborn` plot?</summary>

Changes the colomap to Magma

</details>
&nbsp;


<br /> 

</details>

<details>
  <summary> 5. What is []?</summary>

An empty `list`. In Python square brackets are used to open and close a list object.

</details>


<br /> 

</details>

<details>
  <summary> 6. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume `spam` contains [2, 4, 6, 8, 10].)</summary>

`spam[2] = 'hello'` 

</details>
&nbsp;

<details>
  <summary> 7. What are the operators for list concatenation and list replication?
 </summary>

*  `+` concatenation
* `*` replication

(similar to string concatenation and replication)

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 8. What is the difference between the append() and insert() list methods? </summary>

The `insert(i, elem)` method adds item `elem` to a list at a specific position `i` in a list, while `append(elem)` adds an item `elem` to the end of the list.

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 9. What are two ways to remove values from a list? </summary>

* `mylist.remove(elem)`
* `del mylist[i]` 

and 

* `mylist.pop(i)`, removes value by index i and return value
* `mylist.clear()`, removes all values from list

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 10. Name a few ways that list values are similar to string values. </summary>

both data types are sequential data types, so

* they are ordered in a defined sequence
* the elements can be accessed via indices
* the meaning of `+` and `*` is the same (concatenation and replication)

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 11. What is the difference between lists and tuples? </summary>

The `list` data type is a mutable object, while the `tuple` is an immutable and fixed size object. This difference means that Python must allocate an extra memory block to extend the list obect when created, which makes lists less memory efficient than tuples. 

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 12. How do you type the tuple value that has just the integer value 42 in it? </summary>

`(42)`

</details>


</details>

<br /> 

</details>

<details>
  <summary> 11. How can you get the tuple form of a list value? How can you get the list form of a tuple value? </summary>

`tuple(mylist)` and `list(mytuple)`

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 13. Variables that 'contain' list values don't actually contain lists directly. What do they contain instead? </summary>

References to objects in memory. When the '=' operator is used to copy a mutable object, it does not create a new object, it only creates a new variable that share reference to the original object.

</details>
&nbsp;

</details>

<br /> 

</details>

<details>
  <summary> 14. What is the difference between copy.copy() and copy.deepcopy()? </summary>

shallow copy (`copy()`): will create new and independent object with same content
deep copy (`deepcopy()`): creates a new object and recursively adds the copies of nested objects present in the original elements.

</details>
&nbsp;