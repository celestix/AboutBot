#(c) DevsExpo 2021
#Stardevs
import inspect
import logging
import re
from pathlib import Path
import functools
from telethon import events
from scarlett import aboutbot
from scarlett import Config

import glob
bothandler = Config.COMMAND_HAND_LER
def aboutbot_cmd(add_cmd, is_args=False):
    def cmd(func):
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        else:
            pattern = bothandler + add_cmd + "$"
        aboutbot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd

def god_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            star = Config.OWNER_ID
            if event.sender_id == star:
                await func(event)
            else:
                pass

        return wrapper

    return decorator

def start_aboutbot(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path
        import scarlett.utils
        path = Path(f"scarlett/plugins/{shortname}.py")
        name = "scarlett.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your About Bot.")
        print("Loaded " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path
        import scarlett.utils
        path = Path(f"scarlett/plugins/{shortname}.py")
        name = "scarlett.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.aboutbot_cmd = aboutbot_cmd
        mod.aboutbot = aboutbot
        mod.Config = Config
        mod.god_only = god_only()
        spec.loader.exec_module(mod)
        sys.modules["scarlett.plugins" + shortname] = mod
        print("IMPORTED " + shortname)
