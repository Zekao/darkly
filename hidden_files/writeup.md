# flag 3 | hidden files

For this flag, we will use nikto to scan all accessible route. We find /admin/ page and /whatever/ directory

In /whatever/ we can find htpasswd file and inside we found :
```root:437394baff5aa33daa618be47b75cb49```

The password decrypted is : `qwerty123@`

In the /admin page, after login we got the flag : `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`