# Find the Second Largest Number

Write a Python program that takes a list of numbers and finds the **second largest** number in the list.

#### Requirements:
 - If the list contains fewer than two unique numbers, the program should raise an error
 - If there are enough values, the program should find and display the second largest number
 - Ignore all non-number values

#### Example:
```python

[1, 33, 5, -12, 3.3, 'Dog', 100.0, 5, True, 5]

# second largest number is 33

```

---

### Validation rules
- Not enough values or empty list
- Items in a list are not numbers

### Hints:
- Use **set()** to remove duplicate numbers.
- Sort the list and access the second largest value using indexing


