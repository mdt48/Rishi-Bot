import discord
import os
from dotenv import load_dotenv

bot = discord.Client()
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
@bot.event 
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count += 1

    print("rishi-bot is in " + str(guild_count) + " guilds.")    

@bot.event
async def on_message(message):
    # if message.content == "hello":
    #     await message.channel.send("Im geeked")
    if message.author.bot:
        return
    await message.channel.send("Im geeked")


bot.run(DISCORD_TOKEN)