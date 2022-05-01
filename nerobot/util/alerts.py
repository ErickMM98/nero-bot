"""
Script to send alerts to console and email.
"""

import logging


def send_alert(function: "function"):
    """
    Send an alert to console and email.
    """
    logging.warning(function)



@send_alert
def test_function():
    """
    Test function.
    """
    return 1 + 3


if __name__ == "__main__":
    print(type(send_alert))
    # send_alert('Test')
