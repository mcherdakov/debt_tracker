from aiohttp import web
from handlers import (
    debt_handler, transactions_handler, add_transaction_handler,
)
from settings import config

app = web.Application()
app.add_routes([
    web.get('/api/v0/debt', debt_handler),
    web.get('/api/v0/transactions', transactions_handler),
    web.post('/api/v0/transaction', add_transaction_handler),
])

if __name__ == '__main__':
    web.run_app(app, port=config.PORT)
