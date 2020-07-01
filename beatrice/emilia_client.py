import aiohttp
import json


class EmiliaClient:
    DEBT_PATH = '/api/v0/debt'
    TRANSACTIONS_PATH = '/api/v0/transactions'
    ADD_TRANSACTION_PATH = '/api/v0/transaction'

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def _form_url(self, path):
        return f'http://{self.host}:{self.port}{path}'

    async def _send_get_request(self, url, params):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                return await response.json()

    async def _send_post_request(self, url, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=json.dumps(data)) as response:
                return await response.json()

    async def get_debt(self, username):
        url = self._form_url(self.DEBT_PATH)
        params = {
            'username': username,
        }
        return await self._send_get_request(url, params)

    async def get_transactions(self, username):
        url = self._form_url(self.TRANSACTIONS_PATH)
        params = {
            'username': username,
        }
        return await self._send_get_request(url, params)

    async def add_transaction(self, user_from, user_to, amount, message):
        url = self._form_url(self.ADD_TRANSACTION_PATH)
        data = {
            'from': user_from,
            'to': user_to,
            'amount': amount,
            'message': message,
        }

        await self._send_post_request(url, data)
