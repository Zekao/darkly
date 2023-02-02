# flag 7 | redirect 2

For this flag, we will need to be in [this page](http://192.168.56.104/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f)

On the html source code, we can see many comments

```html
<!--You must come from : "https://www.nsa.gov/".-->
```

```html
<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->
```

So we will make a curl request with the user agent `ft_bornToSec` and the referer `https://www.nsa.gov/`

```bash
curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://192.168.56.104/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f | grep flag
```