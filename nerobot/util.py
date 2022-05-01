"""
Functions to do some useful things.
"""

import os
import sys
import time
import datetime
import subprocess
import logging
import logging.handlers
import re

from collections import OrderedDict
from functools import wraps

from nerobot.config import Config

LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
