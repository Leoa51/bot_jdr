import discord
import random
import json
from discord.ext import commands
from src.classes.character import Character
from src.middleWare import middleWare

HP_FILE = "hp_data.json"


# Chargement des données depuis un fichier JSON
def load_hp_data():
    try:
        with open(HP_FILE, "r") as f:
            data = json.load(f)
            return {name: Character(name, hp) for name, hp in data.items()}
    except FileNotFoundError:
        return {}

# Sauvegarde des données dans un fichier JSON
def save_hp_data():
    with open(HP_FILE, "w") as f:
        json.dump({name: personnage.hp for name, personnage in characters.items()}, f)

# Dictionnaire pour stocker les characters
characters = load_hp_data()



async def roll(ctx, faces: int = 6):
    """Lance un dé avec le nombre de faces spécifié (par défaut 6)."""
    if faces < 2:
        await ctx.send("Un dé doit avoir au moins 2 faces !")
    else:
        resultat = random.randint(1, faces)
        await ctx.send(f'🎲 {ctx.author.mention} a lancé un dé à {faces} faces et a obtenu: **{resultat}**!')


async def set_hp(ctx, name: str, hp: int):
    """Définit les points de vie d'un joueur ou d'un ennemi."""
    characters[name] = Character(name, hp)
    save_hp_data()
    await ctx.send(f'✅ {name} a maintenant {hp} PV.')

async def get_hp(ctx, name: str):
    """Affiche les points de vie d'un joueur ou d'un ennemi."""
    if name in characters:
        await ctx.send(f'❤️ {name} a {characters[name].hp} PV.')
    else:
        await ctx.send(f"⚠️ {name} n'a pas encore de PV enregistrés.")


async def soin(ctx, name: str, amount: int):
    """Ajoute des PV à un joueur ou un ennemi."""
    if name in characters:
        characters[name].soigner(amount)
        save_hp_data()
        await ctx.send(f'➕ {name} a été soigné de {amount} PV et a maintenant {characters[name].hp} PV.')
    else:
        await ctx.send(f"⚠️ {name} n'a pas encore de PV enregistrés.")


async def dommage(ctx, name: str, amount: int):
    """Réduit les PV d'un joueur ou d'un ennemi (les PV peuvent devenir négatifs)."""
    if name in characters:
        characters[name].subir_dommage(amount)
        save_hp_data()
        await ctx.send(f'⚔️ {name} a subi {amount} dégâts et a maintenant {characters[name].hp} PV.')
    else:
        await ctx.send(f"⚠️ {name} n'a pas encore de PV enregistrés.")


# Démarrer le bot
# bot.run(TOKEN)
