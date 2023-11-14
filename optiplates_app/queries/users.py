from optiplates_app.database_config.db import db

def findUser(fields):
    user_collection = db['Users']
    return user_collection.find_one(fields)

def findUserByMultipleFields(fields):
    user_collection = db['Users']
    return user_collection.find_one({
        "$or": fields
    })

def insertUser(user):
    user_collection = db['Users']
    return user_collection.insert_one(user)