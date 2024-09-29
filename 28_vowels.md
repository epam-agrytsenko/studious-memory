# Count Vowels and Consonants

#### Problem Statement:
Write a Python function that takes a predefined string and counts the number of vowels and consonants in the string. It should ignore spaces, punctuation, and numbers.

#### Requirements:
 - Ignore spaces, punctuation, and numbers when counting.
 - Treat both uppercase and lowercase letters equally (i.e., "A" and "a" are both vowels).

#### Example:
```python
ss = 'New 2025 year is coming! Yeeeh ;-)'
vowels, consonants = count_letters(ss)

print(f'Vowels: {vowels}')
print(f'Count: {len(vowels)}')
print()
print(f'Consonants: {consonants}')
print(f'Count: {len(consonants)}')
```

---

### Hints:
- Define a set of vowels and consonants. Example: `vowels = {'a', 'e', 'i', 'o', 'u'}`.
- Use string methods like `.lower()` and `.isalpha()`


