# from src import init
# import src.commands
# from src.middleWare import middleWare

from src import *
from src.middleWare import middleWare

if __name__ == "__main__":
    conf = init.init()
    bot = conf.bot
    middleWare(bot)
    bot.run(conf.TOKEN)

