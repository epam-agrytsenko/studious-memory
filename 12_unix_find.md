##### Unix `find' on Python

Similarly to the Unix utility `find`, implement a Python module for finding files and directories on the file system.

Pay attention to the script [utils/find_util](utils/find_util)
```
bash$ ./find_util /usr/ -name "*.pyc" -type f
```

Where `*.pyc` is the pattern of file name(s) in the [shell-pattern](https://www.gnu.org/software/findutils/manual/html_node/find_html/Shell-Pattern-Matching.html) format.

###### Notes:
 * Use `os.walk`
 * Use `os.path.join`
 * To check if a file name matches the pattern, use `fnmatch.fnmatch`

###### Answer the question:
 * How many `*.pyc` files are in your Git repository?

---
