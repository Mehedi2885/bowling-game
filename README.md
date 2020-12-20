# Bowling Game
Bowling game project written in python/django

## Prerequisites
Python3 and above, Django 2.2, django-rest-framework 3.9.2

## Getting started
Install python3 and above
```
pip3 insatll -r requirements.txt
```
Go to project folder:
Start migration of your project
```
python3 manage.py makemigrations 
python3 manage.py migrate    

```
Create superuser:
```
python3 manage.py createsuperuser 
```
Start django development server:
```
python3 manage.py runserver
```
##### To start game call api :
**ip:port/bowling/score/**
##### To get desired player game with id:
**ip:port/bowling/score/id/** 

Now update player game in real time with every ball played with valid data, at invalid data api will send desired message.

valid value are:

```
0-9, X, x, /, -, ''
```





