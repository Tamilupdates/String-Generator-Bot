from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))
DATABASE_URL = getenv("DATABASE_URL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)