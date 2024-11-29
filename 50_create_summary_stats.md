#### Create Summary Statistics

Write a function that calculates and returns the summary statistics (mean, median, mode) of a list of numbers.

Note:
 - use `json.dumps(obj, indent=2)` for formatting output

Example:
```python
import json

def summary_statistics(numbers):
    return # dictionary with keys 'min', 'avg', 'max'

if __name__ == '__main__':
    res = summary_statistics([1, 2, 3, 4, 4, 5, 5, 5])
    print(json.dumps(res, indent=2))
```

#### <u>Check yourself</u>:

Expected output:
```python
{
  "min": 3.625, 
  "agv": 4.0,
  "max": 5
}
```
