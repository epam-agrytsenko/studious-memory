#### Min-Max Normalization

Implement a function that performs min-max normalization on a list of numeric values. Min-max normalization scales the values so that they fit in the range [0, 1].

Implementation details:
 - for values in list, find min and max. Return min as `0` and max as `1`
 - scale intermediate numbers in percentage values

Example:
```python
def min_max_normalize(values):
    return # list of normalized values
```

#### <u>Check yourself</u>:
```python
min_max_normalize([1, 2, 3, 4, 5]) == [0.0, 0.25, 0.5, 0.75, 1.0]
```