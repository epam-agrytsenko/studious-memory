#### Convert String to Title Case

Write a function that converts a string to title case, where the first letter of each word is capitalized, and all other letters are lowercase

##### Hints:
1. Use str.split()
2. Use str.capitalize()

```python
def to_title_case(sentence: str) -> str:
    return ""  # add your implementation
```

##### <u>Check yourself</u>:

```python
assert to_title_case("hello world") == "Hello World"
assert to_title_case("python PROGRAMMING") == "Python Programming"
assert to_title_case("already Capitalized") == "Already Capitalized"
```