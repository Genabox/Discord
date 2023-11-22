import nextcord
from nextcord.ext import commands
from sympy import *
import datetime

TOKEN = ''
channel_id =   # Replace your channel ID 

def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Укажите имя файла журнала
log_file = "bot_log.txt"

@bot.event
async def on_ready():
    print(f"@ === -- The bot successfully logged in as: {bot.user.name} -- === @ Discord")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id != channel_id:
        return

    expression = message.content
    now = get_current_time()

    try:
        # Проверяем, заканчивается ли выражение оператором.
        if expression.endswith(("+", "-", "*", "/", "^")):
            raise ValueError("НекоррCALCULATION ERROR: the expression ends with the operator.")

        result = N(expression)
        result_str = f'{result:.2f}' if isinstance(result, Float) else str(result)

        # Выводим результат выражения в зеленом цвете вместе с датой и временем.
        log_message = f'[{now}] [CALCULATORBOT] CALCULATION: {expression} = {result_str}'
        print(log_message)
        await message.channel.send(f'Результат: {result_str}')

        # Записываем сообщение в журнал
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_message)
        
    except Exception as e:

        # Выводим ошибку в красном цвете вместе с датой и временем.
        log_message = f'[{now}] [CALCULATORBOT] ERROR: {str(e)}'
        print(log_message)
        await message.channel.send(f'[{now}] ERROR: {str(e)}')

        # Записываем сообщение в журнал
        with open(log_file, "a") as f:
            f.write(log_message)

    await bot.process_commands(message)

bot.run(TOKEN)
