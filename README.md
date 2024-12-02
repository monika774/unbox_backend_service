Project setup backend  :-
Create virtual environment 
Run commands :  python mange.py makemigrations
                                  Python manage py migrate 
For creating user run:
python mage.py createsuperuser
Then give admin and password

I have set admin -speed and password - speed

This is database setup:-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SpeedDataDB',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

Run :  python manage.py runserver
