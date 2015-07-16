"""
Grey User database handler
"""
import grey.db

def create_path(creatorId, name, callback):
    grey.db.mongodb.path_db.save({
        'creatorId': creatorId,
        'name': name
    }, callback = callback)
