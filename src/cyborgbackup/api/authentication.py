# Python
import logging
import hashlib
import hmac
import json

# Django
from django.conf import settings
from django.utils.encoding import smart_text
from django.contrib.auth.models import User

# Django REST Framework
from rest_framework import authentication
from rest_framework import exceptions

logger = logging.getLogger('cyborgbackup.api.authentication')


class LoggedBasicAuthentication(authentication.BasicAuthentication):

    def authenticate(self, request):
        ret = super(LoggedBasicAuthentication, self).authenticate(request)
        if ret:
            username = ret[0].username if ret[0] else '<none>'
            logger.debug(smart_text(u"User {} performed a {} to {} through the API".format(username, request.method, request.path)))
        return ret

    def authenticate_header(self, request):
        return super(LoggedBasicAuthentication, self).authenticate_header(request)


class SessionAuthentication(authentication.SessionAuthentication):

    def authenticate_header(self, request):
        return 'Session'

    def enforce_csrf(self, request):
        return None
