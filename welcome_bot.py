import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.

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
        
        await channel.send(f'Welcome {member.mention}! Glad to have you with us!\n\nGeneral Information: {general_information_channel.mention}\nRoadmap: {roadmap_channel.mention}')

DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
bot.run(DISCORD_TOKEN)
