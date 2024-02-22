
from aiogram import Bot, Dispatcher, types
# from aiogram.filters import CommandStart

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_hendler(command=["start"])
async def start_command():



