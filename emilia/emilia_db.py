from pymongo import MongoClient
from settings import config


class EmiliaDB:
    def __init__(self, host, user, password, db_name):
        self.client = MongoClient(
            f'mongodb+srv://{user}:{password}@{host}/{db_name}'
            '?retryWrites=true&w=majority'
        )
        self.db = self.client.emilia
        self.users = self.db.users
        self.debt = self.db.debt
        self.transactions = self.db.transactions

    def get_user_by_username(self, username):
        return self.users.find_one({'username': username})

    def get_debt(self, user1, user2):
        """
        returns: reverse, debt_object
            reverse: if True, debt object is from user2 to user1
        """
        debt_user1 = self.debt.find_one({
            'from': user1,
            'to': user2,
        })
        debt_user2 = self.debt.find_one({
            'from': user2,
            'to': user1,
        })

        if debt_user1 is None and debt_user2 is None:
            raise Exception('Debt object not found')

        if debt_user1 is not None and debt_user2 is not None:
            raise Exception('Multiple debt objects')

        if debt_user1 is not None:
            return False, debt_user1
        else:
            return True, debt_user2


db = EmiliaDB(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db_name=config.DB_NAME,
)
