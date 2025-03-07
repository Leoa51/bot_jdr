import discord
import random
import json
from discord.ext import commands
from src.classes.Character import Character
from src.classes.Config import Config
from src.middleWare import middleWare
import re

HP_FILE = "hp_data.json"



async def json(config, ctx):
    await config.load_config_from_channel(ctx)
    # await ctx.send(config.Characters.keys())


# @check_rights_wrapper
async def roll(ctx, dice: str = "1d100"):
    """Lance plusieurs dés avec la syntaxe NdF (ex: 3d10 pour 3 dés à 10 faces)."""
    match = re.fullmatch(r"(\d+)d(\d+)", dice)
    if not match:
        await ctx.send("Format invalide ! Utilise la forme NdF, par exemple: 3d10. Ex: !roll 2d6.")
        return

    num_dice, faces = map(int, match.groups())
    if num_dice < 1 or faces < 2:
        await ctx.send("Le nombre de dés doit être au moins 1 et chaque dé doit avoir au moins 2 faces.")
        return

    rolls = [random.randint(1, faces) for _ in range(num_dice)]
    total = sum(rolls)
    await ctx.send(f'🎲 {ctx.author.mention} a lancé {num_dice}d{faces}: {rolls} (Total: {total})')


async def dommage(config, ctx, name, amount):
    character = config.get_character_by_name(name)
    character.take_damage(amount)
    # config.write_config()
    await ctx.send(f'{ "❤️" if character.current_hp > 0 else "☠️"} {name} a maintenant {character.current_hp} PV.')


async def heal(config, ctx, name, amount):
    character = config.get_character_by_name(name)
    character.heal(amount)
    # config.write_config()

    await ctx.send(f'❤️ {name} a maintenant {character.current_hp} PV.')


async def create_character(config, ctx, name, hp):
    new_character = Character(name, hp)
    id = config.get_last_character_id() + 1
    config.Characters[str(id)] = new_character
    config.write_config()
    await ctx.send(f'✅ {name} a été créé avec {hp} PV.')

async def delete_character_by_name(config : Config, ctx, name):
    character_id = config.get_character_id_by_name(name)
    config.Characters.pop(character_id)
    config.write_config()
    await ctx.send(f'✅ {name}, {character_id} a été supprimé.')


async def delete_character_by_id(config : Config, ctx, id):
    config.Characters.pop(id)
    config.write_config()
    await ctx.send(f'✅ {id} a été supprimé.')












#
# characters = []
#
# async def set_hp(ctx, name: str, hp: int):
#     """Définit les points de vie d'un joueur ou d'un ennemi."""
#     characters[name] = Character(name, hp)
#     save_hp_data()
#     await ctx.send(f'✅ {name} a maintenant {hp} PV.')
#
# async def get_hp(ctx, name: str):
#     """Affiche les points de vie d'un joueur ou d'un ennemi."""
#     if name in characters:
#         await ctx.send(f'❤️ {name} a {characters[name].hp} PV.')
#     else:
#         await ctx.send(f"⚠️ {name} n'a pas encore de PV enregistrés.")
#
#
# async def soin(ctx, name: str, amount: int):
#     """Ajoute des PV à un joueur ou un ennemi."""
#     if name in characters:
#         characters[name].soigner(amount)
#         save_hp_data()
#         await ctx.send(f'➕ {name} a été soigné de {amount} PV et a maintenant {characters[name].hp} PV.')
#     else:
#         await ctx.send(f"⚠️ {name} n'a pas encore de PV enregistrés.")
#
#
#
#
#
# # Démarrer le bot
# # bot.run(TOKEN)
