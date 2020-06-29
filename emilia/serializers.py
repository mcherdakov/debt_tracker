import json


class BaseSerializer:
    def __init__(self):
        pass

    def serialize(*args, **kwargs):
        raise NotImplementedError


class DebtSerializer(BaseSerializer):
    def __init__(self, reverse, debt_object):
        self.reverse = reverse
        self.debt_object = debt_object

    def serialize(self):
        amount = self.debt_object.get('amount')
        return json.dumps({
            'amount':
                -amount if self.reverse else amount
        })


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
