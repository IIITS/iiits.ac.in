from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import os
<<<<<<< HEAD

os.environ['DJANGO_SETTINGS_MODULE'] ="iiits_config.settings"
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
os.environ['HTTPS'] = "on"

=======
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
os.environ['HTTPS'] = "on"
>>>>>>> d91a6c4794ef75e9177cc93f14e31d22b9fe2cd0
