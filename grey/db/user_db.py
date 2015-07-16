"""
Grey User database handler
"""
import grey.db

def find_user(userId, callback):
    grey.db.mongodb.user_db.find_one({"userId": userId }, callback = callback)

def create_user(user, callback):
    grey.db.mongodb.user_db.save(user, callback = callback)

def update_user(userId, update_dic, callback):
    update_dic = {"$set": update_dic}
    grey.db.mongodb.user_db.find_and_modify(
        query={ 'userId': userId },
        update=update_dic,
        new=True,
        callback = callback
    )
