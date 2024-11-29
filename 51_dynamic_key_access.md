#### Dynamic Key Access in Dictionaries

Write a function that can access a deeply nested value in a dictionary using a dynamic key chain. 
The keys will be provided in a list, and you must navigate through the dictionary dynamically.

Example:
```python
def access_nested_dict(data_dict, key_list):
    return # Nested value
```

#### <u>Check yourself</u>:
```python
data = {
    'a': {
        'b': {
            'c': 'd'
        }
    }
}
key_chain = ['a', 'b', 'c']
access_nested_dict(data, key_chain) == 'd'
```