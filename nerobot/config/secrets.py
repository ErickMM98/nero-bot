"""
Script to manipulate secrets
"""
import nerobot.util.read as read


def read_telegram_token(json_file: str) -> str:
    return read.read_json(json_file)["telegram"]["token"]

