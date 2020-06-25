import json

from aiohttp import web
from emilia_db import db


async def user_handler(request):
    uid = request.query.get('id')
    username = request.query.get('username')
    if uid is not None:
        response_object = {
            'username': db.get_user_by_id(uid)['username']
        }
    elif username is not None:
        response_object = {
            'username': db.get_user_by_username(username)['username']
        }
    else:
        response_object = [
            {
                'username': user['username']
            }
            for user in db.get_users()
        ]

    return web.Response(
        text=json.dumps(response_object)
    )


async def debt_handler(request):
    response_object = [
        {
            'to': '2',
            'amount': 100.2
        }
    ]
    return web.Response(text=json.dumps(response_object))
