"""
Script to read many types of files.
"""

import json


SECRETS_FORMAT = {"git": ["password"], "telegram": ["token"]}


def is_dict_secret_correct_format(secret_dict: dict) -> bool:
    """
    Checks if a secret dict has the correct format.

    """
    for key, value in SECRETS_FORMAT.items():
        if key not in secret_dict:
            return False
        for secret in value:
            if secret not in secret_dict[key]:
                return False
    return True


def read_json(file_path: str) -> dict:
    """
    Reads a json file.

    """
    with open(file_path, "r") as f:
        secret_dict = json.load(f)
        assert is_dict_secret_correct_format(
            secret_dict
        ), "Secret dict is not in the correct format. It must have the following keys: {}".format(
            SECRETS_FORMAT
        )
        return secret_dict


if __name__ == "__main__":
    print(
        read_json("D:\\PersonalProjects\\bot-telegram\\nero-bot\\secrets\\secrets.json")
    )
