"""
Grey User database handler
"""
from grey.db import mongodb

def create_path(creatorId, name, callback):
    mongodb.path_db.save({
        'creatorId': creatorId,
        'name': name
    }, callback = callback)
