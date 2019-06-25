import discord
from discord.ext import commands

prefix = 'c;'
bot = commands.Bot(prefix)


@bot.command()
async def calendar(ctx):
    raise NotImplementedError()


@bot.event
async def on_ready():
    global guilds

    guilds = dict()
    for guild in bot.guilds:
        guilds[guild.id] = GuildInfo(guild)

    print(f'Logged into {str(len(guilds))} guilds:')
    for guild in list(guilds.values()):
        print(f'\t{guild.name}:{guild.id}')
    print("Calendar is up and running.")


if __name__ == '__main__':
    global source_path
    source_path = os.path.dirname(os.path.abspath(__file__))

    logging.basicConfig(level=logging.ERROR)

    file = open('secret.txt')
    secret = file.read()
    file.close()

    bot.run(secret)
