import json


class BaseSerializer:
    def __init__(self):
        pass

    def serialize(*args, **kwargs):
        raise NotImplementedError


class DebtSerializer(BaseSerializer):
    def __init__(self, username, debts, many=False):
        # username for correct sign
        self.debts = debts
        self.username = username
        self.many = many

    def serialize_one(self, debt):
        amount = debt.get('amount')
        if debt.get('from') == self.username:
            debt_to = debt.get('to')
        else:
            debt_to = debt.get('from')
            amount = -amount

        return {
            'amount': amount,
            'to': debt_to,
        }

    def serialize(self):
        if not self.many:
            return json.dumps(self.serialize_one(
                self.debts
            ))

        return json.dumps(
            {
                'debts': [
                    self.serialize_one(debt)
                    for debt in self.debts
                ],
            }
        )


class TransactionSerializer(BaseSerializer):
    def __init__(self, transactions, many=False):
        self.transactions = transactions
        self.many = many

    @staticmethod
    def serialize_one(transaction):
        return {
            'from': transaction.get('from'),
            'to': transaction.get('to'),
            'amount': transaction.get('amount'),
            'message': transaction.get('message'),
        }

    def serialize(self):
        if not self.many:
            return json.dumps(self.serialize_one(
                self.transactions
            ))

        return json.dumps(
            {
                'transactions': [
                    self.serialize_one(transaction)
                    for transaction in self.transactions
                ]
            }
        )
