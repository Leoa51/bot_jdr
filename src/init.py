import discord
import random
import json
from discord.ext import commands

class init:
    def __init__(self):
        self.TOKEN = "token"
        intents = discord.Intents.default()
        intents.message_content = True
        bot = commands.Bot(command_prefix='!', intents=intents)
        self.bot = bot


    async def init(self):
        pass