from .base import *  # noqa

#INSTALLED_APPS += [
#    '',
#]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}