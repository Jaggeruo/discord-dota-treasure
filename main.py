import json
import discord
from discord.ext import commands

with open("data/data.json", "r") as data_file:
    data_dict = json.load(data_file)
    prefix = data_dict['prefix']
    token = data_dict['token']

client = commands.Bot(command_prefix=prefix, case_insensitive=True)
client.load_extension("cogs.market_features")


@client.event
async def on_ready():
    print("Bot ready")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Opóźnienie: {round(client.latency, 2) * 1000 } ms")


client.run(token)
