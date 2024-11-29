
##### Using threading library to verify URL's


The file [utils/links.txt](utils/links.txt) contains a list of URL addresses that need to be validated for accessibility.

We need the most efficient solution. Use the `threading` library to initiate multiple web requests simultaneously.

Save the result of the script execution to a file in JSON format _(see example below)_.

Note:
 * Use the `requests` library (pip install requests).
 * The `Response.ok` property can be useful for determining the validity of the response ([github/requests](https://github.com/requests/requests/blob/d2962f1d55a211a4606d8387b6333de7a21e630d/requests/models.py#L693)).

Example result:
```
[
  {
    "url": "https://www.does_not_exist.com/",
    "is_ok": false,
    "status_code": null
  },
  {
    "url": "http://lucumr.pocoo.org/",
    "is_ok": true,
    "status_code": 200
  },
  {
    "url": "http://jinja.pocoo.org/docs/",
    "is_ok": true,
    "status_code": 200
  }
]
``` 

---
