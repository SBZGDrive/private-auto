import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6008385625:AAH0jG49fq0nBv_HESrYnIH4ctXSoPvztTk")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "10412514"))
    API_HASH = os.environ.get("API_HASH", "4d55a7064ad72adcfa8944f505453a8c")
    AUTH_USERS = os.environ.get("OWNER", "1620169470")

