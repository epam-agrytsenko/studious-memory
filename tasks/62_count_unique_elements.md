#### Count Unique Elements

Write a function that counts the number of unique elements in a list

##### Hints:
 - Use `set`

```python
def count_unique_elements(data: list) -> int:
    return 0  # add your implementation
```


##### <u>Check yourself</u>
```python
assert count_unique_elements([1, 2, 2, 3, 4, 4, 4]) == 4
assert count_unique_elements(["apple", "banana", "apple", "cherry"]) == 3
assert count_unique_elements([1, "1", 1, 2]) == 3
assert count_unique_elements([[1, 2], [1, 2], [1, 2, 3]]) == 2
```

##### Answer the questions:
 - why list with lists as elements doesn't work?
 - how to make it work?
