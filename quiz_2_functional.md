
### Scopes: Global, Local & Nonlocal
1. **What will be the output of the following code?**
   ```python
   x = 10
   def func():
       x = 20
       print(x)
   func()
   print(x)
   ```
   - a) 10, 10
   - b) 20, 10
   - c) 10, 20
   - d) 20, 20

2. **Which keyword is used to modify the value of a global variable inside a function?**
   - a) global
   - b) local
   - c) nonlocal
   - d) static

3. **What will be the output of the following code?**
   ```python
   x = 5
   def outer():
       x = 10
       def inner():
           nonlocal x
           x += 1
           print(x)
       inner()
       print(x)
   outer()
   ```
   - a) 6, 11
   - b) 11, 11
   - c) 11, 10
   - d) Error

4. **Which of the following statements about the `nonlocal` keyword is true?**
   - a) It can only be used inside global functions.
   - b) It can only be used inside nested functions.
   - c) It refers to the global scope.
   - d) It refers to the local scope of the current function.

5. **In which scope will the following variable `y` be available?**
   ```python
   def func1():
       y = 5
       def func2():
           print(y)
   ```
   - a) Global scope
   - b) Local scope of `func2`
   - c) Local scope of `func1`
   - d) The variable `y` is not available.

### Recursion
6. **What is the base case in the following recursive function?**
   ```python
   def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n-1)
   ```
   - a) `n == 0`
   - b) `n == 1`
   - c) `return n * factorial(n-1)`
   - d) `return 1`

7. **Which of the following is NOT an advantage of using recursion?**
   - a) Recursion can simplify the code.
   - b) Recursion is always faster than iteration.
   - c) Recursion can solve problems that naturally fit a recursive structure.
   - d) Recursion can replace complex nested loops.

8. **What is a common issue that can occur with poorly designed recursive functions?**
   - a) Infinite loop
   - b) Stack overflow
   - c) SyntaxError
   - d) TypeError

9. **What will be the output of the following code?**
   ```python
   def countdown(n):
       if n <= 0:
           print("Blastoff!")
       else:
           print(n)
           countdown(n-1)
   countdown(3)
   ```
   - a) 3 2 1 0 Blastoff!
   - b) 3 2 1 Blastoff!
   - c) 3 2 1
   - d) Error

10. **How does Python handle the depth of recursion by default?**
    - a) Python doesn't limit recursion depth.
    - b) Python has a default recursion limit, which can be changed.
    - c) Python automatically optimizes recursion depth.
    - d) Python throws an error if recursion depth exceeds 100.

### Iterator/Generator
11. **What is the difference between a list and a generator in Python?**
    - a) Lists are faster to iterate over than generators.
    - b) Generators store all values in memory.
    - c) Generators yield items one at a time, lists store all items in memory.
    - d) Lists can only store numeric data types.

12. **What will be the output of the following code?**
    ```python
    def gen():
        yield 1
        yield 2
        yield 3
    g = gen()
    print(next(g))
    print(next(g))
    print(next(g))
    ```
    - a) 1 2 3
    - b) 3 2 1
    - c) Error
    - d) 1 1 1

13. **Which method is used to make an object an iterator?**
    - a) `__iter__()`
    - b) `__next__()`
    - c) `__yield__()`
    - d) `__gen__()`

14. **What will happen if you call `next()` on a generator that has no more items?**
    - a) It will return the last item.
    - b) It will raise a `StopIteration` exception.
    - c) It will return `None`.
    - d) It will reset the generator.

15. **Which of the following statements is true about Python generators?**
    - a) Generators can be iterated only once.
    - b) Generators store all the data in memory.
    - c) Generators require more memory than lists.
    - d) Generators cannot be converted to lists.

### Itertools
16. **Which `itertools` function would you use to create an iterator that returns elements from the iterable as long as a condition is true?**
    - a) `itertools.filterfalse`
    - b) `itertools.dropwhile`
    - c) `itertools.takewhile`
    - d) `itertools.groupby`

17. **What does the `itertools.product` function do?**
    - a) It returns the Cartesian product of input iterables.
    - b) It returns an iterator that aggregates elements from two or more iterables.
    - c) It returns an iterator that returns the product of elements in an iterable.
    - d) It returns combinations of elements in an iterable.

18. **What will be the output of the following code?**
    ```python
    import itertools
    a = [1, 2, 3]
    b = [4, 5]
    result = list(itertools.product(a, b))
    print(result)
    ```
    - a) `[(1, 4), (2, 5)]`
    - b) `[(1, 2, 3), (4, 5)]`
    - c) `[(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]`
    - d) `[(1, 1), (2, 2), (3, 3)]`

19. **Which `itertools` function would you use to create an iterator that cycles through an iterable indefinitely?**
    - a) `itertools.cycle`
    - b) `itertools.repeat`
    - c) `itertools.chain`
    - d) `itertools.accumulate`

### Decorators
20. **Which of the following is NOT true about decorators in Python?**
    - a) Decorators are a way to modify or enhance functions or methods.
    - b) Decorators are executed when the function they decorate is called.
    - c) Decorators can take arguments.
    - d) Decorators can be chained together.
