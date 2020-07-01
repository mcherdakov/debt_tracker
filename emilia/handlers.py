import json
from aiohttp import web
from http import HTTPStatus
from emilia_db import db
from serializers import DebtSerializer, TransactionSerializer


CTYPE = 'application/json'


async def debt_handler(request):
    username = request.query.get('username')

    try:
        debts = db.get_user_debts(username)
    except Exception as e:
        return web.Response(
            text=json.dumps(
                {
                    'message': str(e),
                }
            ),
            status=HTTPStatus.BAD_REQUEST,
            content_type=CTYPE,
        )

    response = DebtSerializer(username, debts, many=True).serialize()
    return web.Response(
        text=response,
        content_type=CTYPE,
    )


async def transactions_handler(request):
    username = request.query.get('username')

    transactions = db.get_transactions(username)
    response = TransactionSerializer(transactions, many=True).serialize()

    return web.Response(
        text=response,
        content_type=CTYPE,
    )


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
            content_type=CTYPE,
        )

    response_object = {
        'message': 'Transaction created successfully',
    }
    return web.Response(
        text=json.dumps(response_object),
        content_type=CTYPE,
    )
