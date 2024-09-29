# Even and Odd Numbers

Write a Python function that takes a predefined list of numbers and separates them into two lists: one containing all the even numbers and the other containing all the odd numbers. The function should return both lists.

#### Requirements:
1. The function should be called `separate(numbers)` and accept a list of integers as an argument.
2. The function should create two separate lists:
   - One for **even numbers**.
   - One for **odd numbers**.
3. The function should return both lists (even and odd).

#### Example:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = separate(numbers)

print('Even numbers:', even)
print('Odd numbers:', odd)
```

Expected Output:
```
Even numbers: [2, 4, 6, 8, 10]
Odd numbers: [1, 3, 5, 7, 9]
```

---

### Requirement:
 - Implement 2 **different** solutions: using `for` loop and list comprehensions
