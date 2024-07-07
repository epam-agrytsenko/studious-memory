
##### Multiprocessing library

To solve problem #5 (Multiples of 3 and 5), multiple different algorithms were implemented. The most popular ones are listed in the file [utils/multiples_of_three_and_five.py](utils/multiples_of_three_and_five.py).

Let's find out which of the proposed algorithms is the most efficient.

Use the `multiprocessing` library to run all 4 functions in parallel. You will also need the `@timeit` decorator or the `timer` context manager.

Answer the question:
 * why don't we use the `threading` library to solve this problem?

---

###### Check yourself:
```
bash$ python multiples_of_three_and_five.py

Output:

math_formula() -> 0.0 sec
several_for_loops() -> 28.89 sec
iterate_over_fifteen() -> 41.32 sec
simple_iteration() -> 66.87 sec
```
