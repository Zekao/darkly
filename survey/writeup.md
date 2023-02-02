# flag 1 | html exploit

For this flag, we will use the  `I forgot my password` view, a vulnerability is present when we change the address mail of recover

If we set something different, we will get the flag
```html
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```
Will be changed to
```html
<input type="hidden" name="mail" value="randomvalue" maxlength="15">
```

Boom, we got the flag
`1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0`