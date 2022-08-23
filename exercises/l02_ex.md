# Exercises 2 #

## Pair programming ##

1) __Combining Strings__. 'Adding' two strings produces their concatenation: `a + b` is `ab`. Write a function called `fence()` that takes two parameters called `original` and `wrapper` and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

```py
>>> print(fence('name', '*'))
```

and the output should be

```py
*name*
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
def fence(original, wrapper):
    return wrapper + original + wrapper
```

</details>
&nbsp;

---

## Check your understanding ##

1. What values do the __variables__ `mass` and `age` have after each of the following statements? Test your answer by executing the lines.

```py
1 mass = 47.5
2 age = 122
3 mass = mass * 2.0
4 age = age - 20
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

1. `mass` holds a value of 47.5, `age` does not exist
2. `mass` still holds a value of 47.5, `age` holds a value of 122
3. `mass` now has a value of 95.0, `age`'s value is still 122
4. `mass` still has a value of 95.0, `age` now holds 102


</details>
&nbsp;

2. __Sorting Out References__. Python allows you to assign multiple values to multiple variables in one line by separating the variables and values with commas. What does the following program print out?

```py
first, second = 'James', 'Kirk'
third, fourth = second, first
print(third, fourth)
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

`Kirk James`

</details>
&nbsp;


3. __Seeing Data Types__. What are the data types of the following variables?

```py
planet = 'Earth'
apples = 5
distance = 10.5
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

```py
type(planet)
type(apples)
type(distance)
```

```py
<class 'str'>
<class 'int'>
<class 'float'>
```

</details>
&nbsp;


4. __Return versus print__. Note that `return` and `print()` are not interchangeable. `print()` is a function that prints data to the screen. It enables us, users, see the data. The `return` statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:

```py
def add(a, b):
    print(a + b)
```

What will we see if we execute the following commands?

```py
A = add(7, 3)
print(A)
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

Python will first execute the function `add()` with `a = 7` and `b = 3`, and, therefore, print 10. However, because function `add()` does not have a line that starts with `return` (no return 'statement'), it will, by default, return nothing which is called `None`. Therefore, A will be assigned to `None` and the last line (`print(A)`) will print `None`. As a result, we will see:

```py
10
None
```

</details>
&nbsp;

---

## Practice Questions ##

1. Which of the following is a variable, and which is a string?

```py
spam
'spam'
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

`spam` is a variable and `'spam'` is a string

</details>
&nbsp;


2. Name three data types

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

- sting
- integer
- float

</details>
&nbsp;


3. What is an expressions made up of? What do all expressions do?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

An expression is an instruction that combines values and operators and always evaluates down to a single value.

</details>
&nbsp;


4. What is a statement, e.g., assignment statement `var = 10`

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

A statement is an instruction that the Python interpreter can execute. When you type a statement on the command line, Python executes it and displays the result, if there is one. The result of a print statement is a value.

</details>
&nbsp;


5. What does the variable `spock` contain in the following code

```py
spock = 20
spock + 1
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

the integer `20`

</details>
&nbsp;

6. What should the following two expressions evaluate to

```py
'spam' + 'spamspam'
'spam' * 3
```

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

`''spamspamspam''`

</details>
&nbsp;

7. Why is `spock` a valid variable name and 100 invalid

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

- one word with no spaces
- only use letters, numbers and underscore
- cannot begin with number

| Valid | Invalid |
| --- | --- |
| snake_case | snake-case |
| camelBack | camel back |
| wnumber23 | 23wnumber |
| _23 | 23 |
| TOTAL_SUM | TOTAL_$UM |
| hello | 'hello' |

</details>
&nbsp;

8. What three functions can be used to get the integer, floating-point numner, string version of a value

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

- `int()`
- `float()`
- `str()`

</details>
&nbsp;

9. What is the advantage of functions, and more generally, modular programming?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

modular/manageble & reusable code

</details>
&nbsp;

10. When does the code in a function execute: during function definition or function call?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

function call

</details>
&nbsp;

11. What statement creates a function?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

the `def` statement works as follows. `def` is the keyword for defining a function. The function name is followed by parameter(s) in (). The colon : signals the start of the function body, which is marked by indentation. Inside the function body, the return statement determines the value to be returned. 

</details>
&nbsp;

12. What is the difference between a function and a function call?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

A function call means invoking or calling that function. Unless a function is called there is no use of that function. The difference between the function and function call is, _a function is procedure to achieve a particular result while function call is using this function to achive that task_.

</details>
&nbsp;

13. How many scopes are there in Python?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

two or four depending on how you count

</details>
&nbsp;

14. What happens to a variable in local scope, when the function call returns?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

it is deleted

</details>
&nbsp;

15. What is a return value? Can a return value be part of an expression?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>


Answer: The `return` statement is a special statement that you can use inside a function or method to send the function's result back to the caller. A return statement consists of the return keyword followed by an optional return value. The return value of a Python function can be any Python object.

Yes, because an expression is just a representation of a value. Expressions are composed of values and operators. A function call can be used in an expression because the call evaluates to its return value.

```py
def hello(name):
    return name

print(hello('Spock'))
```

</details>
&nbsp;

16. If a function lacks a return statement, what is the return value of the function call?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

`None`

</details>
&nbsp;

17. What keyword allow you to update a global variable in a function?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

`global`

</details>
&nbsp;

18. What does `None` mean?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

null value

</details>
&nbsp;

19. What does the `import numpy` statement do?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

imports the objects in the numpy namespace

</details>
&nbsp;

20. If you have a function named `randint()` and a module named `random`, how would you import and call `randint`?

</details>
<br /> 
</details>
<details>
  <summary> [Answer] </summary>

`random.randint()`

</details>
&nbsp;
