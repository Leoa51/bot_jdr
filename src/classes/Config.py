import json

import discord
from discord import client

from src.classes.Character import Character


class Config:

    Characters = {}




    def __init__(self):
        self.load_config()

    def load_config(self):
        try:
            with open("config.json", "r") as f:
                Characters_buffer = json.load(f)
                self.Characters = {k: Character(v["name"], v["hp"], v["current_hp"]) for k, v in Characters_buffer.items()}
        except Exception:
            self.Characters = {}

    async def load_config_from_channel(self, ctx):
        try:
            # with open("config.json", "r") as f:
            # channel = discord.utils.get(client.get_all_channels(), name="json")
            channel = discord.utils.get(ctx.guild.text_channels, name="json")
            # print(ctx.guild.text_channels)

            # for message in channel.history(limit=100):
            async for message in channel.history(limit=100):
                if message.content.startswith("json"):
                    Characters_buffer = json.loads(message.content[4:].strip())
                    self.Characters = {k: Character(v["name"], v["hp"], v["current_hp"]) for k, v in Characters_buffer.items()}
                    self.write_config()
                    await ctx.send("Configuration chargée.")
                    break
                else:
                    await ctx.send("Aucune configuration trouvée.")
                # self.Characters = json.load(f)
        except Exception:
            await ctx.send("Aucune configuration trouvée.")
            self.Characters = {}

    async def write_config_on_channel(self, ctx):
        try:
            channel = discord.utils.get(ctx.guild.text_channels, name="json")
            await channel.send("json " + json.dumps({k: v.to_dict() for k, v in self.Characters.items()}))
            await ctx.send("Configuration envoyée au channel json.")
        except Exception as e:
            await ctx.send(f"Aucun channel json trouvée. {e}")


    def write_config(self):
        print(self.Characters)
        with open("config.json", "w") as f:
            json_characters = {str(k): v.to_dict() for k, v in self.Characters.items()}
            json.dump(json_characters, f)


    def get_last_character_id(self):
        try:
            return int(max(self.Characters.keys()))
        except ValueError:
            return 0

    def get_character_by_id(self, id):
        return self.Characters[str(id)]

    def get_character_by_name(self, name):
        for id, character in self.Characters.items():
            if character.name == name:
                return character