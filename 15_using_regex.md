
##### Multiply numbers with regex

Given text:
```
З 35 футболістів, які забили принаймні 7 голів на чемпіонатах світу, лише у трьох футболістів середній показник перевищує 2 голи за гру. Цих 35 гравців представляють 14 футбольних збірних.
```

Write a function that multiplies each digit in the text by 2 and returns the modified text.

###### Example:
```
def my_function(text, multiplier=2):
    # implement me
    return text


>>> my_function('I am 10 years old')
>>> 'I am 20 years old'

>>> my_function('I am 10 years old', multiplier=25)
>>> 'I am 250 years old'
```

###### Notes:
 - Use `re.sub` https://docs.python.org/3/library/re.html#re.sub
 - Pay attention to the `repl` parameter (repl can be a string or a function)

---