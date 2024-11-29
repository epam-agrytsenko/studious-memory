#### Zip Lists into a Dictionary

Write a function zip_into_dict that takes two lists, keys and values, and zips them into a dictionary. 
The function should handle the case where the lists are of different lengths by stopping at the shortest list.

Example:
```python
def zip_into_dict(keys, values):
    return # dictionary formed by zipping keys and values
```

#### <u>Check yourself</u>:
```python
zip_into_dict(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}
zip_into_dict(['name', 'age'], ['Alice', 25, 'extra data']) == {'name': 'Alice', 'age': 25}
```