# from src import init
# import src.commands
# from src.middleWare import middleWare

# from src import *
import src
from src.classes.Config import Config
# from src.middleWare import middleWare

if __name__ == "__main__":
    conf = src.init.init()
    bot = conf.bot
    json_data = conf.config
    src.middleWare.middleWare(bot, conf.config)
    bot.run(conf.TOKEN)

