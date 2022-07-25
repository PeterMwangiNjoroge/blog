# blog
A blogging system developed with python django web framework.
To run the code on your local system, ensure you have python and git installed then do the following:
> * `git clone https://github.com/mwass/blog.git`
> * `cd blog`
> * `python -m venv venv_blog`
> * `venv_blog\Scripts\activate` in Windows or `source venv_blog/bin/activate` in unix
> * `pip install django` to install django
> * `pip install django-crispy-forms` to install django crispy forms
> * `python manage.py makemigrations my_blog` to make migrations
> * `python manage.py migrate` to make apply migrations
> * `python manage.py createsupeuser` to create super user
> * `python manage.py runserver` to spin a development server
> * visit 127.0.0.1:8000
A live version of this system is running on https://petermaara2.pythonanywhere.com/
