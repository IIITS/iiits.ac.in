from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import os


os.environ['DJANGO_SETTINGS_MODULE'] ="iiits_config.settings"
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
os.environ['HTTPS'] = "on"

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
os.environ['HTTPS'] = "on"
