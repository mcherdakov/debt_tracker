import json
from aiohttp import web
from http import HTTPStatus
from emilia_db import db
from serializers import DebtSerializer, TransactionSerializer


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


async def transactions_handler(request):
    username = request.query.get('username')

    transactions = db.get_transactions(username)
    response = TransactionSerializer(transactions, many=True).serialize()

    return web.Response(text=response)


async def add_transaction_handler(request):
    body = await request.json()
    try:
        db.add_transaction(
            user_from=body.get('from'),
            user_to=body.get('to'),
            amount=float(body.get('amount')),
            message=body.get('message'),
        )
    except ValueError:
        return web.Response(
            text=json.dumps(
                {
                    'message': 'Incorrect amount param',
                },
            ),
            status=HTTPStatus.BAD_REQUEST,
        )

    response_object = {
        'message': 'Transaction created successfully',
    }
    return web.Response(
        text=json.dumps(response_object),
    )
