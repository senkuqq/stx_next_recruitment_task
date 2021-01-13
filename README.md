# Stx Next recruitment task

Rest api for fetching and storing data about books from GoogleApi.

Application is able to retrieve data from googleapi and then store it in database, 
that includes updating existing ones. To do that simply ```POST /api/v1/db/``` with body ```{"q":"your-query"}```

There is also endpoint for retrieving already imported books - ```GET /api/v1/books/``` 
and ```GET /api/v1/books/<bookid>```

To filter by author or published date, add at the end of the url ```?author="Jan Kowalski"``` or ```?published_date=1995```

To sort ascending or descending by published date use ```?sort=published_date```
or ```?sort=-published_date```

# Building

```sh
$ git clone https://github.com/senkuqq/stx_next_recruitment_task.git
$ cd stx_next_recruitment_task
$ docker build -t web:latest .
```

# Running the application
Run docker image.
```sh
$ docker run -d --name app -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
```

To ensure everything is running properly run.

```sh
$ docker exec -it app python manage.py test
```
Create superuser.
```sh
$ docker exec -it app python manage.py createsuperuser
```

# Online
You can check online version on [heroku](http://stx-next-recruitment-task.herokuapp.com/api/v1/).

There is file stx-next-recruitment-heroku.postman_collection.json which You can import to Postman and try endpoints by yourself! 


# Comments
* I decided to include makemigration and migrations in dockerfile to simplify 
running the application for the first time
  
* As googleapi  limit results to 10 records by default, one ```POST api/v1/db```
can import maximum of 10 records
