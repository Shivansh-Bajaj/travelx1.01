"""
WSGI config for travelx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travelx.settings")

application = get_wsgi_application()
<<<<<<< HEAD
try:
    from dj_static import Cling
    application = Cling(get_wsgi_application())
except:
    pass
=======
>>>>>>> 98ad4f5cb0d1e0e19eb4292a20824df88566a645
