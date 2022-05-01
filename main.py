from nerobot import NeroBot
from nerobot.config.secrets import read_telegram_token

if __name__ == "__main__":
    token = read_telegram_token("PATH_TO_TOKEN")
    NeroBot(token).run()