from dotenv import load_dotenv
import logging
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

logging.basicConfig(level=logging.INFO)

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
load_dotenv()
DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
bot.run(DISCORD_TOKEN)
