## Quiz for door stores
1.  Install this libraries to your python path.
    
        pip install django  
        pip install django-bootstrap4  
        pip install django-phonenumber-field[phonenumbers]  
        pip install Pillow  

2.  Create `migrations` in the database. Then create a `superuser`.       
        
        python manage.py migrate
        python manage.py createsuperuser

3. For send messages on e-mail write this code in settings.py:

        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_PORT = 465
        EMAIL_HOST_USER = "your_email@gmail.com"
        EMAIL_HOST_PASSWORD = "your_password"
        EMAIL_USE_SSL = True
