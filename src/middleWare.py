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
            await commands.soin(ctx, name, amount)

        @bot.command()
        async def dommage(ctx, name: str, amount: int):
            print("command dommage")
            await commands.dommage(self.config, ctx, name, amount)

        # @bot.command()
        # async def help(ctx):
        #     print("command help")
        #     print(commands.Personnage.__subclasses__())






