# Kilofarms #

This Repository contains source code for the problem statement given by Kilofarms.

# Table of Contents
- [Instructions to run](#instructions-to-run)
- [Implementation](#implementation)
 - [Stack](#stack)
 - [Features](#features)
 - [API documentation](#api-documentation)

# Instructions to run
1. Run using Docker: The application is containerised using docker.
	1. Change the database URI in app/settings.py file to connect flask application container and mysql container.
	
		```
		SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:supersecret@mysql/kilofarms?host=mysql?port=3306'
		```

	2. Run the following command.
	
		```
		docker-compose up
		```

2. Run from command line:
	1. Make sure mysql is hearing in localhost:3306 and update credentials in database URI in app/settings.py.
	2. Install virtualenv and create and activate a virtualenv
	
		```
		virtualenv venv
		source venv/bin/activate
		```
	
	3. Install the requirements
	
		```
		pip install -r requirements.txt
		```
		
	4. Run the following command to start the flask application
	
		```
		flask run
		```

# Implementation

## Stack
1. REST API Server is built using Flask.
2. Web application is constructed using HTML and CSS.
3. MySQL is used as database and SQLAlchemy is used as ORM to connect flask and MySQL.
4. Postman is used for API documentation.
5. Application is containerised using Docker.

## Features
All the features in the problem statement has been implemented.
### Python REST API Web Server
Two modules have been implemented in Web Server

1. Authentication module
2. Product module

JWT is used for authentication. All the APIs in the problem statement has been implemented.

### Web Pages implemented
1. Home Page
2. Login Page
3. Signup Page
4. Get All Products Page
5. View a Product Page

## API documentation
Check the API documentation [here](https://documenter.getpostman.com/view/12829759/TzCH9pF9)
