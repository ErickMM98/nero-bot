from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


class NeroBot(Updater):
    """
    #TODO: Write a description of the class
    This is the principal bot of Erick :O
    """
    def __init__(self, token: str = None, *args, **kwargs) -> None:
        if token is None:
            raise ValueError("Token is required")
        super().__init__(token, *args, **kwargs)
        self.name = "NeroBot"
        self.version = "0.0.1"

    def run(self) -> None:
        logging.warning(f"{self.name} is running...")
        self.dispatcher.add_handler(CommandHandler("hello", hello))
        self.start_polling()
        self.idle()
