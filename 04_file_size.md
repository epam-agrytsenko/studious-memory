
##### File size conversion

Implement a function that takes the file size in bytes (Byte) and converts it to a human-readable format: `Byte`, `Kilobyte`, `Megabyte`, `Gigabyte`.

How many gigabytes are in `sys.maxsize`?

Example:
```python
def file_size(size_in_bytes):
    # implement me
    return '12.6Mb'
```

Notes:
 * Limit the output to Gigabytes.
 * String Format [examples](https://docs.python.org/2/library/string.html#format-examples)
 * This is a very poor implementation: https://stackoverflow.com/a/14822210

---

###### Check yourself
```
assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'
```





 