from aiohttp import web
from handlers import debt_handler

app = web.Application()
app.add_routes([
    web.get('/api/v0/debt', debt_handler),
])

if __name__ == '__main__':
    web.run_app(app)
