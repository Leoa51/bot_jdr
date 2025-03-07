# import commands
# from . import commands
from functools import wraps

from src import commands
# from src.commands import check_rights_wrapper

def check_rights_wrapper(func):
    @wraps(func)
    async def wrapper(ctx, *args, **kwargs):
        if ctx.author.guild_permissions.administrator:
            # await ctx.send("Vous avez les droits nécessaires.")
            return await func(ctx, *args, **kwargs)
        else:
            await ctx.send("Vous n'avez pas les droits nécessaires.")
            return
    return wrapper


class middleWare:
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

        @bot.event
        async def on_ready():
            print(f'Connecté en tant que {self.bot.user}')

        @bot.command()
        async def exit(ctx):
            print("command exit")
            self.last_ctx = ctx
            await bot.close()

        @bot.event
        async def on_disconnect():
            config.write_config()
            print("Le bot est en train de se déconnecter...")
            await config.write_config_on_channel(self.last_ctx)
            # Ajoutez ici le code que vous souhaitez exécuter avant que le bot ne s'arrête

        # @bot.event
        # async def on_close():
        #     print("Le bot est en train de fermer la connexion...")
        #     # Ajoutez ici le code que vous souhaitez exécuter avant que le bot ne s'arrête


        @bot.command()
        @check_rights_wrapper
        async def json(ctx):
            print("command json")
            await commands.json(self.config, ctx)

        @bot.command()
        @check_rights_wrapper
        async def write_json(ctx):
            print("command write_config_on_channel")
            await config.write_config_on_channel(ctx)


        @bot.command()
        @check_rights_wrapper
        async def roll(ctx, dice: str = "1d100"):
            print("command roll")
            # await commands.check_rights(ctx)
            await commands.roll(ctx, dice)

        @bot.command()
        async def create_character(ctx, name: str, hp: int):
            print("command create_character")
            await commands.create_character(self.config, ctx, name, hp)




        @bot.command()
        async def get_hp(ctx, name: str):
            print("command get_hp")
            await commands.get_hp(ctx, name)

        @bot.command()
        async def set_hp(ctx, name: str, hp: int):
            print("command set_hp")
            await commands.set_hp(ctx, name, hp)

        @bot.command()
        async def soin(ctx, name: str, amount: int):
            print("command soin")
            await commands.heal(self.config, ctx, name, amount)

        @bot.command()
        async def dommage(ctx, name: str, amount: int):
            print("command dommage")
            await commands.dommage(self.config, ctx, name, amount)

        @bot.command()
        @check_rights_wrapper
        async def delete_character(ctx, name: str):
            print("command delete_character")
            await commands.delete_character_by_name(self.config, ctx, name)

        @bot.command()
        @check_rights_wrapper
        async def delete_character_by_id(ctx, id: str):
            print("command delete_character by id")
            await commands.delete_character_by_id(self.config, ctx, id)





