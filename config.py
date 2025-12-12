# Copyright (C) @iamakki001
# Channel: https://t.me/iamvillain77

import re

API_ID = "18674208" # Your Telegram API ID
API_HASH = "96542e74d79f488625cce1d5ced32406" # Your Telegram API Hash
BOT_TOKEN = "8242244894:AAF6e1W6fwFYh4Zuy9u8flMugxEc76OQYhs" # Your Bot Token
OWNER_ID = '5909658683'
# MongoDB connection URI
MONGO_URI = "mongodb+srv://Villainmusic01:deathnote0p@cluster0.nah8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*' #done change here
)
