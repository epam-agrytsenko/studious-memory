##### IP validation

Write a function to validate an IP address.

Example:
```python
def check_ip(ip_address):
    return True/False
```

Write several solutions:
 * using the `re` library
 * using `socket.inet_aton`

---
 
###### Check yourself
```
assert check_ip('') is False
assert check_ip('192.168.0.1') is True
assert check_ip('0.0.0.1') is True
assert check_ip('10.100.500.32') is False
assert check_ip(700) is False
assert check_ip('127.0.1') is True
```
 
 
