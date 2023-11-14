from pymongo import MongoClient
from optiplates_app.database_config import config

client = MongoClient(config.MONGO_URI)
db = client.get_database()
