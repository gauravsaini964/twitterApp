
# SortaLikeTwitter

Sorta like twitter is a project in Django/ReactJs which imitates basic feature of twitter like tweeting, commenting, and liking a tweet.


# Tech Stack

 1. Python 3.8.2
 2. Django 2.2
 3. DjangoRestFramework
 4. JWT for Auth
 5. ReactJS
 6. Redux

## Steps to run

 - Method 1
	 - Backend
		 1. Clone the project
		 2. Change directory to twitter_backend
		 3. Make new virtual env based on python 3.8.2
		 4. Activate virtual env
		 5. Run `pip install -r requirements.txt` inside virtual env
		 6. Run `python manage.py migrate` in root folder
		 7. Run `python manage.py runserver 0.0.0.0:8000` to start application server'
	 - Frontend
		 - After step 1 above
		 - Change directory to twitter_frontend
		 - Run yarn install to install dependencies
		 - After that `yarn start` to start the frontend server.
			 
 - Method 2 : Docker Images
	 - Backend
		 1. Clone the project
		 2. Change directory to twitter_backend
		 3. Run `docker build -t yourdockerusername/twitterbackend -f Dockerfile.dev .`
		 4. Then execute `docker run -p 8000:8000 yourdockerusername/twitterbackend`
	 - Frontend
		 1. Clone the project
		 2. Change directory to twitter_frontend
		 3. Run `docker build -t yourdockerusername/twitterfrontend -f Dockerfile.dev .`
		 4. Then execute `docker run -it -p 3000:3000 sainigaurav/twitterfrontend`

 - Method 3 : Docker Compose
		 1. Clone the project
		 2. Run `docker-compose up --build`
		 3. Use `docker-compose up` for subsequent run.
		 

## API List
The project contains 10 APIs in total.
Here is the postman collection for the APIs:
[API - Collection](https://www.getpostman.com/collections/9194d62363a5275cd298)



## ToDo

 - [X] Dockerize this application

