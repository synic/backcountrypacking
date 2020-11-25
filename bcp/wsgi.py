import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bcp.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
