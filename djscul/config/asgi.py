# standard library
import os

# Django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develop')

application = get_asgi_application()
