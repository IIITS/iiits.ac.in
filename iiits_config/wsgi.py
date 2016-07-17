from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import os
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
os.environ['HTTPS'] = "on"