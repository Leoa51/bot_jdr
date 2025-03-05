# import commands
# from . import commands
from src import commands


class middleWare:
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_ready():
            print(f'Connecté en tant que {self.bot.user}')

        @bot.command()
        async def roll(ctx, faces: int = 6):
            print("command roll")
            await commands.roll(ctx, faces)


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
            await commands.dommage(ctx, name, amount)

        # @bot.command()
        # async def help(ctx):
        #     print("command help")
        #     print(commands.Personnage.__subclasses__())






