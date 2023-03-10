import os

AUTHORIZED_USER_ID = int(os.environ.get("AUTHORIZED_USER_ID"))  # type: ignore
TELEGRAM_TOKEN = str(os.environ.get("TELEGRAM_TOKEN"))
OPENAI_API_KEY = str(os.environ.get("OPENAI_API_KEY"))
