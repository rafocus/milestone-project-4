[![Build Status](https://travis-ci.org/rafocus/milestone-project-4.svg?branch=master)](https://travis-ci.org/rafocus/milestone-project-4)
# Milestone project 4
## Issue Tracker

A web application to serve as a ticket system to track issues, help developers and end users to report and fix bugs, suggest and track the development of features. 

Demo application deployed [here](https://issuetrack2019.herokuapp.com/)  

Demo login:  
Username: testuser  
Password: testpass1  

## UX

### Wireframes: 

<img src="design/wireframes/desktop_list.png" height="300"/><img src="design/wireframes/mobile_list.png"  height="300"/>
<img src="design/wireframes/desktop_detail.png" height="300"/><img src="design/wireframes/mobile_detail.png"  height="300"/>

### User stories:

- A user can view the tickets list on the home page, can view the details of every ticket, the comments, can make payment without being authenticated.
- A user can create an account. 
- An authenticated user can create a ticket of a Bug or feature type, comment, vote, pay for features.
- When a feature ticket is created, a superuser will add a target budget for the funding.
- Users can pay a minimum amount and above for a feature, when the target is reached, the feature can start being implemented.
- A ticket status to indicate: in progress, completed, pending.

## Features

### Existing Features

- User authentication
- List view of all tickets
- Search, results filtering
- Detail view 
- Commenting
- Voting
- Cart
- Checkout
- Payment using Stripe

### Features left to implement

- Blog
- Contact page
- Detailed progress page

## Technologies used

- HTML5, CSS3, Bootstrap
- Javascript
- Python language
- Djamgo framework
- Postgres database system
- Django crispy forms
- Heroku to deploy a Demo app
- Environ
- Whitenoise
- Stripe
- Travis Ci

## Testing
...

## Deployment

- Clone the repository
- Start a virtual environement with pipenv
- Install dependencies with 'pipenv install'
- Initiate a git local repository
- For local testing and development, create .env file and include values for these variables: SECRET_KEY, DEBUG, STRIPE_SECRET, STRIPE_PUBLISHABLE, DATABASE_URL
- Create accounts for Heroku, Stripe
- Create an app in heroku and add postgres addon, DATABASE_URL will be automatically added to the environment varibales. [help](https://devcenter.heroku.com/articles/git)
- In Heroku seetings add environement variables for: SECRET_KEY, DEBUG, STRIPE_SECRET, STRIPE_PUBLISHABLE
- In command line execute the folling commands:  
$ heroku git:remote -a "your_app_name"  
$ git push heroku master  
$ heroku run python manage.py makemigrations  
$ heroku run python manage.py migrate  
$ heroku run python manage.py createsuperuser  
$ heroku run python manage.py collectstatic  

## Credits

### Design

Rafocus
