# config/settings.py

import os

BASE_URL = os.getenv("BASE_URL", "https://blazedemo.com")
MIN_WAIT = int(os.getenv("MIN_WAIT", 1))
MAX_WAIT = int(os.getenv("MAX_WAIT", 5))
USERS = int(os.getenv("USERS", 50))
SPAWN_RATE = int(os.getenv("SPAWN_RATE", 10))
RUN_TIME = os.getenv("RUN_TIME", "1m")
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"