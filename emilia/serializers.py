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
