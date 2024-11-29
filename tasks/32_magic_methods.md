#### Magic Methods

Implement a Python class Time that supports adding and subtracting minutes 
from a given "hour:minute" format using magic methods.

Example:
```python
class Time:
    def __init__(self, time_str):
        # Initialize with a time string "HH:MM"
    
    def __add__(self, minutes):
        # Add minutes

    def __sub__(self, minutes):
        # Subtract minutes
```

#### <u>Check yourself</u>:
```python
t = Time("10:30")
print(t + 90)   # Output: "12:00"
print(t - 30)   # Output: "10:00"
```