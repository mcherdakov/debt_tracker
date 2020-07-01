from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from settings import config

from emilia_client import EmiliaClient


bot = Bot(token=config.TG_TOKEN)
dp = Dispatcher(bot)
emilia_client = EmiliaClient(
    host=config.EMILIA_HOST,
    port=config.EMILIA_PORT,
)


@dp.message_handler(commands=['start'])
async def process_start(message):
    await bot.send_message(
        message.from_user.id,
        'Hello! I\'m DebtTracker bot :3 \n'
        'Type /help for actions list'
    )


@dp.message_handler(commands=['help'])
async def process_help(message):
    await bot.send_message(
        message.from_user.id,
        '/t - create new transaction\n'
        '/tlist - transactions list\n'
        '/d - your debts\n'
        'Have fun! UwU'
    )


@dp.message_handler(commands=['d'])
async def process_debts_list(message):
    response = await emilia_client.get_debt(message.from_user.username)
    debts = response.get('debts')
    response_header = f'Your ({message.from_user.username}) debts:\n'
    response_body = '\n'.join([
        f'To {debt.get("to")}: {debt.get("amount")}'
        for debt in debts
    ])

    await bot.send_message(
        message.from_user.id,
        f'{response_header}{response_body}'
    )


@dp.message_handler(commands=['tlist'])
async def process_transactions_list(message):
    response = await emilia_client.get_transactions(
        message.from_user.username,
    )
    response_header = f'Your ({message.from_user.username}) transactions:\n'
    response_body = '\n'.join([
        f'{i + 1}. From {t.get("from")} to {t.get("to")}: {t.get("amount")}\n'
        f'Message: {t.get("message")}'
        for i, t in enumerate(response.get('transactions'))
    ])

    await bot.send_message(
        message.from_user.id,
        f'{response_header}{response_body}',
    )


@dp.message_handler()
async def process_create_transaction(message):
    args = message.text.split()
    amount = float(args[0])
    msg = '' if len(args) == 1 else ' '.join(args[1:])
    user_to = message.from_user.username
    user_from = 'bromigo' if user_to == 'SadDwarf' else 'SadDwarf'

    await emilia_client.add_transaction(user_from, user_to, amount, msg)

    await bot.send_message(
        message.from_user.id,
        'Done <3'
    )

if __name__ == '__main__':
    executor.start_polling(dp)
