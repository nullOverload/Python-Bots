import discord
from discord.ext import commands, tasks
import asyncio

TOKEN = "Njk2NzgxMzk2OTQ5MjA1MTcy.XqnE7w.mxGF1aVhi1MBjUB3-s1RZl8EJDI"

client = commands.Bot(command_prefix = "wario ")

@client.event
async def on_ready():
    print("The Bot is ready.")

@client.command()
async def spam(ctx, *, content:str):
        while 1<2:
            await ctx.send(content)
            await asyncio.sleep(0.5)

client.run(TOKEN)
