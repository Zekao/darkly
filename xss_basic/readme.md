# flag13 | xss injection

For this flag, we will do a second xss injection but this time on the feedback form.

we will enter a user (by example a) and set as comment 
```css
<script>alert</script>
```

and we will get the flag on the page
