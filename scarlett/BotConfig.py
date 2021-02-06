import os
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("APP_ID", 6))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    OWNER_UN = os.environ.get("OWNER_UN", None)
    BOT_NAME = os.environ.get("BOT_NAME", None)
    ABOUT_SECTION = os.environ.get("ABOUT_SECTION", None)
    BOT_SECTION = os.environ.get("BOT_SECTION")
    OWNERSHIPS = os.environ.get("OWNERSHIPS", None)
    COM_SECTION = os.environ.get("COM_SECTION", None)
    FED_SECTION = os.environ.get("FED_SECTION")
