# crudFiled
The repo contains the CRUD operation performed using flask API's
1. Clone the repo on your local directory
2. Below are the 4 API's that have been created using flask and sqlalchemy.
2.1 Post - http://127.0.0.1:5000/post/new 
**  request body for AudioType Song:
**  
{
  "audio_type":"song",
  "title":"something just like this",
  "duration":1000
  }
**  request body form AudioType Podcast:
**  
{
  "audio_type":"podcast",
  "name":"we are champions", 
  "duration":10000, 
  "participants":["amey","pranav"],
  "host":"jack"
  }
  **  request body form AudioType AudioBook:
** 
{
"audio_type":"audiobook","title":"motivation", 
"duration":10000,
"author":"amey",
"narrator":"jack"
}

3. Get - http://127.0.0.1:5000/Song/1 or http://127.0.0.1:5000/Song
4. http://127.0.0.1:5000/**audioType/id** Note: Please provide audioType - Song,Podcast,AudioBook
5. Update - http://127.0.0.1:5000/audiotype/id/update **Note: Please provide audioType - Song,Podcast,AudioBook**
6. Delete - http://127.0.0.1:5000/audiotype/id/delete **Note: Please provide audioType - Song,Podcast,AudioBook**

  
