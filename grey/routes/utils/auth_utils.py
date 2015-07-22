"""
Grey Auth Utility functions
"""
import hashlib, os
import grey
import grey.db.auth_db as AuthDB
from grey.error import AuthError
from grey.routes.utils import mongo_callback

# Find the user salt in a manner that allows unittesting
path = os.path.join(os.path.dirname(grey.__file__), "private.py")
if os.path.exists(path):
    from grey.private import USER_SALT
else:
    USER_SALT = os.environ.get('USER_SALT')

def auth(func):
    def wrapper(self, data):
        @mongo_callback(self)
        def find_callback(result):
            if not result:
                raise AuthError()
            func(self, data=data, userId=result["_id"])

        phone = self.request.headers.get("phone")
        device = self.request.headers.get("device")
        if not phone or not device:
            raise AuthError()
        AuthDB.find_user_id(user_hash(phone, device), find_callback)

    return wrapper

def user_hash(phone, device):
    return hashlib.sha224(USER_SALT + phone + device).hexdigest()
