from aiohttp import web
from handlers import debt_handler, user_handler

app = web.Application()
app.add_routes([
    web.get('/api/v0/debt', debt_handler),
    web.get('/api/v0/user', user_handler)
])

if __name__ == '__main__':
    web.run_app(app)
