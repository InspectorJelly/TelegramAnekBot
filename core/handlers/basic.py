from aiogram.types import Message


async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}")


