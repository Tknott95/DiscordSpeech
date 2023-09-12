import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
# END KEY SETTING 

from colors import clr

from talk import Talk

print('\n' + clr.cyan + '  TOC_BOT RUNNNING... \n' + clr.clear)

import discord
import re

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

_talk = Talk()

@client.event
async def on_ready():
    print(clr.bold + '  We have logged in as {0.user}'.format(client) + clr.clear)

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!talk'):
        match = re.search(r"!talk (.*)", message.content)
        _talk.run(match)

        await message.channel.send(file=discord.File('new.wav'))


client.run(DISCORD_TOKEN)
