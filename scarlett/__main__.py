#(c) DevsExpo 2021
#Stardevs
from sys import argv
from scarlett import Config
from scarlett import aboutbot
from scarlett import logging
from pathlib import Path
from sys import argv
import telethon.utils
from telethon import TelegramClient
from scarlett.utils import aboutbot_cmd, start_aboutbot
import glob



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    aboutbot.start(bot_token=Config.BOT_TOKEN)
    
path = "scarlett/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_aboutbot(shortname.replace(".py", ""))

print("Scarlett's All Systems Ready")
print("Run with your own about decription")
print("Developed By @anonyindian")
print("(c)StarDevs 2021")

if len(argv) not in (1, 3, 4):
    aboutbot.disconnect()
else:
    aboutbot.run_until_disconnected()
