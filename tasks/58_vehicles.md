#### Vehicles

Create a class that represents a car:

```python
class Car:
    ...
```

Add following attributes:
 - brand
 - model
 - year

Add method `calculate_age`. For example, if car's `year` is 2018, so the age will be current year - car.year

Add method `as_dict` that return car description as python dictionary. Example:
```python
{
    "brand": "Ford",
    "model": "E350",
    "year": 1997
}
```

Create another class `ElectricCar`, subclass form `Car`. Add additional attribute `battery_capacity`.  
Make sure method `as_dict` includes battery capacity as well
