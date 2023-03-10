import functools

from settings import AUTHORIZED_USER_ID


def authorized_user(function):
    @functools.wraps(function)
    async def wrapped(message, *args, **kwargs):
        if message.from_user.id == AUTHORIZED_USER_ID:
            return await function(message, *args, **kwargs)
        else:
            await message.reply("Access denied")

    return wrapped
