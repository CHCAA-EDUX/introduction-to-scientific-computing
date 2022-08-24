# Lesson 3: Container data types # 

To write proper programs, we need data types that can contain multiple values and therefore handle large complex data. The `list`, `array`, and `dataframe` data types can store multiple items in a single vairable and is used to store collections of data.

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/series2d.png?raw=true" alt="tabular data" width="800"/> |
|:--:|
| *Tabular inflammation data set in 2d Software Carpentries. Tabular data formats with $m \times n$ (rows-by-columns), e.g., csv, tab-delimited files, fixed field formats, spreadsheets, HTML tables, and SQL dumps* |



## 3.1: Lists ##

A `list` is a value (a list value) that contains multiple values in an _ordered sequence_

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> date_of_birth = [2233, 2305, 2336]
>>> what_a_mess = ['Q', 11235, False, 3.14]
>>> what_a_mess
['Q', 11235, False, 3.14]
```

### Indexing lists ###

The list data type is a sequence that allow you to index the individual elements (starting from `0`).

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> captains[0]
'Kirk'
>>> captains[1]
'Picard'
>>> captains[2]
'Janeway'
>>> print(f'{captains[2]} is my favorite captain')
'Janeway is my favorite captain'
>>> print(f'{captains[0]} is older than {captains[1]} and {captains[2]}')
```

An index should not exceed the number of values in yhe list (as list index `len(listname) - 1`) and it can _only_ be an integer (type `int`).

```py
>>> captains[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> captains[2.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not float

>>> captains['2']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not str
```

### Nested lists ###

Lists can contain nested (other) list values (i.e., a list of lists), which is a convenient data type for managing hierarchical data.

```py
>>> fridge = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
>>> print(fridge[0])
['pepper', 'zucchini', 'onion']
>>> print(fridge[0][0])
'pepper'
```

### Negative indices ###

Lists allow you to index from the end (instead of the beginning).

```py
>>> captains = ['Kirk', 'Picard', 'Janeway']
>>> captains[-1]
'Janeway'
```

Negative indexing is actually a shorthand for 

```py
>>> captains[len(captains)-1]
'Janeway'
>>> captains[len(captains)-2]
'Picard'
```

### Slicing lists ###

Indices can be used to index individual elements (values) and slices (sequences of elements).

```py
>>> captains = ['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> captains[0:4]
['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> captains[1:3]
['Picard', 'Sisko']
>>> xy_only = captains[0:-1]
>>> xy_only
['Kirk', 'Picard', 'Sisko']
>>> captains[:-1]
['Kirk', 'Picard', 'Sisko']
```

### Chaging values in a list ###

You can assign a value of a list location with an index

``` py
>>> captains = ['Kirk', 'Picard', 'Sisko']
>>> captains[2] = 'Janeway'
>>> captains
['Kirk', 'Picard', 'Janeway']
```

### List concatenation and replication ###

Like strings (`str`) that is also sequence data, you can use `+` to concatenate lists and `*` for replicate lists.

```py
>>> ['Kirk', 'Picard', 'Janeway'] + [2233, 2305, 2336]
['Kirk', 'Picard', 'Janeway', 2233, 2305, 2336]
>>> [2233, 2305, 2336] * 2
[2233, 2305, 2336, 2233, 2305, 2336]
```

If you are left wondering 'how then do i do element-wise multiplication?' after the last example of replication, then look up `numpy` or use a list comprehension

```py
>>> [item * 2 for item in [2233, 2305, 2336]]
[4466, 4610, 4672]
```

### Removing elements from a list ###

```py
>>> captains = ['Kirk', 'Picard', 'Sisko', 'Janeway']
>>> del captains[2]
>>> captains
['Kirk', 'Picard', 'Janeway']
```

### Working with lists ###

List allow you to `append()` new elements (just as concatenating from the end)

```py
users = list()
while True:
    print(f'Please enter the name of user {len(users) + 1} or enter nothing to end.')
    name = input()
    if name == '':
        break
    users.append(name)
print('The users are:')
for name in users:
    print(f'   {name}')
```


#### Iterate over lists ####

Because lists are sequence data, you can iterate through evey element in the list with a `for` or `while` statement.

```py
captains = ['Kirk', 'Picard', 'Janeway']
for captain in captains:
    print(captain)
```

```py
i = 0
while i < len(captains):
    print(captains[i])
    i = i + 1
```

## 3.2: Arrays ##

* __numpy__ is the fundamental library for scientific computing in Python. It provides a high-performance multidimensional _array_ object, and _tools_ for working with these arrays.
* _powerful N-dimensional arrays_ (vectorization, indexing, broadcasting) 
* _numerical computing tools_ (math functions, linear alg, Fourier transform)
* _interoperable_ (wide range of hardware and computing platforms)
* _performant_ (well-optimized C code/Python with the speed of compiled code)
* _easy to use_ (high level syntax)
* _open source_ 



| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/numpy_arrays.png?raw=true" alt="tabular data" width="800"/> |
|:--:|
| *A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.* |

A numpy _array_ is a grid of values
* all values in an array are of the _same type_
* _indexed_ by a tuple of nonnegative integers
* the number of _dimensions_ is the rank of the array (the length of the shape tuple)
* the _shape_ of an array is a tuple of integers giving the size of the array along each dimension

The _rank_ of an array specifies the number of axes/dimensions of the array
* rank 1, 1d array (list)
* rank 2, 2d array (matrix)
* rank 3, 3d array (stack of matrices)

The _shape_ of an array specifies the length of the array in each dimension represented as a tuple

* 1d array (list), shape: (columns,)
* 2d array (matrix), shape: (rows, columns)
* 3d array (stack of matrices), shape: (layers, rows, columns)

the size of an array is the total number of elements

```py
a = np.array([1, 2, 3]) # create rank 1 array
print(type(a))          # <class 'numpy.ndarray'>
print(a.shape)          # (3,)
print(a[0], a[1], a[2]) # 1,2,3
a[0] = 5                # change element of array
print(a)                # [5, 2, 3]

b = np.array([[1, 2, 3], [4, 5, 6]])    # rank 2 array
print(b.shape)                          # (2, 3)
print(b[0, 0], b[0, 1], b[1, 0])        # 1 2 3
```

`numpy` offers multiple functions to create arrays

```py
a = np.zeros((2, 2))    # rank 2 array of zeros
print(a)                # [[0. 0.] [0. 0.]]

b = np.ones((1, 2))     # rank 1 array of ones
print(b)                # [[1. 1.]]

c = np.full((2, 2), 7)  # constant array
print(c)                # [[7. 7.] [7. 7.]]

d = np.eye(2)   # 2x2 identity matrix
print(d)        # [[1. 0.] [0. 1.]]

e = np.random.random((2, 2))    # array with random floats in the half-open interval [0.0, 1.0) = {x | 0 <= x < 1}
print(e)                        # [[0.91940167  0.08143941] [0.68744134  0.87236687]]
```

Like lists, we can index and slice elements in the array along the relevant dimension(-s). 

We start by creating an array `a` with rank 2 and shape (3, 4)

```py
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # rank 2 array, shape (3, 4)
```

We then want to slice the array in order to extract a subarray of tje first 2 rows and columns 1 and 2 - b must be shape (2, 2)

```py
b = a[:2, 1:3]
```

NB: A slice of an array is a view into the same data, if you modify the slice, you will modify the original

```py
print(a[0, 1])  # 2
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])  # 77
```

`numpy` allows for combinations of indexing, ex. mixing  

Create a new array `a`

```py
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Access data in the middel row using integer and array indexing

```py
row_r1 = a[1, :]   # rank 1 view of the second row
```

and slice indexing only

```py
row_r2 = a[1:2, :] # rank 2 view of the second row
```

Compare the two sub-arrays

```py
print(row_r1, row_r1.shape)   # [5 6 7 8] (4,)
print(row_r2, row_r2.shape)   # [[5 6 7 8]] (1, 4)
```

Same distinction holds for accessing array columns

```py
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape) # [2 6 10] (3,)
print(col_r2, col_r2.shape) # [[2] [6] [10]] (3, 1)
```

Integer array indexing

```py
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])  # [1 4 5]
### equivalent to
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
## reuse element in source array
print(a[[0, 0], [1, 1]])
### equivalent to
print(np.array([a[0, 1], a[0, 1]]))
```

A useful trick with integer array indexing is selecting or mutating one element from each row of a matrix with `arange()`

```py
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a)

### create an array of indices
b = np.array([0, 2, 0, 1])

### create index for each row with `arange()`
print(np.arange(4))

### select one element from each row of a using the indices in b
print(a[np.arange(4), b])

### mutate one elemenet from each row using indices in b
a[np.arange(4), b] += 10

print(a)# elementwise addition to column 0
```

boolean indexing

Construct a rank 1 arrray of all elements that meets the condition in a single statement without variable assignment

```py
a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)
print(a[bool_idx])
print(a[a > 2])
```

Numeric data types in `numpy` arrays include integers and floats. A floating point (known as a float) number has decimal points even if that decimal point value is 0. For example: 1.13, 2.0 1234.345. An integer will never have a decimal point. Thus 1.13 would be stored as 1. 1234.345 is stored as 1234. By default `numpy` uses the data type Int64, which stands for 64 bit integer. The 64 simply refers to the memory allocated to store data. 

```py
x = np.array([1, 2])    # numpy chooses data type
print(x.dtype)          # int64

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64)
```

### Mathematical functions for array manipulation ###


`numpy` contains a range of numerical computing tools for manipulating arrays (i.e., array mathematics)

Create two arrays with int64 elements

```py
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
```


We can then perform elemenwise sum

```py

## elementwise sum
print(x + y)
### equivalent 
print(np.add(x, y))
```

elementwise difference

```py
## elementwise difference
print(x - y)
### equivalent
print(np.subtract(x, y))
```

elementwise product

```py
## elementwise product
print(x * y)
### equivalent
print(np.multiply(x, y))
```

elementwise division

```py
## elementwise division
print(x / y)
### equivalent
print(np.divide(x, y))
```

and compute the elementwise square root

```py
## elementwise square root
print(np.sqrt(x))
```

_Matrix multiplication_ is an operation that produces a matrix from two matrices (i.e., we multiply a matrix by another matrix ). Today matrix multiplication is the backbone of modern AI applications. `numpy` offors several linear alg functions that perform matrix multiplication

```py
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])
```


Inner or dot product of vectors

```py
print(v.dot(w))     # 219
print(np.dot(v, w)) # 219
```

Matrix / vector product - both produce rank 1 array [29 67]

```py
print(x.dot(v))
print(np.dot(x, v))
```

Summation of matrix elements

```py
x = np.array([[1, 2], [3, 4]])
print(np.sum(x))            # 10
print(np.sum(x, axis=0))    # [4 6]
print(np.sum(x, axis=1))    # [3 7]
```

Transposition of matrices

```py
x = np.array([[1, 2], [3, 4]])
print(x)
print(x.T)
```

transpose of a rank 1 array has no effect

```py
v = np.array([1, 2, 3])
print(v)
print(v.T)
```

### Application of `numpy` to disaster management ###

by [Rishabh Dwivedi
](https://blog.jovian.ai/application-of-some-numpy-functions-in-various-fields-of-engineering-and-technology-7a4239aa8f26)

The `np.fft.fft(array, axis=None )` computes the one-dimensional discrete Fourier transform and returns the complex _ndarray_ transformed along the axis. We can understand the usage of this function in the field of disaster management by picking up a dataset of earthquakes online and see how we can make use of Fourier transform to solve our query.

> **_Fourier transform:_**  is a mathematical function that transforms any set of values or functions into a  summation of some harmonic functions i.e what it means is that every function which we can think of  is nothing but the summation series of some sine or cosine functions except at a point of discontinuities.  We use this transformation because the series of sine and cosine functions are easy to work upon  compared to other complex functions. Particularly in this post we will use Fourier transform to  represent our function in terms of series of harmonic functions by representing the frequency of each function known as frequency domain representation.

Recent research has showb that the probability of an earthquake increases as the solar 
magnetic activities increases. Our goal is to investigate if the magnetic activity on the sun follows a definite cycle. One of the ways to quantify the magnetic activities is to measure the number of sunspots every year. The `earthquake.csv` dataset contains the historic data of the number of sunspots observed during 1700-2019.

Our task is to find the frequency at which the Solar magnetic activity attains a maximum and further predict, in which of upcoming years, it will be at its peak value. We need to find the frequency which is in cycles/year at which the number of sunspots or the solar magnetic activity attains a maximum, and by reciprocating this frequency we get years after which solar activity again reaches its maximum.

To find the frequency we 1) transform our tabular data into a summation series of harmonic functions having different amplitude & frequencies via Fourier transform function `np.fft.fft`; 2) the frequency of each harmonic function is represented by `np.fft.fftfreq`, and 3) we then plot the frequency vs. magnitude of fourier transform using `matplotlib` to visualize the frequencies at which the magnitude seems to be maximum and that frequency would be the one in cycles/year at which the activity seems to be maximum.

Load and prepare data

```py
earthquake_data = np.loadtxt('dat/earthquake.csv', delimiter=',', skiprows=1)
year = earthquake_data[:, 0]
sample = earthquake_data[:, 1]
n = sample.size    
```

Compute the discrete Fourier transform

```py
A = np.fft.fft(sample) ## Fourier transform of the sunspot data
freq = np.fft.fftfreq(n ,1)  ## frequency of the given data
fft_theoretical = 2 * np.abs(A / n) ## True theoretical fft 
fft_theoretical[0] = 0    ## Ignoring 0 Hz because it seems to be an outlier 
mask = freq > 0  ## filtering frequencies
```

Plot time domain representation

```py
plt.figure(1)
plt.plot(year, sample)
plt.xlabel('Year',fontsize=15)
plt.ylabel('Sunspots',fontsize=15)
plt.title('Time domain representation ',fontsize=25)
plt.savefig('figures/disaster_time_domain.png')
plt.close()
```

Plot frequency domain representation

```py
plt.figure(1)
plt.plot(freq[mask], fft_theoretical[mask]) 
plt.xlim([0, 0.4])
plt.xlabel('Sample Frequencies',fontsize=15)
plt.ylabel('Amplitude',fontsize=15)
plt.title('Frequency domain representation ',fontsize=25)
plt.savefig('figures/disaster_frequency_domain.png')
```

Figure 1           |  Figure 2
:-------------------------:|:-------------------------:
![](https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/disaster_time_domain.png?raw=true)  |  ![](https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/disaster_frequency_domain.png?raw=true)

By looking at figures we can conclude that the frequency at which solar magnetic activity is maximum  at nearby 0.1 cycles/year (Figure 2, x-axis) i.e., after every 10 years (1/0.1) each cycle will repeat itself and the magnetic activity increases which means after every 10 years there is a maximum chance of getting an earthquake. Furthermore, from Figure 1 it looks like the last peak is near 2015 then 2025 is more liekly to get an earthquake because the solar magnetic activity is at its peak.

## 3.3: Dataframes ##


### Learning outcomes ###
* Importing Data from Comma-Separated Values(CSV) files, JSON files etc.
* Filling out missing values in the dataset
* Data Wrangling and Manipulation
* Merging multiple datasets into one dataset
* Exporting our results as Comma-Separated Values(CSV) files, JSON files etc.

### Pandas dataframes ###

[source](https://towardsdatascience.com/introduction-to-pandas-hands-on-tutorial-part-one-2e74f35ab166)

Dataframes are heterogeneous tabular data object that represent Python's equivalent of an (Excel) spreadsheet. Like spreadsheets, dataframes have 2 dimensions or axes, it has rows and columns (also known as series). On top of a dataframe, you will see the name of the columns and on the left side an index. The dataframes is the primary data structure in the `pandas` library. `pandas` is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. `pandas` is designed to make working with 'relational' or 'labeled' data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python.

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/dataframe.png?raw=true" alt="tabular data" width="800"/> |
|:--:|
| *dataframe* |

In `pandas` is a data-centric library, we will work with data from _Spotify_ in this session. The tasks are to identify the songs with the longest/shortest duration and the most/least energy. The [_Spotify_ API](https://developer.spotify.com/documentation/web-api/) provides both features.

### Reading tabular data ###

We start by importing `pandas` and reading tabular data from a `csv` file

```py
import pandas as pd
df = pd.read_csv('dat/spotify.csv')
```

Inspect the dataframe and its size

```py
print(df)
print(df.shape)
```

Inspect the $n$ first rows of the dataframe (by default $n = 5$)

```py
print(df.head())
print(df.head(10))
```

And the $n$ last rows of the dataframe (again, by default $n = 5$)

```py
print(df.tail())
print(df.tail(10))
```

To get a quick overview of the entire dataframe (ex. column data types, number of Null values) use the `info()` method

```py
print(df.info())
```

If you only want to inspect columnar data types, use the `dtypes` property

```py
print(df.dtypes)
```

### Data filtering in a DataFrame ###

For data manipulations, filtering refers to breaking down a dataframe into subsets which pass a particular condition, ex. `music_duration_min < 4`. In the _Spotify_ data set, we can filter on features such as _Danceability_, _Duration_ etc. to filter out Top $K$ songs that match the particular criteria.

Sort the rows on `danceability` and display the 10 first rows (ascending order by default) of `song_title` only

```py
print(df.sort_values('danceability')['song_title'].head(10))
```

Add `artist` names because song titles may not be unique

```py
print(df.sort_values('danceability')[['song_title', 'artist']].head(10))
```
Show the 10 longest songs by sorting on the `duration_ms` feature and extract the last ten rows

```py
print(df.sort_values('duration_ms')[['song_title', 'artist', 'duration_ms']].tail(10))
```

For more complex queries we can combine filtering with boolean indexing in dataframes.

Extract all songs shorter than four minutes (400,000 ms) as filter 1

```py
df_filt = df[df['duration_ms'] < 400000]
print(df_filt.shape)
```

Then sort the extracted songs in ascending order of `energy` (last 10 should suffice)

```py
df_filt2 = df_filt.sort_values('energy')[['song_title', 'artist', 'duration_ms', 'energy']].tail(10)
print(df_filt2)
```

Values are in ascending order by default, convert to descending order and assign to `ans`

```py
ans = df_filt2.sort_values('energy', ascending=False)
print(ans.head(10))
```

### Exporting dataframes ###

If you want to share your resulting dataframe, you can write to `csv` (`txt` or `xlsx` or `json` etc.)

```py
df_filtered = df.sort_values('duration_ms')[['song_title', 'artist', 'duration_ms']].tail(10)
df_filtered.to_csv('dat/spotify_filtered.csv', index=False)
```
