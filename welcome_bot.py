from dotenv import load_dotenv
import logging
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.members = True

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='bot.log'
)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        roadmap_channel = discord.utils.get(member.guild.channels, name="roadmap")
        general_information_channel = discord.utils.get(member.guild.channels, name="general_information")
        
        await channel.send(f"""Welcome {member.mention}! Ready to pursue your dreams?
                           
                           General Information: {general_information_channel.mention}
                           Roadmap: {roadmap_channel.mention}""")
        print(f"{member} joined the server")

@bot.event
async def on_disconnect():
    print('Bot is disconnecting...')

@bot.event
async def on_error(event, *args, **kwargs):
    args = ", ".join(list(args))
    kwargs = ", ".join(list(kwargs))
    message = f"An error occurred while handling the {event} event.\n\nArgs: {args}\n\nKwargs: {kwargs}"
    print(message)

def __main__():
    load_dotenv()
    DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
    bot.run(DISCORD_TOKEN)

if os.name != 'nt':
    pid = "/tmp/welcome_bot.pid"
    stderr = "bot_err.log"
    stdout = "bot.log"
    from daemonize import Daemonize

    def daemonize():
        daemon = Daemonize(app="welcome_bot.py", pid=pid, action=__main__, stdout=stdout, stderr=stderr)
        try:
            daemon.start()
        except Exception as e:
            print(f"Failed to start daemon: {e}")

    daemonize()

if __name__ == "__main__":
    __main__()
