#### Sum of Digits in Text

Write a function that takes a string (which may contain both digits and non-digit characters) and returns the sum of all the digits.

##### Hints

1. Use str.isdigit() to filter digits
2. Use type conversion (e.g., int())

Implement different solutions
1. Use `for` loop 
2. Use list comprehension
3. Use regexp


```python

def sum_of_digits(text: str) -> int:
    return 0  # add your implementation
```

##### <u>Check yourself</u>:

```python
assert sum_of_digits("abc123") == 6
assert sum_of_digits("4 apples, 5 bananas") == 9
assert sum_of_digits("no digits") == 0
```