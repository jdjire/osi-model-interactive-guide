import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osi_guide.settings')

# Vercel Python runtime looks for `app` as the entrypoint.
app = get_wsgi_application()
