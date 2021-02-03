# Songs-API 🎵

deployed on heroku https://chillbeats.herokuapp.com/

# GET /song
Returns a list of all the  songs 

Example Response:
```
{
"results": [
{
"artist": "Mama Aiuto ",
"audio": "https://mp3.chillhop.com/serve.php/?mp3=9908",
"cover": "https://i.scdn.co/image/ab67616d00004851d48d24735fd4af023ede3aa1",
"name": "Today Feels Like Everyday"
},
{
"artist": "Cloudchord ",
"audio": "https://mp3.chillhop.com/serve.php/?mp3=9734",
"cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0",
"name": "Inverno"
},
  ]
}
```

# GET /integer

URL Parameters: integer specify the number be number of songs that will be returned

Response: returns specified number of songs
