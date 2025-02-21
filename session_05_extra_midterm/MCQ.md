```markdown
# Midterm 

## Multiple-Choice Questions

### Question 1
**Consider the statement:**
```python
L = {'1':1, '2':2, '3':3}
```

**Which is correct?**

- L is a list
- L is immutable
- L contains 6 elements
- L has integer keys
- L maps strings to integers

✅ **Correct Answer:** L maps strings to integers.

### Question 2

**Assume a `break` statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?**

- The program might immediately terminate.
- The function might immediately terminate.
- The loop will always immediately terminate.
- All of the above.
- None of the above.

✅ **Correct Answer:** The loop will always immediately terminate.

### Question 3

**In Python, which of the following is a mutable object?**

- a string
- a tuple
- a list
- all of the above
- none of the above

✅ **Correct Answer:** a list.

### Question 4

**Assume the statement `s[1024] = 3` does not produce an error message. This implies:**

- `type(s)` can be `str`
- `type(s)` can be `tuple`
- `type(s)` can be `list`
- All of the above

✅ **Correct Answer:** `type(s)` can be `list`.

### Question 5

**Consider the code:**

```python
L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3
```

**Which of the following does NOT cause an exception (error) to be thrown?**

- `print(L[3])`
- `print(d['b'])`

- ```python
  for i in range(100001, -1, -2): 
      print(f)
  ```

- `print(int('abc'))`
- None of the above

✅ **Correct Answer:** `for i in range(100001, -1, -2): print(f)`

### Question 6

**Examine the following code snippet:**

```python
stuff  = _____
for thing in stuff:
    if thing == 'iQ':
        print("Found it")
```

**Select all the values of the variable `stuff` that will make the code print "Found it".**

- `["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]`
- `( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" )`
- `[ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ) ]`
- `( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )`
- `["iQ"]`
- `"iQ"`

✅ **Correct Answer:** `["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]`, `( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" )`, `["iQ"]`

### Question 7

**The following Python code is supposed to compute the square of an integer by using successive additions.**

```python
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
```

**Not considering recursion depth limitations, what is wrong with this implementation of procedure `Square`? Check all that apply.**

- It is going to return a wrong value.
- The term `Square` is a reserved Python keyword.
- Function names cannot start with a capital letter.
- The function is never going to return anything.
- Python has arbitrary precision arithmetic.
- This function will not work for negative numbers.
- The call `SquareHelper(abs(x), abs(x))` won't work because you can't have `abs(x)` as both parameters.
- Nothing is wrong; the code is fine as-is.

✅ **Correct Answer:** Nothing is wrong; the code is fine as-is.
