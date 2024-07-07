
##### Context manager

Implement the context manager `timer`.

Notes:
 * Use `__enter__` and `__exit__`.

--- 

###### Check yourself:
```
with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)
    
Output:
timer: block 'doing some sleeps' executed in 6.013 sec
```