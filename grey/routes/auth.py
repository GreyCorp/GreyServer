"""
GreyService Authentication Route
Creating and Maintaining Users
"""
from grey.routes.utils.auth_utils import user_hash
from grey.routes.utils import unpack, mongo_callback
from grey.routes.handler import GreyHandler
import grey.db.auth_db as AuthDB

class AuthHandler(GreyHandler):
    # Create User if doesn't exist
    @unpack(["phone", "device"])
    def login(self, phone, device):
        @mongo_callback(self)
        def create_callback(result):
            self.respond({
                "_id": result,
                "phone": phone,
            })

        @mongo_callback(self)
        def find_callback(result):
            if result:
                self.respond(result)
                return
            AuthDB.create_user(phone, hashed, create_callback)

        hashed = user_hash(phone, device)
        AuthDB.find_user_id(hashed, find_callback)

AuthRoute = (r"/auth/(?P<action>[a-zA-Z]+)?", AuthHandler)
