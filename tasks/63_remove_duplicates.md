#### Remove duplicates from list

Write a function that removes duplicate elements from a list, preserving the original order of the elements

##### Hints:
 - Keep same order of elements
 - Use a `set` to store seen elements

```python
def remove_duplicates(numbers: list[int]) -> list[int]:
    return []
```

##### <u>Check yourself</u>:
```python
if __name__ == "__main__":
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]    
```