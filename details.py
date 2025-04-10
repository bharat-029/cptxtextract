import os
from os import getenv


API_ID = int(getenv("API_ID", 23664819))
API_HASH = getenv("API_HASH", "3853f97c662d5d08cee5f0d07361361e")
BOT_TOKEN = getenv("BOT_TOKEN", "7668997178:AAF4ulorEaLSEkHGppTHvekl27IOZnbBDNY")
OWNER_ID = int(getenv("OWNER_ID", "8004315740"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8004315740").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-"))
