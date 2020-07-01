from os import environ


class Config:
    def __init__(self):
        self.TG_TOKEN = environ.get('TG_TOKEN')
        self.EMILIA_HOST = environ.get('EMILIA_HOST', '0.0.0.0')
        self.EMILIA_PORT = environ.get('EMILIA_PORT', '8000')
