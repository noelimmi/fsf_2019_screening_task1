# Task Manager

A simple Task Manager Web app , where User can create Task and also
create a Team with other users ,assign task to them.
A Basic Profile is also created when user sign up.
This is done as a part of Screening test for FOSSEE PYTHON FELLOWSHIP 2019.

## Requirements

Python 3.6 above,
Django 2.1,
Pipenv for managing virtual environment,
pillow 5.4.1 for working with image uploaded on server,
django-crispy-forms = 1.7.2 for adding Bootstrap on Django Forms.

## Features

Users can register and login.  
Create Personal Task or can create a Team.  
User can add other members in System as team-members.  
User can assign task to his team members.  
Team members can comment on those tasks.  
Only Team members Can View Team Task and Comment on it.  
Only Team Admin can create Task in his team.






## Added features

A basic Profile is set up when user sign up, also user can update his profile.<br/>
Teams also can have team icon.<br/>
Images uploaded on server is resized to reduce space.

### Installing

Install pipenv using pip

```
pip install pipenv
```

Check if pipenv is added to your Environment Path

Create a Virtual Path by running following command

```
pipenv shell
```

It will create Pipfile

Install the requirements which can be found in requirements.txt, To install automatically just run

```
pipenv install
```

Once done navigate to taskmanager where manage.py file can be found

```
cd taskmanager
```

To start Django server,run

```
python manage.py runserver
```

If done correctly, Web app is up and running ,register as user and try signing in

## ScreenShots
![Memberaddremove](https://user-images.githubusercontent.com/28575372/55363842-26259600-54fc-11e9-8168-a231a73ee01d.JPG)
![Register](https://user-images.githubusercontent.com/28575372/55363843-26be2c80-54fc-11e9-9310-dfedf0ef4529.JPG)
![TeamDetail](https://user-images.githubusercontent.com/28575372/55363846-26be2c80-54fc-11e9-8d4a-5c74ef69b089.JPG)
![UserProfile](https://user-images.githubusercontent.com/28575372/55363847-2756c300-54fc-11e9-84ed-68ce7469b0e7.JPG)
![UserTask](https://user-images.githubusercontent.com/28575372/55363848-2756c300-54fc-11e9-885d-17f6f2f5fd3c.JPG)
![UserTaskCreation](https://user-images.githubusercontent.com/28575372/55363850-27ef5980-54fc-11e9-8f4a-c9d4ae563b20.JPG)
![Comments](https://user-images.githubusercontent.com/28575372/55363851-27ef5980-54fc-11e9-99c1-d25cb5efe155.JPG)
![CreatedndEnrolledTeam](https://user-images.githubusercontent.com/28575372/55363852-2887f000-54fc-11e9-9a1d-23b89ef14f36.JPG)
![grouptaskdetails](https://user-images.githubusercontent.com/28575372/55363853-2887f000-54fc-11e9-8abc-6135036a3e8f.JPG)
![Grouptasks](https://user-images.githubusercontent.com/28575372/55363854-2887f000-54fc-11e9-814b-23b5a1e9c4f4.JPG)
![Login](https://user-images.githubusercontent.com/28575372/55363855-29208680-54fc-11e9-81f4-dc4cf9eaee40.JPG)

## Running the tests

run test using

```
python manage.py test appname
```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
