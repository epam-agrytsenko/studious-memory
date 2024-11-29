
##### Working with 'csv' and 'json' structures

There is a file [utils/cars.csv](utils/cars.csv).

Use the `csv` library to read the contents of the file.
Convert the data to the `json` format and save it to the file `cars.json`.

Notes:
 * Use [csv.DictReader](https://docs.python.org/2/library/csv.html#csv.DictReader)
 * Use [json.dump](https://docs.python.org/2/library/json.html#json.dump) with the parameter `indent=2`
 * Use the context manager `with` to create the file

---

##### <u>Check yourself</u>:
```
bash$ cat ../task_12/cars.json
[
  {
    "Year": "1997",
    "Make": "Ford",
    "Model": "E350"
  },
  {
    "Year": "2000",
    "Make": "Mercury",
    "Model": "Cougar"
  },
  {
    "Year": "2006",
    "Make": "Dacia",
    "Model": "Logan"
  }
]
```

