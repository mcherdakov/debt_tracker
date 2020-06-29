import json
from aiohttp import web
from http import HTTPStatus
from emilia_db import db
from serializers import DebtSerializer


async def debt_handler(request):
    user_from = request.query.get('from')
    user_to = request.query.get('to')

    try:
        reverse, debt = db.get_debt(user_from, user_to)
    except Exception as e:
        return web.Response(
            text=json.dumps(
                {
                    'message': str(e),
                }
            ),
            status=HTTPStatus.BAD_REQUEST,
        )

    response = DebtSerializer(reverse, debt).serialize()
    return web.Response(text=response)
