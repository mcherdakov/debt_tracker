from os import environ


class Config:
    def __init__(self):
        self.PORT = environ.get('PORT', 8000)
        self.DB_HOST = environ.get('DB_HOST', 'emilia-wlp2v.mongodb.net')
        self.DB_USER = environ.get('DB_USER', 'admin')
        self.DB_PASSWORD = environ.get('DB_PASSWORD', 'password')
        self.DB_NAME = environ.get('DB_NAME', 'emilia')
