
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

 1. Method 1
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
		 

## API List
The project contains 10 APIs in total.
Here is the postman collection for the APIs:
[API - Collection](https://www.getpostman.com/collections/9194d62363a5275cd298)



## ToDo

 - [ ] Dockerize this application

