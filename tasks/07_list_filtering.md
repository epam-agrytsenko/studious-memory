
##### List filtering

Given an object of type list():
```python
l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
```

Implement a function that filters only `integer` (int) values from this list.

Write several solutions:
 * using a for loop
 * using list comprehensions
 * using filter() + lambda

Example:

```
def filter_list(l):
    return  # [1, 2, 4, 10, 33]
```

---

##### <u>Check yourself</u>: 
```
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```