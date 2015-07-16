"""
Grey Request/Response Utils
"""
import json, urlparse

from grey.error import MissingField, InvalidJSON, MongoError, GreyError

def mongo_callback(req):
    def decorator(func):
        def wrapper(result, error):
            try:
                if error:
                    raise MongoError(error)
                func(result)
            except GreyError as e:
                req.respond(e.message, e.code)
        return wrapper
    return decorator

def unpack(arguments = []):
    """
    Unpack arguments to be used in methods wrapped
    """
    def decorator(func):
        def wrapper(_self, data, **kwargs):
            data = smart_parse(data)
            try:
                args = [data[item] for item in arguments]
            except KeyError:
                raise MissingField(item)
            func(_self, *args, **kwargs)
        return wrapper
    return decorator

def form_urlencoded_parse(body):
    """
    Parse x-www-form-url encoded data
    """
    try:
        data = urlparse.parse_qs(body, strict_parsing=True)
        for key in data:
            data[key] = data[key][0]
        return data
    except ValueError:
        raise InvalidJSON()

def smart_parse(body):
    """
    Handle json, fall back to x-www-form-urlencoded
    """
    try:
        data_dict = json.loads(body)
    except ValueError:
        return form_urlencoded_parse(body)
    return data_dict
