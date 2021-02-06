#(c) @StarDevs
#Developed By @anonyindian
#Don't Copy Without Credits
#Leechers Gonna Be Fucked Up
from . import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest


@aboutbot_cmd("start", is_args=False)
async def _(event):
    
    who = await aboutbot(GetFullUserRequest(event.sender_id))
    name = who.user.first_name
    uname = Config.OWNER_UN
    botname = Config.BOT_NAME
    await aboutbot.send_message(event.chat_id, f"**Hey {name}, I am {botname}.\n\nI am assistant of {uname}\n\nYou can check his info through me.😊**", 
                                buttons=[
                                    [Button.inline("Help:💬", data="help")],
                                    [Button.url("Deploy Your Own Bot🤩", url="https://heroku.com/deploy?template=https://github.com/anonyindian/aboutbot")]
                                ])
    
@aboutbot.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    uname = Config.OWNER_UN
    botname = Config.BOT_NAME
    if Config.BOT_SECTION == "None" and Config.FED_SECTION == "None":
        await event.edit(f"**Hello there, \nMy name is {botname}.\nI am {uname}'s assistant.**\n\nClick below buttons to find specific info about my master.",
                        buttons=[
                            [Button.inline("About", data="about"), Button.inline("Channels & Groups", data="grups")],
                            [Button.inline("Communities", data="coms")]
                        ])
    elif Config.BOT_SECTION == "None":
        await event.edit(f"**Hello there, \nMy name is {botname}.\nI am {uname}'s assistant.**\n\nClick below buttons to find specific info about my master.", 
                        buttons=[
                            [Button.inline("About", data="about"), Button.inline("Channels & Groups", data="grups")],
                            [Button.inline("Communities", data="coms"), Button.inline("Fed", data="fed")]
                        ])
        
    elif Config.FED_SECTION == "None":
         await event.edit(f"**Hello there, \nMy name is {botname}.\nI am {uname}'s assistant.**\n\nClick below buttons to find specific info about my master.", 
                        buttons=[
                            [Button.inline("About", data="about"), Button.inline("Channels & Groups", data="grups")],
                            [Button.inline("Communities", data="coms"), Button.inline("Bots", data="bots")]
                        ])
    
    else:
         await event.edit(f"**Hello there, \nMy name is {botname}.\nI am {uname}'s assistant.**\n\nClick below buttons to find specific info about my master.", 
                        buttons=[
                            [Button.inline("About", data="about"), Button.inline("Bots", data="bots"), Button.inline("Channels & Groups", data="grups")],
                            [Button.inline("Communities", data="coms"), Button.inline("Fed", data="fed")]
                        ])

@aboutbot.on(events.callbackquery.CallbackQuery(data="about"))
async def _(event):
    abttxt = Config.ABOUT_SECTION
    await event.edit(f"{abttxt}", 
                        buttons=[
                            [Button.inline("Return", data="help")]
                        ])

@aboutbot.on(events.callbackquery.CallbackQuery(data="bots"))
async def _(event):
    bottxt = Config.BOT_SECTION
    await event.edit(f"{bottxt}", 
                        buttons=[
                            [Button.inline("Return", data="help")]
                        ])

@aboutbot.on(events.callbackquery.CallbackQuery(data="grups"))
async def _(event):
    ownergrups = Config.OWNERSHIPS
    await event.edit(f"{ownergrups}", 
                        buttons=[
                            [Button.inline("Return", data="help")]
                        ])

@aboutbot.on(events.callbackquery.CallbackQuery(data="coms"))
async def _(event):
    coms = Config.COM_SECTION
    await event.edit(f"{coms}", 
                        buttons=[
                            [Button.inline("Return", data="help")]
                        ])
  
@aboutbot.on(events.callbackquery.CallbackQuery(data="fed"))
async def _(event):
    feds = Config.FED_SECTION
    await event.edit(f"{feds}", 
                        buttons=[
                            [Button.inline("Return", data="help")]
                        ])
