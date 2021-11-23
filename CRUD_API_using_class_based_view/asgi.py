"""
ASGI config for CRUD_API_using_class_based_view project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUD_API_using_class_based_view.settings')

application = get_asgi_application()
