# flag 2 | html exploit

For this flag, we will use the  `Survey` view, a vulnerability is present when we the value of an input

If we set something different, we will get the flag
```html
<option value="10">10</option>
```
Will be changed to
```html
<option value="42">10</option>
```

We got the flag
`03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa`