# Task Manager

    A simple Task Manager Web app , where User can create Task and also create a Team with other users ,assign task to them. <br/>
    A Basic Profile is also created when user sign up. This is done as a part of Screening test for FOSSEE PYTHON FELLOWSHIP 2019.<br/>

## Requirements

Python 3.6 above,
Django 2.1
Pipenv for managing virtual environment
pillow 5.4.1 for working with image uploaded on server
django-crispy-forms = 1.7.2 for adding Bootstrap on Django Forms

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

## Running the tests

run test using

```
python manage.py test appname
```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
