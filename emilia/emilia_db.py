from pymongo import MongoClient
from bson.objectid import ObjectId
from settings import config


class EmiliaDB:
    def __init__(self, host, user, password, db_name):
        self.client = MongoClient(
            f'mongodb+srv://{user}:{password}@{host}/{db_name}'
            '?retryWrites=true&w=majority'
        )
        self.db = self.client.emilia
        self.users = self.db.users

    def get_users(self):
        return list(self.users.find())

    def get_user_by_id(self, uid):
        return self.users.find_one({'_id': ObjectId(uid)})

    def get_user_by_username(self, username):
        return self.users.find_one({'username': username})

    def get_debt(self, id):
        pass


db = EmiliaDB(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db_name=config.DB_NAME,
)
