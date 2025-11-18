import os
import sys
import json
from collections.abc import MutableMapping

from dotenv import load_dotenv
load_dotenv()

# Correct way: load from .env file
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("Mongo URI:", MONGO_DB_URL)
