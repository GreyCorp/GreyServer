"""
Grey Auth database handler
"""
import grey.db

def find_user_id(hashed, callback):
    grey.db.mongodb.auth_db.find_one({'hashed': hashed}, callback = callback)

def create_user(phone, hashed, callback):
    grey.db.mongodb.auth_db.save({
        'hashed': hashed,
        'phone': phone
    }, callback = callback)
