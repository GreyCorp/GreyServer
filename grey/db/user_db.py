"""
grey User database handler
"""
from grey.db import mongodb

def find_user_id(hashed, callback):
    mongodb.user_db.find_one({'hashed': hashed}, callback = callback)

def create_user(phone, hashed, callback):
    mongodb.user_db.save({
        'hashed': hashed,
        'phone': phone
    }, callback = callback)
