import requests
import re

url = "http://192.168.56.104/.hidden/"
r = requests.get(url)
files = re.findall(r'href="(.*)"', r.text)

for file in files:
    r = requests.get(url + file)
    new_files = re.findall(r'href="(.*)"', r.text)
    for new_file in new_files:
        r = requests.get(url + file + "/" + new_file)
        if "flag" in r.text:
            print (r.text)
            exit (0)
