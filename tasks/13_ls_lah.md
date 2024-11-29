##### Unix 'ls -lh' on Python

Similarly to the `ls -lh` command for Unix systems, implement a Python module that displays the contents of a directory.

Notes:
 1. To get the contents of a directory, use `os.listdir`
 2. Use `os.stat` to get information about each file
 3. Use the [prettytable](http://zetcode.com/python/prettytable/) library
   ```pip install prettytable```
    Column names: Mode, Owner, Group, Size, File name
 4. Use the `pwd` and `grp` libraries to get the username and group

---
 