
# Greeting function

Implement a function that takes `name` and `age` and returns the text:
```python
'Hello, my name is <name>. I am <age> years old!'
```

Implement 3 different solutions:
- Format string using C-style
- Using `.format()` method
- Using F-string

Useful links:
- [Python String Formatting Cheatsheet](https://www.pythoncheatsheet.org/cheatsheet/string-formatting)


### Code example:
``` python
def greeting_c_style(name, age):
    """C-style string formatting with %s (old, rarely used)"""
    return


def greeting_with_format(name, age):
    """Method .format(). Introduced in Python 2"""
    return


def greeting_fstring(name, age):
    """F-string, introduced in Python 3"""
    return


if __name__ == '__main__':
    greeting_c_style('Billy', 20)
    greeting_with_format('Steve', 70)
    greeting_fstring('James', 22)
```