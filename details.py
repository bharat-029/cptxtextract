import os
from os import getenv


API_ID = int(getenv("API_ID", 20491966))
API_HASH = getenv("API_HASH", "aa1c8f86db7f78fe9bfdd77bb48a5b23")
BOT_TOKEN = getenv("BOT_TOKEN", "7914172257:AAHAgAWkrjnJYvGGx6vkNHuEux1KW_II3vk")
OWNER_ID = int(getenv("OWNER_ID", "7168441486"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7168441486").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002374881847"))
