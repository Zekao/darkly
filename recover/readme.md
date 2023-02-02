# flag12 | scrap 

For this flag, we will download all the files from http://192.168.56.104/.hidden/

We will go through all the files and find the flag, the flag will be in a readme containing the word flag
    
```python
import requests
import re

url = "http://192.168.56.104/.hidden/"
r = requests.get(url)
files = re.findall(r'href="(.*)"', r.text)

for file in files:
    r = requests.get(url + file)
    if "flag" in r.text:
        print(r.text)
```

Let's run it
```bash
python script.py | grep flag
```