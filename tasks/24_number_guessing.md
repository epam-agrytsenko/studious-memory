# Number Guessing

Create a simple number guessing game in Python where the program generates 
a random number between 1 and 100, and the user has to guess the number. 
The program should give feedback to the user after each guess by telling them 
whether their guess is too high, too low, or correct.

### Requirements
 - The program should generate a random number between 1 and 100.
 - The user is allowed up to **7 guesses** to find the correct number.
 - After each guess, the program should indicate whether the guess was too high, too low, or correct.
 - If the user guesses correctly, congratulate them and exit the program.
 - If the user fails to guess the number in 7 tries, reveal the correct number and end the game.
 - The program should handle invalid inputs (e.g., non-numeric values).


#### Example:
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 7 guesses to find the number.

Guess #1: 50
Too high

Guess #2: 25
Too low

Guess #3: 35
Correct!
```

---

### Hints:
- Use `random.randint(1, 101)` to generate a random number.
- Use a `while True` loop.
- Use **input validation** to handle non-numeric values.

