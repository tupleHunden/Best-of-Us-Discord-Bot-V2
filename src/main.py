"""
    This is a rewrite of the Discord Bot found at: github.com/tupleHunden/Best-of-Us-Discord-Bot/
"""

import os                           # This will help us work with dotenv easier
import discord                      # This is the main library we will use to interface with Discord
from discord.ext import commands    # Command Extension of the Discord Library
from dotenv import load_dotenv      # dotenv will make it easier to use sensitive tokens/info.

# This will configure the dotenv file to read sensitive tokens for the slack bot
load_dotenv()

# These constants will enable sensitive token info to be used by the bot.
DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# This will create an instance of the discord client named "Stan" for use across the application.
DISCORD_CLIENT = discord.Client()  # TODO: Rename DISCORD_CLIENT to something more user friendly

# This will set the command prefix to !, enabling the bot to listen for !.
BOT = commands.Bot(command_prefix='!')


@DISCORD_CLIENT.event
async def on_ready():
    """
        on_ready() will display a message when the bot is connected to Discord.
    """
    print('{0.user} has successfully connected to Discord'.format(DISCORD_CLIENT))


# This will bring the bot online.
DISCORD_CLIENT.run(DISCORD_BOT_TOKEN)
