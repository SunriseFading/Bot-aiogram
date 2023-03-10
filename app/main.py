import aiogram
import openai

from settings import OPENAI_API_KEY, TELEGRAM_TOKEN
from utils import authorized_user

openai.api_key = OPENAI_API_KEY
bot = aiogram.Bot(TELEGRAM_TOKEN)
dispatcher = aiogram.Dispatcher(bot)

messages: list[dict] = []


@dispatcher.message_handler(commands=["start"])
@authorized_user
async def start_command(message):
    await message.reply("Started")


@dispatcher.message_handler(commands=["clear"])
@authorized_user
async def reset_command(message):
    messages.clear()
    await message.reply("Cleared")


@dispatcher.message_handler(lambda message: not message.text.startswith("/"))
@authorized_user
async def answer_question(message):
    messages.append({"role": "user", "content": message.text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1200,
        messages=messages,
    )

    reply = response.choices[0].message.content

    await message.reply(
        aiogram.utils.markdown.text(reply), parse_mode=aiogram.types.ParseMode.MARKDOWN
    )


if __name__ == "__main__":
    aiogram.executor.start_polling(dispatcher)
