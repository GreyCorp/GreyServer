"""
GreyServer Errors
"""

class GreyError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class RouteNotFound(GreyError):
    def __init__(self, action):
        GreyError.__init__(self,
            "%s route could not be found" % action,
            404
        )

class MissingField(GreyError):
    def __init__(self, field):
        GreyError.__init__(self,
            "%s field was not provided" % field,
            400
        )

class InvalidJSON(GreyError):
    def __init__(self):
        GreyError.__init__(self,
            "No JSON object could be decoded.",
            400
        )

class AuthError(GreyError):
    def __init__(self):
        GreyError.__init__(self,
            "User not authenticated",
            401
        )

class MongoError(GreyError):
    def __init__(self, message):
        GreyError.__init__(self,
            message,
            500
        )
