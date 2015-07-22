"""
GreyService Authentication Route
Creating and Maintaining Users
"""
import grey.db.user_db as UserDB
from grey.routes.utils import unpack, mongo_callback
from grey.routes.handler import GreyHandler
from grey.routes.utils.auth_utils import auth


class UserHandler(GreyHandler):
    # Create User if doesn't exist
    @auth
    @unpack(["user"])
    def create(self, user, userId):
        @mongo_callback(self)
        def create_user_callback(result):
            self.respond(user)

        @mongo_callback(self)
        def find_user_callback(existing_user):
            if existing_user:
                self.respond(existing_user)
                return
            user["userId"] = userId
            UserDB.create_user(user, create_user_callback)
        UserDB.find_user(userId, find_user_callback)

    @auth
    @unpack(["update_dic"])
    def update(self, update_dic, userId):
        @mongo_callback(self)
        def update_callback(result):
            print "Result", result
            self.respond(result)

        UserDB.update_user(userId, update_dic, update_callback)

UserRoute = (r"/user/(?P<action>[a-zA-Z]+)?", UserHandler)
